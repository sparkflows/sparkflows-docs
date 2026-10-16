:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › Drive</p>

List shared drives
==================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>Drive</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_drive_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the shared drives the account is a member of, with each drive's id and name. Pass a drive's id as driveId, with corpora drive, to List files or Search files to see what is inside it.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Drive** row, then click **Add to agent**.

The agent now sees ``google_drive_drive_getmany`` and calls it when a request needs it.

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
   * - ``limit``
     - whole number
     - No
     - How many shared drives at most, from 1 to 100; sent as Google's page size, since only one page is read. Example: 50. Default: 50.
   * - ``query``
     - text
     - No
     - A shared-drive query, for example name contains 'Finance'.
   * - ``fields``
     - list of text
     - No
     - Shared-drive fields to return, for example ["id", "name", "createdTime"]; blank returns Google's default set, which has id and name.

Need it on every run?
---------------------

To run **List shared drives** every time a flow reaches it, without the agent deciding, use the :doc:`List shared drives App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/drive-getmany>`.
