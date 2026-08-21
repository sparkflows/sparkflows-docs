Tools & Actions
=============

Connect agents to APIs, applications, databases, workflows, and custom tools so they can retrieve information and take actions across enterprise systems.

Sparkflows tools provide a controlled interface between an agent and external capabilities. Tools can be used to retrieve data, invoke APIs, execute workflows, interact with applications, and perform business actions. This allows agents to move beyond generating responses and participate in end-to-end business processes.

Tools should be selected and configured based on the task the agent needs to perform. Parameters, authentication, permissions, and expected outputs should be validated before tools are made available to production agents.

Start Here
-----------------

Start by identifying the systems and actions the agent needs to access. Connect the required tools, configure their parameters and credentials, and test each tool independently before incorporating it into an agent workflow.

Review tool inputs and returned results during testing. For sensitive or irreversible actions, apply appropriate permissions, guardrails, or human approval before allowing the agent to execute the action.

Documentation Topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Tools Overview
     - Understand how tools connect agents to external capabilities.
   * - Tool Types
     - Understand the different types of tools available to agents.
   * - Add Tools to Agents
     - Connect tools to an agent and make them available during execution.
   * - API Tools
     - Connect agents to APIs and external services.
   * - Database Tools
     - Allow agents to access and work with database systems.
   * - Application Tools
     - Connect agents to enterprise applications.
   * - Workflow Tools
     - Invoke Sparkflows workflows from agents.
   * - Custom Tools
     - Extend agents with custom tool capabilities.
   * - Tool Parameters
     - Configure inputs and parameters required by tools.
   * - Tool Authentication
     - Configure authentication and credentials for tool access.
   * - Tool Permissions
     - Control which tools and actions agents can invoke.
   * - Tool Execution
     - Run tools and inspect their inputs and returned results.
   * - Actions
     - Configure actions that agents can perform across connected systems.
   * - Human Approval
     - Require review before selected actions are executed.
   * - Troubleshooting
     - Diagnose tool configuration, authentication, and execution issues.
