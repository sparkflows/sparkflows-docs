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
     <div><dt>Tool name</dt><dd><code>outlook_mail_folder_get</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Returns one mail folder with its id, name, parent and unread, total and child folder counts. Use it to check a folder's counts, for example how many unread emails the inbox holds.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **get** in the **Folder** row, then click **Add to agent**.

The agent now sees ``outlook_mail_folder_get`` and calls it when a request needs it.

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
     - The folder id from Folder getMany, or a well-known name such as inbox, sentitems or archive.
   * - ``fields``
     - list of text
     - No
     - Graph mailFolder properties to return, such as displayName, unreadItemCount and totalItemCount; blank returns them all.

Need it on every run?
---------------------

To run **Get a mail folder** every time a flow reaches it, without the agent deciding, use the :doc:`Get a mail folder App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/folder-get>`.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-getmany.html">List mail folders</a><a href="folder-getmessages.html">List the emails in a folder</a><a href="folder-create.html">Create a mail folder</a><a href="folder-delete.html">Delete a mail folder</a></div>
