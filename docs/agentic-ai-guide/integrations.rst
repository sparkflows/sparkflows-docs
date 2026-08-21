Integrations & Enterprise Data
==============================

Enterprise agents are most useful when they can work with the systems where business data and actions already live. Sparkflows connects visual workflows to databases, warehouses, data lakes, files, cloud platforms, APIs, enterprise applications, AI services, and other supported systems.

Connections are reusable platform objects that allow workflows to access external systems without embedding credentials directly into workflow logic. Once configured, the same connection can support data engineering, analytics, ML, RAG, agent tools, and Agentic Apps as appropriate.

Integration documentation should cover both connectivity and usage: how to create and test a connection, authenticate securely, use the connected system in a workflow, and troubleshoot common issues.

Start here
----------

Start by creating the required connection and validating authentication before building the agent logic around it. Use the connector-specific documentation for required parameters, permissions, supported operations, and limitations.

For agents that take actions in external systems, distinguish read operations from write or transactional operations and apply additional permissions or approval where appropriate.

Documentation topics
--------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Topic
     - Description
   * - Integrations Overview
     - Understand how Sparkflows connects agents to enterprise systems.
   * - Create & Test a Connection
     - Configure reusable connections and validate connectivity.
   * - Manage Connections
     - Review and maintain configured connections.
   * - Databases & Warehouses
     - Connect supported relational databases and data warehouses.
   * - Data Lakes & Cloud Storage
     - Use enterprise lake and object storage platforms.
   * - Files & Documents
     - Use structured and unstructured files in workflows.
   * - REST APIs
     - Connect external systems using REST interfaces.
   * - Enterprise Applications
     - Integrate with supported business applications.
   * - Microsoft Ecosystem
     - Connect supported Azure, Fabric, Microsoft 365, and SharePoint services.
   * - Databricks & Snowflake
     - Use supported enterprise data platforms.
   * - AWS, Azure & GCP
     - Connect supported cloud data and AI services.
   * - LLM Providers
     - Connect supported model services.
   * - Vector Databases
     - Connect supported vector stores.
   * - Connection Authentication
     - Configure credentials, tokens, and other authentication.
   * - Troubleshooting
     - Diagnose connectivity, permissions, and credential issues.
