:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Flow</p>

Run a flow
==========

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Flow</dd></div>
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_flow_invoke</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Runs an active autolaunched flow by its API name with the given input variables and returns the flow's response, output variables included. Use it to trigger automation built in Flow Builder; List flows gives the names.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **invoke** in the **Flow** row, then click **Add to agent**.

The agent now sees ``salesforce_flow_invoke`` and calls it when a request needs it.

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
   * - ``flowApiName``
     - text
     - Yes
     - The flow's API name, for example Send\_Renewal\_Reminder; List flows returns it.
   * - ``inputs``
     - JSON object
     - No
     - The flow's input variables as name to value, for example {"recordId": "001XX000003DHPh"}; blank runs the flow with no inputs. Example: {"recordId": "001XX000003DHPh", "daysAhead": 30}.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Run a flow** every time a flow reaches it, without the agent deciding, use the :doc:`Run a flow App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/flow-invoke>`.

Other Flow tools
----------------

.. raw:: html

   <div class="tool-related"><a href="flow-getmany.html">List flows</a></div>
