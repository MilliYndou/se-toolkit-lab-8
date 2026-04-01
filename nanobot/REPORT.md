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
