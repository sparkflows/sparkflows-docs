:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Custom Object</p>

Describe custom object fields
=============================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Custom Object</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_custom_object_describe</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists every field on the custom object named in objectApiName, one row per field with its API name, label, type, length and whether it can be blank or updated. Use it to learn the object's \_\_c field names before a create, update or query.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **describe** in the **Custom Object** row, then click **Add to agent**.

The agent now sees ``salesforce_custom_object_describe`` and calls it when a request needs it.

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

Need it on every run?
---------------------

To run **Describe custom object fields** every time a flow reaches it, without the agent deciding, use the :doc:`Describe custom object fields App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/custom-object-describe>`.

Other Custom Object tools
-------------------------

.. raw:: html

   <div class="tool-related"><a href="custom-object-get.html">Get a custom object record</a><a href="custom-object-getmany.html">List custom object records</a><a href="custom-object-create.html">Create a custom object record</a><a href="custom-object-update.html">Update a custom object record</a><a href="custom-object-upsert.html">Create or update a custom object record by external id</a><a href="custom-object-delete.html">Delete a custom object record</a><a href="custom-object-count.html">Count custom object records</a></div>
