:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Folder</p>

List mail folders
=================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Folder</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_mail_folder_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the top-level mail folders of a mailbox with their ids, names and unread and total counts; child folders are not included. Use it to find the folder id that Message getMany, Message search and Message move take.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **list** in the **Folder** row, then click **Add to agent**.

The agent now sees ``outlook_mail_folder_getmany`` and calls it when a request needs it.

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
   * - ``fields``
     - list of text
     - No
     - Graph mailFolder properties to return, such as id, displayName, unreadItemCount and totalItemCount; blank returns them all. Example: ["id", "displayName", "unreadItemCount"].
   * - ``limit``
     - whole number
     - No
     - How many folders at most. Default: 50.

Need it on every run?
---------------------

To run **List mail folders** every time a flow reaches it, without the agent deciding, use the :doc:`List mail folders App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/folder-getmany>`.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-get.html">Get a mail folder</a><a href="folder-getmessages.html">List the emails in a folder</a><a href="folder-create.html">Create a mail folder</a><a href="folder-delete.html">Delete a mail folder</a></div>
