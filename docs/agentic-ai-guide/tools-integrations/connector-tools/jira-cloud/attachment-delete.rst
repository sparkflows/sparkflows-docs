:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Attachment</p>

Delete an attachment
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_attachment_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Permanently deletes one attachment from its issue. The attachment id comes from Attachment getMany.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.
* The account behind the connection must be allowed to change this data in Jira Cloud.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **delete** in the **Attachment** row, then click **Add to agent**.

The agent now sees ``jira_cloud_attachment_delete`` and calls it when a request needs it.

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
   * - ``attachmentId``
     - text
     - Yes
     - The id of the attachment, from Attachment getMany. Example: 10200.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Jira Cloud.

Need it on every run?
---------------------

To run **Delete an attachment** every time a flow reaches it, without the agent deciding, use the :doc:`Delete an attachment App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/attachment-delete>`.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-get.html">Get an attachment&#x27;s details</a><a href="attachment-getmany.html">List an issue&#x27;s attachments</a></div>
