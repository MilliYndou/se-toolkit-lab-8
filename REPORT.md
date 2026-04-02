# Lab 8 — Report

## Task 1A — Bare agent

**Test command:**
cd ~/se-toolkit-lab-8/nanobot
uv run python -m nanobot.cli.commands agent --session cli:task1a -c ./config.json -m What is the agentic loop?

**Agent response (copy-pasted from terminal):**

🐈 nanobot
The agentic loop is the fundamental cycle that an AI agent follows to accomplish tasks. It typically consists of these core stages:

 1 Perceive — Gather information from the environment (user input, files, APIs, sensors, etc.)
 2 Reason/Plan — Analyze the information, determine goals, and decide on actions to take
 3 Act — Execute the chosen actions (call tools, modify files, send messages, etc.)
 4 Observe — Receive feedback from the actions taken (outputs, errors, state changes)
 5 Repeat — Use the new information to continue the loop until the goal is achieved

---

## Task 1B — Agent with LMS tools

**Test command:**
cd ~/se-toolkit-lab-8/nanobot
uv run python -m nanobot.cli.commands agent --session cli:task1b -c ./config.json -m What labs are available?

**Agent response (copy-pasted from terminal):**

🐈 nanobot
Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

Let me know which lab you would like to explore!

**Tool call log:**
Tool call: mcp_lms_lms_labs({})

---

## Task 1C — Skill prompt

**Test command:**
cd ~/se-toolkit-lab-8/nanobot
uv run python -m nanobot.cli.commands agent --session cli:task1c -c ./config.json -m Show me the scores

**Agent response (copy-pasted from terminal):**

🐈 nanobot
I will help you view the scores. First, let me check which labs are available in the LMS.

🐈 nanobot
Here are the available labs:

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 — lab-08

Which lab would you like to see the scores for? Please specify by lab ID (e.g., lab-01, lab-02, etc.).

**Skill file location:** nanobot/workspace/skills/lms/SKILL.md

---

## Task 2A — Deployed agent

Nanobot gateway is running with:
- WebChat channel enabled on port 8765
- MCP server lms: connected, 9 tools registered
- MCP server webchat: connected, 1 tools registered
- Agent loop started

---

## Task 2B — Web client

WebSocket endpoint: /ws/chat on port 42002
Flutter client: http://vm-ip:42002/flutter
Access key: 12345

---

## Task 2A — Deployed agent

Nanobot gateway startup log:

Channels enabled: webchat
WebChat relay listening on 127.0.0.1:8766
WebChat starting on 0.0.0.0:8765
server listening on 0.0.0.0:8765
MCP server lms: connected, 9 tools registered
MCP server webchat: connected, 1 tools registered
Agent loop started

---

## Task 2B — Web client

WebSocket test response:
Here are the available labs:
lab-01: Lab 01 – Products, Architecture & Roles
lab-02: Lab 02 — Run, Fix, and Deploy a Backend Service
lab-03: Lab 03 — Backend API: Explore, Debug, Implement, Deploy
lab-04: Lab 04 — Testing, Front-end, and AI Agents
lab-05: Lab 05 — Data Pipeline and Analytics Dashboard
lab-06: Lab 06 — Build Your Own Agent
lab-07: Lab 07 — Build a Client with an AI Coding Agent
lab-08: lab-08

Flutter client: http://vm-ip:42002/flutter
Access key: 12345

---
## Task 3A — Structured logging

