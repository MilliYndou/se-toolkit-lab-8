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
