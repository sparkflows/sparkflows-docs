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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>salesforce_attachment_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Creates an attachment (a file on a record) from the given fields and returns its new Id. The file content goes in body as base64, and parentId names the record it belongs to.

Before you start
----------------

* A Salesforce connection. See :doc:`how to set one up <../salesforce>`.
* The account behind the connection must be allowed to change this data in Salesforce.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Salesforce** under **Connectors** and connect your Salesforce connection.
#. Tick **create** in the **Attachment** row, then click **Add to agent**.

The agent now sees ``salesforce_attachment_create`` and calls it when a request needs it.

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
   * - ``parentId``
     - text
     - Yes
     - The Id of the record the file belongs to, such as an account, opportunity or case. Example: 006XX000002kLmN.
   * - ``name``
     - text
     - Yes
     - The file name with its extension. Example: signed-quote.pdf.
   * - ``body``
     - text
     - Yes
     - The file's content encoded as base64. Example: JVBERi0xLjcKJeLjz9MKNSAwIG9iago8PC9GaWx0ZXIvRmxhdGVEZWNvZGU+Pgo=.
   * - ``contentType``
     - text
     - No
     - The file's MIME type, for example application/pdf.
   * - ``description``
     - text
     - No
     - A note about the file. Example: Quote signed by the customer on 29 Sep..

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Salesforce.

Need it on every run?
---------------------

To run **Create an attachment** every time a flow reaches it, without the agent deciding, use the :doc:`Create an attachment App Action </agentic-ai-guide/tools-integrations/app-action-apps/salesforce/attachment-create>`.

Other Attachment tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="attachment-get.html">Get an attachment</a><a href="attachment-getmany.html">List attachments</a><a href="attachment-update.html">Update an attachment</a><a href="attachment-delete.html">Delete an attachment</a></div>
