---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

You have access to LMS (Learning Management System) tools via MCP. Use these tools to fetch real-time course data.

## Available Tools

- lms_health - Check if the LMS backend is healthy
- lms_labs - Get list of available labs
- lms_pass_rates - Get pass rates for a specific lab
- lms_scores - Get scores for a specific lab
- lms_completion - Get completion data for a specific lab
- lms_groups - Get group data for a specific lab
- lms_timeline - Get timeline for a specific lab
- lms_top_learners - Get top learners for a specific lab

## Strategy

### When user asks about labs, scores, pass rates, completion, groups, timeline, or top learners:

1. If lab is not specified: First call lms_labs to get available labs, then ask the user to choose which lab they want information about.

2. If lab is specified: Call the appropriate tool directly with the lab parameter.

3. For lab selection: Use the lab id (e.g., lab-01, lab-02) as the parameter value. Display lab titles to the user for selection.

### Response formatting:

- Format percentages with one decimal place (e.g., 75.3 percent)
- Show counts as whole numbers
- Keep responses concise and focused on the requested data
- If backend is unhealthy, inform the user and suggest trying again later

### Example interactions:

User: Show me the scores
Action: Call lms_labs first, then ask which lab

User: Show scores for lab-01
Action: Call lms_scores with lab equals lab-01

User: What labs are available
Action: Call lms_labs and list them
