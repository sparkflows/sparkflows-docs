:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../email-imap-smtp.html">Email (IMAP and SMTP)</a> › Folder</p>

List folders
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mail_tools.svg" alt="Email (IMAP and SMTP) logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Email (IMAP and SMTP)</dd></div>
     <div><dt>Resource</dt><dd>Folder</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>mail_tools_folder_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the mailbox's folders, one row per folder name, for use as folder in the other operations. Names are split on a / hierarchy separator.

Before you start
----------------

* A Email (IMAP and SMTP) connection. See :doc:`how to set one up <../email-imap-smtp>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Email, IMAP and SMTP** under **Connectors** and connect your Email (IMAP and SMTP) connection.
#. Tick **list** in the **Folder** row, then click **Add to agent**.

The agent now sees ``mail_tools_folder_getmany`` and calls it when a request needs it.

What the agent fills in
-----------------------

Nothing. The agent calls it as it is.
