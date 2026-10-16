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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the attachments of one message with filename, content type and size in bytes; the file contents are not returned. Reading them leaves the message unread if it was.

Prerequisites
-------------

* **Connection:** Email (IMAP and SMTP) connection. See :doc:`the Email (IMAP and SMTP) prerequisites <../email-imap-smtp>`.

Parameters
----------

As an agent tool, the model fills in each parameter unless you fix it under **Fixed settings**.

.. list-table::
   :header-rows: 1
   :widths: 22 14 12 52
   :class: tool-params

   * - Parameter
     - Type
     - Required
     - Description
   * - ``messageId``
     - text
     - Yes
     - The UID in the uid column of List messages or Search messages, which stays the same while the message stays in its folder. Example: 4821.
   * - ``folder``
     - text
     - No
     - The folder to work in, as List folders names it, for example INBOX or [Gmail]/All Mail; blank means INBOX.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Email, IMAP and SMTP**, connect, and tick **list** in the **Attachment** row. The model sees it as ``mail_tools_attachment_getmany``.
