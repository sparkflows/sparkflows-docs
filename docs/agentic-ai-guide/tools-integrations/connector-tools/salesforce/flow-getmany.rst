:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Flow</p>

List flows
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Flow</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_flow_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the active autolaunched flows that can be run through the API, one row per flow with its API name and label. Use it to find the name Run a flow needs.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **list** in the **Flow** row, then click **Add to agent**.

The agent now sees ``salesforce_flow_getmany`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.

Need it on every run?
---------------------

To run **List flows** every time a flow reaches it, without the agent deciding, use the :doc:`List flows App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/flow-getmany>`.

Other Flow tools
----------------

.. raw:: html

   <div class="tool-related"><a href="flow-invoke.html">Run a flow</a></div>
