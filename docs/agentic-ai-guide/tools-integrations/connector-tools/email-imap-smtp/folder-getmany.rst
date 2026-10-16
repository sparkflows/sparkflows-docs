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
     <div><dt>Available as</dt><dd>Agent tool only</dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the mailbox's folders, one row per folder name, for use as folder in the other operations. Names are split on a / hierarchy separator.

Prerequisites
-------------

* **Connection:** Email (IMAP and SMTP) connection. See :doc:`the Email (IMAP and SMTP) prerequisites <../email-imap-smtp>`.

Parameters
----------

This tool takes no parameters.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Email, IMAP and SMTP**, connect, and tick **list** in the **Folder** row. The model sees it as ``mail_tools_folder_getmany``.
