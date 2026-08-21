Developer & API
===============

Sparkflows is designed to support visual development while still allowing developers to extend the platform when a use case requires custom logic or integration. APIs, code processors, and custom components can complement visual workflows rather than replacing them.

Developers can use programmatic interfaces to trigger workflows, integrate deployed agents with external applications, build custom processors or tools, and add Python, SQL, or JavaScript logic where supported.

Developer documentation should clearly separate stable public APIs from internal implementation details and provide authentication, request/response, error handling, and working examples for supported extension points.

Start here
----------

Start with the API or extension point that matches the integration requirement. Validate authentication and a minimal request first, then connect it to the larger workflow or application.

For custom code, keep business logic modular and reusable so it can be governed and maintained alongside the visual workflow.

Documentation topics
--------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Developer Overview
     - Extend Sparkflows Agentic AI with APIs and code.
   * - REST API
     - Use supported Sparkflows APIs for programmatic integration.
   * - API Authentication
     - Authenticate applications calling Sparkflows APIs.
   * - Agent & Workflow APIs
     - Invoke deployed agents and workflows programmatically where exposed.
   * - Python
     - Extend workflows with Python.
   * - SQL
     - Use SQL for data operations and custom logic.
   * - JavaScript
     - Extend Agentic Apps and supported components.
   * - Custom Processors
     - Build reusable organization-specific processors.
   * - Custom Tools
     - Create agent tools for proprietary systems.
   * - External APIs
     - Integrate third-party and internal services.
   * - Webhooks & Events
     - Integrate workflows with events where supported.
   * - Request & Response Formats
     - Understand supported API payload structures.
   * - Error Handling
     - Handle API and runtime errors.
   * - Troubleshooting
     - Diagnose API, code, and extension issues.
