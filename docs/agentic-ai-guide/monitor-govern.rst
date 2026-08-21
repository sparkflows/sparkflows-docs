Monitor & Govern
=============

After deployment, monitor agent execution to understand how agents behave in production and to identify failures, unexpected actions, or performance issues. Production observability is especially important for agentic systems because a single request can involve multiple model calls, retrieval steps, tools, workflow branches, and business actions.

Sparkflows provides visibility across agent and workflow runs so teams can inspect execution stages, inputs and outputs, tool calls, retrieved context, errors, and other available operational information. This makes it easier to troubleshoot individual runs and understand patterns across production usage.

Governance operates alongside monitoring. Access controls, guardrails, human approvals, version history, and audit information help organizations control who can change or execute agents and maintain oversight over automated decisions and actions.

Start Here
-----------------

Start with Agent Runs and Workflow Runs to understand production activity. Use tracing and logs when investigating a specific execution. Review guardrail events and approval history for workflows with additional controls.

Monitoring should be configured as part of the production lifecycle rather than added after a problem occurs. The exact metrics available can vary by deployment and Sparkflows configuration, so reference pages should clearly distinguish platform-level, model-level, and infrastructure-level telemetry.

Documentation Topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Monitoring Overview
     - Understand production monitoring and governance for deployed agents.
   * - Agent & Workflow Runs
     - View current and historical executions.
   * - Execution Status & Duration
     - Monitor run status, duration, outcomes, and failures.
   * - Agent Tracing
     - Trace reasoning, retrieval, tools, and actions across execution.
   * - Tool & LLM Calls
     - Inspect model and tool interactions where exposed.
   * - RAG Tracing
     - Inspect retrieved context used by agents.
   * - Inputs & Outputs
     - Review workflow inputs, intermediate results, and generated outputs.
   * - Logs & Errors
     - Inspect execution logs and error details for troubleshooting.
   * - Usage Monitoring
     - Understand agent, workflow, model, API, or token usage where exposed.
   * - Performance Monitoring
     - Track execution and response performance.
   * - Guardrail Events
     - Review requests or outputs affected by configured controls.
   * - Human Approval History
     - Review approvals, rejections, and escalations.
   * - Audit Logs
     - Maintain relevant administrative and execution history.
   * - Versions & Deployment History
     - Track changes to agents, workflows, and deployments.
   * - Access Controls
     - Govern who can create, run, modify, and deploy agents.
   * - Troubleshooting
     - Diagnose monitoring, logging, and observability issues.
