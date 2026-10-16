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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-mail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the emails inside one mail folder, named by a well-known name or its id, as Microsoft Graph returns them: subject, sender, recipients, dates, read state and a preview. Use it when a request names one folder; Message getMany covers the same folders with readable columns, and the whole mailbox when no folder is given.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Mail prerequisites <../outlook-mail>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**, and in an App Action each one is a box on the **Details** step.

.. list-table::
   :header-rows: 1
   :widths: 18 17 11 12 42
   :class: tool-params

   * - Parameter
     - App Action input
     - Type
     - Required
     - Description
   * - ``mailbox``
     - Mailbox
     - text
     - Yes
     - The address of the mailbox. Example: asha.rao@contoso.com.
   * - ``folder``
     - Folder
     - text
     - Yes
     - The folder: a well-known name (inbox, sentitems, drafts, archive, deleteditems, junkemail) or a folder id from Folder getMany.
   * - ``filter``
     - Filter
     - text
     - No
     - An OData filter on message properties, such as isRead eq false or receivedDateTime ge 2026-09-01T00:00:00Z.
   * - ``orderBy``
     - Order by
     - text
     - No
     - A property and a direction, such as receivedDateTime desc; with a filter, the property sorted on must appear in the filter as well.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph message properties to return, such as subject, from, receivedDateTime, bodyPreview and isRead; blank returns them all. Example: ["subject", "from", "receivedDateTime"].
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many emails at most. Default: 50.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **getMessages** in the **Folder** row. The model sees it as ``outlook_mail_folder_getmessages``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **List the emails in a folder**, and fill in the inputs above. It runs every time the flow reaches it.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-getmany.html">List mail folders</a><a href="folder-get.html">Get a mail folder</a><a href="folder-create.html">Create a mail folder</a><a href="folder-delete.html">Delete a mail folder</a></div>
