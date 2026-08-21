Developer & API
===============

Sparkflows is designed to support visual development while still allowing developers to extend the platform when a use case requires custom logic or integration. APIs, code processors, and custom components can complement visual workflows rather than replacing them.

Developers can use programmatic interfaces to trigger workflows, integrate deployed agents with external applications, build custom processors or tools, and add Python, SQL, or JavaScript logic where supported.

Developer documentation should clearly separate stable public APIs from internal implementation details and provide authentication, request/response, error handling, and working examples for supported extension points.

Steps to Extend Sparkflows
--------------------------

Extend Sparkflows using APIs, code, and custom components by working through the following steps.

Step 1: Identify the Extension Requirement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Identify the integration, custom logic, or development requirement that cannot be addressed through the visual workflow alone.

Step 2: Select the Extension Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Choose the appropriate API, code processor, custom processor, custom tool, or other supported extension point.

Step 3: Configure API Authentication
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure the authentication required for applications calling Sparkflows APIs.

Step 4: Invoke Agents & Workflows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use supported APIs to invoke deployed agents and workflows programmatically where exposed.

Step 5: Add Custom Code
~~~~~~~~~~~~~~~~~~~~~~~

Extend workflows with Python, SQL, or JavaScript where supported.

Step 6: Build Custom Processors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create reusable organization-specific processors for custom workflow logic.

Step 7: Create Custom Tools
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create agent tools for proprietary systems and capabilities.

Step 8: Integrate External APIs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Connect third-party and internal services through supported interfaces.

Step 9: Configure Webhooks & Events
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Integrate workflows with events where supported.

Step 10: Define Request & Response Handling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use supported API payload structures and handle request and response data appropriately.

Step 11: Handle Errors
~~~~~~~~~~~~~~~~~~~~~

Implement appropriate handling for API and runtime errors.

Step 12: Test & Troubleshoot
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Validate the extension with minimal requests or workflows and diagnose API, code, and extension issues.

Next Step
---------

Once the required APIs, code, or custom components have been tested, integrate them into the broader agent or workflow and continue to Evaluate to validate the resulting behavior.
