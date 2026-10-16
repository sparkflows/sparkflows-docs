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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the active autolaunched flows that can be run through the API, one row per flow with its API name and label. Use it to find the name Run a flow needs.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.

Parameters
----------

This tool takes no parameters.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **list** in the **Flow** row. The model sees it as ``salesforce_flow_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **List flows**, and fill in the inputs above. It runs every time the flow reaches it.

Other Flow tools
----------------

.. raw:: html

   <div class="tool-related"><a href="flow-invoke.html">Run a flow</a></div>