Happy-path log excerpt (status 200):
{\"_time\": \"2026-04-01T23:57:52.919Z\", \"severity\": \"INFO\", \"service.name\": \"Learning Management Service\", \"event\": \"request_started\", \"trace_id\": \"a1713b6ac54a251ad4dac048abd48ba0\"}
{\"_time\": \"2026-04-01T23:57:52.920Z\", \"severity\": \"INFO\", \"service.name\": \"Learning Management Service\", \"event\": \"auth_success\", \"trace_id\": \"a1713b6ac54a251ad4dac048abd48ba0\"}
{\"_time\": \"2026-04-01T23:57:52.920Z\", \"severity\": \"INFO\", \"service.name\": \"Learning Management Service\", \"event\": \"db_query\", \"table\": \"item\"}
{\"_time\": \"2026-04-01T23:57:53.241Z\", \"severity\": \"INFO\", \"service.name\": \"Learning Management Service\", \"event\": \"request_completed\", \"trace_id\": \"a1713b6ac54a251ad4dac048abd48ba0\"}

Error-path log excerpt (db_query with error):
{\"_time\": \"2026-04-01T23:57:53.241Z\", \"severity\": \"ERROR\", \"service.name\": \"Learning Management Service\", \"event\": \"db_query\", \"error\": \"[Errno -2] Name or service not known\", \"trace_id\": \"a1713b6ac54a251ad4dac048abd48ba0\", \"span_id\": \"8c61c56fe4e7bd6e\"}

VictoriaLogs UI: http://vm-ip:42002/utils/victorialogs/select/vmui
Query: _time:1h service.name:Learning Management Service severity:ERROR

## Task 3B — Traces

VictoriaTraces UI: http://vm-ip:42002/utils/victoriatraces

Healthy trace: trace_id=1ff969f07f5d7b054110de0fc8267cf3
Span hierarchy: request_started -> auth_success -> db_query -> request_completed (200 OK)

Error trace: trace_id=210008ca7cf723536de841d6b29504af
Span hierarchy: request_started -> auth_success -> db_query (ERROR: connection is closed)


---

## Task 3C — Observability MCP tools

### Agent response (normal conditions):

Question: Any LMS backend errors in the last 10 minutes?

Agent response:
"Based on my investigation:

LMS Backend Status: Healthy

The LMS backend is currently healthy with 56 items in the database.
Error Count: No errors found in the last 10 minutes for the Learning Management Service.

Trace Analysis: Retrieved recent traces showing normal operation with successful database queries and request completion."

Tool calls observed:

mcp_obs_logs_error_count({"service": "Learning Management Service", "hours": 0})
mcp_obs_logs_search({"query": "_time:10m service.name:\"Learning Management Service\" severity:ERROR", "limit": 10})
mcp_obs_logs_search({"query": "_time:10m severity:ERROR", "limit": 5})
mcp_obs_traces_list({"service": "Learning Management Service", "limit": 5})

### Agent response (after triggering failure):

Question: Any LMS backend errors in the last 10 minutes?

Agent response: "The LMS backend is currently unhealthy and returning HTTP 404 errors. This means the service is not available at the moment."

Tool calls observed:

mcp_obs_logs_error_count({"service": "Learning Management Service", "hours": 0})
mcp_obs_logs_search({"query": "_time:10m severity:ERROR service.name:\"Learning Management Service\"", "limit": 10})
mcp_obs_logs_search({"query": "_time:10m severity:ERROR", "limit": 5})

MCP tools registered:

mcp_obs_logs_search
mcp_obs_logs_error_count
mcp_obs_traces_list
mcp_obs_traces_get


---

##Task 4A - Multi-step investigation
Question: What went wrong?

Agent response: Based on my investigation of the traces, here’s what went wrong:

Root Cause: Database Connection Failure

The Learning Management Service backend failed to connect to the PostgreSQL database.

Log Evidence:

Error: [Errno -2] Name or service not known
Service: Learning Management Service
Operation: db_query (SELECT from item table)
Trace Evidence:

Trace shows failure at: db_query span
Root span: request_started -> auth_success -> db_query (ERROR)
Tool calls used:

mcp_obs_logs_error_count
mcp_obs_logs_search
mcp_obs_traces_list

##Task 4B - Proactive health check
Cron job created:

Job ID: e3c266fd
Schedule: Every 120 seconds (2 minutes)

Proactive health report (while PostgreSQL was stopped):

Status: UNHEALTHY
1 ERROR in last 2 minutes
Service: Learning Management Service
Error: Database connection failure

##Task 4C - Bug fix and recovery

Root Cause - Planted Bug:

Location: backend/src/lms_backend/routers/items.py, function get_items()

Bug: The exception handler caught ALL exceptions and returned HTTP 404 “Items not found” instead of surfacing the real database error.

Fix:

Changed: Re-raise the exception instead of hiding it behind a 404.

Post-fix failure check:

After rebuild and with PostgreSQL stopped, the agent now reports the REAL error instead of “404 Items not found”.

**Agent response (after fix, PostgreSQL stopped):**
“The LMS backend is experiencing a database connection failure. The error shows: [Errno -2] Name or service not known. This indicates the PostgreSQL database is unreachable.”

Healthy follow-up:

After restarting PostgreSQL, the system reports healthy.

**Agent response (after PostgreSQL restarted):**
“The LMS backend is healthy. No errors found in the last 2 minutes. All 8 labs are available.”
