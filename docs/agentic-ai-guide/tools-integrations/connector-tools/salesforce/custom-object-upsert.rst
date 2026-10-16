:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Custom Object</p>

Create or update a custom object record by external id
======================================================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Custom Object</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_custom_object_upsert</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a record of the custom object, or updates the one whose external id field already holds the same value, so a repeated sync never makes duplicates; returns the external id. Use Create a custom object record or Update a custom object record when there is no external id.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **upsert** in the **Custom Object** row, then click **Add to agent**.

The agent now sees ``salesforce_custom_object_upsert`` and calls it when a request needs it.

What the agent fills in
-----------------------

The agent fills these in from each request. To pin a value so the agent cannot change it, set it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - What it means
   * - ``objectApiName``
     - text
     - Yes
     - The custom object's API name, ending in \_\_c, for example Invoice\_\_c.
   * - ``externalIdField``
     - text
     - Yes
     - The API name of a field on the object marked External ID, for example Invoice\_Number\_\_c; its value goes in fields.
   * - ``fields``
     - JSON object
     - Yes
     - The record's fields as API name to value, including the external id field with its value and, in case the record is new, its required fields, for example {"Invoice\_Number\_\_c": "INV-1001", "Amount\_\_c": 2500}. Example: {"Invoice\_Number\_\_c": "INV-1001", "Amount\_\_c": 2500, "Status\_\_c": "Open"}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create or update a custom object record by external id** every time a flow reaches it, without the agent deciding, use the :doc:`Create or update a custom object record by external id App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/custom-object-upsert>`.

Other Custom Object tools
-------------------------

.. raw:: html

   <div class="tool-related"><a href="custom-object-get.html">Get a custom object record</a><a href="custom-object-getmany.html">List custom object records</a><a href="custom-object-create.html">Create a custom object record</a><a href="custom-object-update.html">Update a custom object record</a><a href="custom-object-delete.html">Delete a custom object record</a><a href="custom-object-describe.html">Describe custom object fields</a><a href="custom-object-count.html">Count custom object records</a></div>
