Security & Guardrails
=============

Security and guardrails control how agents access data, use tools, generate outputs, and execute actions. Agentic systems can interact with multiple enterprise resources, so permissions and controls should be applied across the entire workflow rather than only at the model layer.

Sparkflows enterprise controls can be used to govern access to the platform, workflows, data connections, applications, and deployment capabilities. Credentials and secrets used by tools or integrations should be managed securely and separated from prompts and user-visible workflow content.

Guardrails add runtime controls around agent behavior. Depending on the configured capability, they can validate inputs or outputs, restrict actions, protect sensitive information, require human approval, or enforce other organizational policies. Monitoring and audit information provide the visibility required to review how those controls operate in production.

Start here
-----------------

Start by applying least-privilege access to users, agents, data, and tools. Identify actions that are sensitive or irreversible and place explicit controls or human approval around them.

Before production deployment, test the configured guardrails and verify that unauthorized users, inputs, tools, and actions are handled as expected. Security documentation should always reflect the exact capabilities enabled in the customer's Sparkflows environment.

Documentation topics
-----------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Security Overview
     - Understand enterprise security for Sparkflows Agentic AI.
   * - Authentication & SSO
     - Control user and application authentication where configured.
   * - Role-Based Access Control
     - Manage permissions by user and role.
   * - Agent & Workflow Permissions
     - Control who can create, modify, run, and deploy.
   * - Data Access
     - Control enterprise data available to agents.
   * - Tool Permissions
     - Restrict which tools and actions agents can invoke.
   * - Credentials & Secrets
     - Secure credentials used by integrations.
   * - Environment Separation
     - Manage development, test, and production environments.
   * - Input Guardrails
     - Validate or restrict agent inputs.
   * - Output Guardrails
     - Validate generated responses before use.
   * - Action Guardrails
     - Control sensitive or irreversible agent actions.
   * - PII & Content Controls
     - Protect sensitive information where supported.
   * - Grounding Controls
     - Validate use of enterprise context where supported.
   * - Human Approval
     - Require authorization for selected actions.
   * - Auditability & Version History
     - Track execution and administrative changes.
   * - Troubleshooting
     - Diagnose access, permissions, and guardrail configuration issues.
