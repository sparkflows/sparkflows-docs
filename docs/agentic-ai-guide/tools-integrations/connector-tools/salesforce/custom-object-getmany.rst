:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Custom Object</p>

List custom object records
==========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Custom Object</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_custom_object_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Queries records of the custom object with an optional SOQL condition and returns up to limit rows. Without fields only the standard fields (Id, Name, owner and system dates) come back, so name the object's \_\_c fields to get its data. Use Run a SOQL query for aggregates or joins.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **list** in the **Custom Object** row, then click **Add to agent**.

The agent now sees ``salesforce_custom_object_getmany`` and calls it when a request needs it.

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
   * - ``where``
     - text
     - No
     - A SOQL condition without the word WHERE, such as Status\_\_c = 'Open' AND CreatedDate = LAST\_N\_DAYS:30, with text in single quotes and dates unquoted; it may end with ORDER BY but not LIMIT, and blank returns every record up to the limit.
   * - ``fields``
     - list of text
     - No
     - Field API names to return, such as ["Id", "Name", "Status\_\_c", "Amount\_\_c"]; blank returns only the standard fields, which leaves out every \_\_c field.
   * - ``limit``
     - whole number
     - No
     - How many records at most. Example: 50. Default: 50.

Need it on every run?
---------------------

To run **List custom object records** every time a flow reaches it, without the agent deciding, use the :doc:`List custom object records App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/custom-object-getmany>`.

Other Custom Object tools
-------------------------

.. raw:: html

   <div class="tool-related"><a href="custom-object-get.html">Get a custom object record</a><a href="custom-object-create.html">Create a custom object record</a><a href="custom-object-update.html">Update a custom object record</a><a href="custom-object-upsert.html">Create or update a custom object record by external id</a><a href="custom-object-delete.html">Delete a custom object record</a><a href="custom-object-describe.html">Describe custom object fields</a><a href="custom-object-count.html">Count custom object records</a></div>
