:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Folder</p>

Create a mail folder
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Folder</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/outlook-mail.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates a mail folder at the top level of the mailbox and returns it with its id. Use the id with Message move to file emails into it.

Prerequisites
-------------

* **Connection:** Microsoft Graph connection. See :doc:`the Outlook Mail prerequisites <../outlook-mail>`.
* The connection's account must be allowed to change this data in Outlook Mail.

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
   * - ``displayName``
     - Folder name
     - text
     - Yes
     - The name of the new folder. Example: Vendor invoices.
   * - ``isHidden``
     - Hidden
     - true or false
     - No
     - true hides the folder from Outlook's folder list; it cannot be unhidden later.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Outlook Mail**, connect, and tick **create** in the **Folder** row. The model sees it as ``outlook_mail_folder_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Outlook Mail**, then **Create a mail folder**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-getmany.html">List mail folders</a><a href="folder-get.html">Get a mail folder</a><a href="folder-getmessages.html">List the emails in a folder</a><a href="folder-delete.html">Delete a mail folder</a></div>
