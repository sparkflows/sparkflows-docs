:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../email-imap-smtp.html">Email (IMAP and SMTP)</a> › Attachment</p>

List attachments
================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/mail_tools.svg" alt="Email (IMAP and SMTP) logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Email (IMAP and SMTP)</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>mail_tools_attachment_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the attachments of one message with filename, content type and size in bytes; the file contents are not returned. Reading them leaves the message unread if it was.

Before you start
----------------

* A Email (IMAP and SMTP) connection. See :doc:`how to set one up <../email-imap-smtp>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Email, IMAP and SMTP** under **Connectors** and connect your Email (IMAP and SMTP) connection.
#. Tick **list** in the **Attachment** row, then click **Add to agent**.

The agent now sees ``mail_tools_attachment_getmany`` and calls it when a request needs it.

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
   * - ``messageId``
     - text
     - Yes
     - The UID in the uid column of List messages or Search messages, which stays the same while the message stays in its folder. Example: 4821.
   * - ``folder``
     - text
     - No
     - The folder to work in, as List folders names it, for example INBOX or [Gmail]/All Mail; blank means INBOX.
