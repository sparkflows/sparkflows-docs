:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../salesforce.html">Salesforce</a> › Attachment</p>

Create an attachment
====================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/salesforce.svg" alt="Salesforce logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Salesforce</dd></div>
     <div><dt>Resource</dt><dd>Attachment</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/salesforce.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an attachment (a file on a record) from the given fields and returns its new Id. The file content goes in body as base64, and parentId names the record it belongs to.

Prerequisites
-------------

* **Connection:** Salesforce connection. See :doc:`the Salesforce prerequisites <../salesforce>`.
* The connection's account must be allowed to change this data in Salesforce.

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
   * - ``parentId``
     - Attached to (Id)
     - text
     - Yes
     - The Id of the record the file belongs to, such as an account, opportunity or case. Example: 006XX000002kLmN.
   * - ``name``
     - File name
     - text
     - Yes
     - The file name with its extension. Example: signed-quote.pdf.
   * - ``body``
     - Content (base64)
     - text
     - Yes
     - The file's content encoded as base64. Example: JVBERi0xLjcKJeLjz9MKNSAwIG9iago8PC9GaWx0ZXIvRmxhdGVEZWNvZGU+Pgo=.
   * - ``contentType``
     - Content type
     - text
     - No
     - The file's MIME type, for example application/pdf.
   * - ``description``
     - Description
     - text
     - No
     - A note about the file. Example: Quote signed by the customer on 29 Sep..

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Salesforce**, connect, and tick **create** in the **Attachment** row. The model sees it as ``salesforce_attachment_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Salesforce**, then **Create an attachment**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-get.html">Get an attachment</a><a href="attachment-getmany.html">List attachments</a><a href="attachment-update.html">Update an attachment</a><a href="attachment-delete.html">Delete an attachment</a></div>
