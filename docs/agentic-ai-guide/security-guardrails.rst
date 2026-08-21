Security & Guardrails
=====================

Security and guardrails control how agents access data, use tools, generate outputs, and execute actions. Agentic systems can interact with multiple enterprise resources, so permissions and controls should be applied across the entire workflow rather than only at the model layer.

Sparkflows enterprise controls can be used to govern access to the platform, workflows, data connections, applications, and deployment capabilities. Credentials and secrets used by tools or integrations should be managed securely and separated from prompts and user-visible workflow content.

Guardrails add runtime controls around agent behavior. Depending on the configured capability, they can validate inputs or outputs, restrict actions, protect sensitive information, require human approval, or enforce other organizational policies. Monitoring and audit information provide the visibility required to review how those controls operate in production.

Steps to Secure & Govern an Agent
---------------------------------

Secure and govern an agent by working through the following steps.

Step 1: Configure Authentication & Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control user and application authentication and apply appropriate access permissions.

Step 2: Apply Role-Based Access Control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manage permissions by user and role.

Step 3: Configure Agent & Workflow Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control who can create, modify, run, and deploy agents and workflows.

Step 4: Control Data Access
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Control the enterprise data available to agents.

Step 5: Configure Tool Permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Restrict which tools and actions agents can invoke.

Step 6: Secure Credentials & Secrets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Secure credentials used by tools, integrations, and other connected resources.

Step 7: Separate Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Manage development, test, and production environments where supported.

Step 8: Configure Input Guardrails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate or restrict inputs provided to agents.

Step 9: Configure Output Guardrails
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate generated responses before they are used.

Step 10: Control Agent Actions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply controls to sensitive or irreversible actions.

Step 11: Protect Sensitive Information
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Apply PII and content controls where supported.

Step 12: Configure Grounding Controls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate the use of enterprise context where supported.

Step 13: Add Human Approval
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Require authorization for selected actions.

Step 14: Maintain Auditability & Version History
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Track execution and administrative changes to maintain oversight.

Next Step
---------

Once security controls and guardrails have been configured and tested, continue to Monitor & Govern to review their operation and maintain production oversight.
