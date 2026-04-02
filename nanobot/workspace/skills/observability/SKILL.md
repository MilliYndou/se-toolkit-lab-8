---
name: observability
description: Use VictoriaLogs and VictoriaTraces MCP tools for observability data
always: true
---

# Observability Skill

You have access to observability tools via MCP for querying logs and traces.

## Available Tools

- logs_search — Search logs in VictoriaLogs using LogsQL query
- logs_error_count — Count errors per service over a time window
- traces_list — List recent traces for a service from VictoriaTraces
- traces_get — Fetch a specific trace by ID from VictoriaTraces

## Strategy

### When the user asks about errors or issues:

1. First call logs_error_count to see if there are recent errors
2. If errors exist, call logs_search with a query like "_time:10m severity:ERROR service.name:Learning Management Service" to get details
3. If you find a trace_id in the log results, call traces_get to fetch the full trace
4. Summarize findings concisely — do not dump raw JSON

### When the user asks about a specific service health:

1. Call logs_error_count with the service name and a recent time window (e.g., 10 minutes)
2. If errors exist, use logs_search to get more details
3. Optionally use traces_list to see recent traces for that service

### Query tips:

- Use _time:10m for recent errors (last 10 minutes)
- Use service.name:"Learning Management Service" to filter by service
- Use severity:ERROR to filter for errors only
- Extract trace_id from log results to fetch full traces

### Response formatting:

- Summarize findings in plain language
- Mention the number of errors found and time window
- If a trace is fetched, explain what went wrong in the span hierarchy
- Keep responses concise and focused on the user question

## Example interactions:

User: Any LMS backend errors in the last 10 minutes?
Action: Call logs_error_count with service="Learning Management Service", hours=0 (or use logs_search with _time:10m)

User: What happened in trace abc123?
Action: Call traces_get with trace_id="abc123"

User: Show me recent errors
Action: Call logs_search with query="_time:10m severity:ERROR"
