"""MCP server for observability (VictoriaLogs and VictoriaTraces)."""

import asyncio
import json
from typing import Any

import httpx
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool
from pydantic import BaseModel

from mcp_obs.settings import resolve_settings


class LogsSearchParams(BaseModel):
    query: str = ""
    limit: int = 10


class LogsErrorCountParams(BaseModel):
    service: str = ""
    hours: int = 1


class TracesListParams(BaseModel):
    service: str = ""
    limit: int = 10


class TracesGetParams(BaseModel):
    trace_id: str


def _text(data: Any) -> list[TextContent]:
    if isinstance(data, BaseModel):
        payload = data.model_dump()
    elif isinstance(data, list):
        payload = [item.model_dump() if isinstance(item, BaseModel) else item for item in data]
    else:
        payload = data
    return [TextContent(type="text", text=json.dumps(payload, ensure_ascii=False, indent=2))]


def create_server(http_client: httpx.AsyncClient) -> Server:
    settings = resolve_settings()
    server = Server("mcp-obs")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        return [
            Tool(
                name="logs_search",
                description="Search logs in VictoriaLogs using LogsQL query",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {"type": "string", "description": "LogsQL query (e.g., _time:1h service.name:\"LMS\" severity:ERROR)"},
                        "limit": {"type": "integer", "description": "Maximum number of results", "default": 10},
                    },
                    "required": ["query"],
                },
            ),
            Tool(
                name="logs_error_count",
                description="Count errors per service over a time window",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "service": {"type": "string", "description": "Service name to filter (optional)"},
                        "hours": {"type": "integer", "description": "Time window in hours", "default": 1},
                    },
                },
            ),
            Tool(
                name="traces_list",
                description="List recent traces for a service from VictoriaTraces",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "service": {"type": "string", "description": "Service name"},
                        "limit": {"type": "integer", "description": "Maximum number of traces", "default": 10},
                    },
                    "required": ["service"],
                },
            ),
            Tool(
                name="traces_get",
                description="Fetch a specific trace by ID from VictoriaTraces",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "trace_id": {"type": "string", "description": "Trace ID to fetch"},
                    },
                    "required": ["trace_id"],
                },
            ),
        ]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any] | None) -> list[TextContent]:
        try:
            if name == "logs_search":
                params = LogsSearchParams.model_validate(arguments or {})
                query = params.query.replace(" ", "+")
                url = f"{settings.victorialogs_url}/select/logsql/query?query={query}&limit={params.limit}"
                resp = await http_client.get(url)
                resp.raise_for_status()
                return _text(resp.json())

            elif name == "logs_error_count":
                params = LogsErrorCountParams.model_validate(arguments or {})
                hours = params.hours
                service_filter = f" service.name:\"{params.service}\"" if params.service else ""
                query = f"_time:{hours}h severity:ERROR{service_filter}"
                url = f"{settings.victorialogs_url}/select/logsql/query?query={query}&limit=1000"
                resp = await http_client.get(url)
                resp.raise_for_status()
                logs = resp.json() if isinstance(resp.json(), list) else [resp.json()]
                count = len(logs)
                return _text({"error_count": count, "service": params.service or "all", "hours": hours})

            elif name == "traces_list":
                params = TracesListParams.model_validate(arguments or {})
                url = f"{settings.victoriatraces_url}/select/jaeger/api/traces?service={params.service}&limit={params.limit}"
                resp = await http_client.get(url)
                resp.raise_for_status()
                return _text(resp.json())

            elif name == "traces_get":
                params = TracesGetParams.model_validate(arguments or {})
                url = f"{settings.victoriatraces_url}/select/jaeger/api/traces/{params.trace_id}"
                resp = await http_client.get(url)
                resp.raise_for_status()
                return _text(resp.json())

            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]

        except Exception as exc:
            return [TextContent(type="text", text=f"Error: {type(exc).__name__}: {exc}")]

    return server


async def main() -> None:
    settings = resolve_settings()
    async with httpx.AsyncClient(base_url="", timeout=30.0) as client:
        server = create_server(client)
        async with stdio_server() as (read_stream, write_stream):
            init_options = server.create_initialization_options()
            await server.run(read_stream, write_stream, init_options)


if __name__ == "__main__":
    asyncio.run(main())
