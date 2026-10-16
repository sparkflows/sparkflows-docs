:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../outlook-mail.html">Outlook Mail</a> › Folder</p>

Delete a mail folder
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/outlook_mail.svg" alt="Outlook Mail logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Outlook Mail</dd></div>
     <div><dt>Resource</dt><dd>Folder</dd></div>
     <div><dt>Type</dt><dd>Delete · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>outlook_mail_folder_delete</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Deletes a mail folder together with the emails in it. Well-known folders such as the Inbox cannot be deleted.

Before you start
----------------

* A Microsoft Graph connection. See :doc:`how to set one up <../outlook-mail>`.
* The account behind the connection must be allowed to change this data in Outlook Mail.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Outlook Mail** under **Connectors** and connect your Microsoft Graph connection.
#. Tick **delete** in the **Folder** row, then click **Add to agent**.

The agent now sees ``outlook_mail_folder_delete`` and calls it when a request needs it.

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
     - The id of the folder to delete, from Folder getMany. Example: AAMkAGI2TG93AAAuAAAAAAAiQ8W967B7TKBjgx9rVEURAQAiIsqMbYjsT5e-T7KzowPTAAAAAAEMAAA=.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Outlook Mail.

Need it on every run?
---------------------

To run **Delete a mail folder** every time a flow reaches it, without the agent deciding, use the :doc:`Delete a mail folder App Action </agentic-ai-guide/tools-integrations/app-action-apps/outlook-mail/folder-delete>`.

Other Folder tools
------------------

.. raw:: html

   <div class="tool-related"><a href="folder-getmany.html">List mail folders</a><a href="folder-get.html">Get a mail folder</a><a href="folder-getmessages.html">List the emails in a folder</a><a href="folder-create.html">Create a mail folder</a></div>
