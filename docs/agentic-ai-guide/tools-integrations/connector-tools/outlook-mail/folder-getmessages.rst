:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Folder</p>

List the emails in a folder
===========================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Folder</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_mail_folder_getmessages</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the emails inside one mail folder, named by a well-known name or its id, as Microsoft Graph returns them: subject, sender, recipients, dates, read state and a preview. Use it when a request names one folder; Message getMany covers the same folders with readable columns, and the whole mailbox when no folder is given.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **getMessages** in the **Folder** row, then click **Add to agent**.

The agent now sees ``outlook_mail_folder_getmessages`` and calls it when a request needs it.

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
   * - ``mailbox``
     - text
     - Yes
     - The address of the mailbox. Example: asha.rao@contoso.com.
   * - ``folder``
     - text
     - Yes
     - The folder: a well-known name (inbox, sentitems, drafts, archive, deleteditems, junkemail) or a folder id from Folder getMany.
   * - ``filter``
     - text
     - No
     - An OData filter on message properties, such as isRead eq false or receivedDateTime ge 2026-09-01T00:00:00Z.
   * - ``orderBy``
     - text
     - No
     - A property and a direction, such as receivedDateTime desc; with a filter, the property sorted on must appear in the filter as well.
   * - ``fields``
     - list of text
     - No
     - Graph message properties to return, such as subject, from, receivedDateTime, bodyPreview and isRead; blank returns them all. Example: ["subject", "from", "receivedDateTime"].
   * - ``limit``
     - whole number
     - No
     - How many emails at most. Default: 50.

Need it on every run?
---------------------

To run **List the emails in a folder** every time a flow reaches it, without the agent deciding, use the :doc:`List the emails in a folder App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/folder-getmessages>`.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-getmany.html">List mail folders</a><a href="folder-get.html">Get a mail folder</a><a href="folder-create.html">Create a mail folder</a><a href="folder-delete.html">Delete a mail folder</a></div>
