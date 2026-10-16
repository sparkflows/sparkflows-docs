:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../jira-cloud.html">Jira Cloud</a> › Attachment</p>

Get an attachment's details
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/jira_cloud.svg" alt="Jira Cloud logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Jira Cloud</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>jira_cloud_attachment_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns the details of one attachment: file name, size, MIME type, author, created time and the URL of its content; it does not download the file. The attachment id comes from Attachment getMany.

Before you start
----------------

* A Jira connection. See :doc:`how to set one up <../jira-cloud>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Jira Cloud** under **Connectors** and connect your Jira connection.
#. Tick **get** in the **Attachment** row, then click **Add to agent**.

The agent now sees ``jira_cloud_attachment_get`` and calls it when a request needs it.

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

Need it on every run?
---------------------

To run **Get an attachment's details** every time a flow reaches it, without the agent deciding, use the :doc:`Get an attachment's details App Action </agentic-ai-guide/tools-integrations/app-action-apps/jira-cloud/attachment-get>`.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-getmany.html">List an issue&#x27;s attachments</a><a href="attachment-delete.html">Delete an attachment</a></div>
