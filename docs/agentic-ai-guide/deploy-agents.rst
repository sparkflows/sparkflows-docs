Deploy
=============

After an agent has been tested and evaluated, deploy it so it can be used by applications, business users, or automated processes. Sparkflows agentic workflows can be operationalized in different ways depending on how the capability needs to be consumed and triggered.

An agent may be exposed through an API, embedded within an Agentic App, executed on a schedule, triggered by an event, or invoked as part of a broader enterprise workflow. The same visual workflow can therefore move from development into an operational experience without rebuilding the core business logic in a separate application.

Production deployment should include more than publishing the workflow. Connections, credentials, runtime parameters, access controls, environment configuration, guardrails, monitoring, and human approvals should be reviewed before the agent is made available to production users.

Start Here
-----------------

Begin with Deployment Overview to choose the right delivery pattern. For user-facing experiences, consider an Agentic App. For system-to-system integration, use the available API deployment pattern. For recurring or process-driven automation, use scheduled or event-driven execution where supported.

After deployment, move to Monitor & Govern to track executions, investigate failures, review agent behavior, and maintain operational control.

Documentation Topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Deployment Overview
     - Choose the appropriate way to operationalize Sparkflows agents and workflows.
   * - Production Readiness
     - Review testing, security, connections, controls, and governance before deployment.
   * - Deploy an Agent
     - Move a tested agent into a production environment.
   * - Deploy a Workflow
     - Operationalize an agentic workflow for enterprise execution.
   * - Deploy as API
     - Expose an agent or workflow for application integration.
   * - Deploy as Agentic App
     - Publish a business-facing experience powered by agents.
   * - Scheduled Execution
     - Run agents and workflows automatically on a defined schedule.
   * - Event-Driven Execution
     - Trigger agent workflows from business or system events.
   * - Batch & Real-Time Execution
     - Run workflows across batches or interactive requests.
   * - Runtime Parameters
     - Configure values supplied to deployed workflows at runtime.
   * - Authentication & Secrets
     - Secure deployed endpoints, connections, and production credentials.
   * - Deployment Versions
     - Manage updates and versions of deployed agents and workflows.
   * - Manage Deployments
     - View and control production deployments.
   * - Deployment Environments
     - Run Sparkflows across supported cloud, hybrid, container, and on-premises environments.
   * - Troubleshooting
     - Diagnose deployment, connectivity, and runtime issues.
