:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Folder</p>

Get a mail folder
=================

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

   Returns one mail folder with its id, name, parent and unread, total and child folder counts. Use it to check a folder's counts, for example how many unread emails the inbox holds.

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
     - The folder id from Folder getMany, or a well-known name such as inbox, sentitems or archive.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Graph mailFolder properties to return, such as displayName, unreadItemCount and totalItemCount; blank returns them all.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **get** in the **Folder** row. The model sees it as ``outlook_mail_folder_get``.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **Get a mail folder**, and fill in the inputs above. It runs every time the flow reaches it.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-getmany.html">List mail folders</a><a href="folder-getmessages.html">List the emails in a folder</a><a href="folder-create.html">Create a mail folder</a><a href="folder-delete.html">Delete a mail folder</a></div>
