:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › Permission</p>

List who has access
===================

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>Permission</dd></div>
     <div><dt>Type</dt><dd>Read</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_permission_getmany</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the permissions on a file or folder: who has access (a user, group, domain or anyone with the link) and with which role. Use it to check current access before sharing or after it.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **list** in the **Permission** row, then click **Add to agent**.

The agent now sees ``google_drive_permission_getmany`` and calls it when a request needs it.

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
   * - ``fileId``
     - text
     - Yes
     - The file or folder's id, from Search files or List files, never its name. Example: 1Q2w3E4r5T6y7U8i9O0pAsDfGhJkLzXcVb.
   * - ``limit``
     - whole number
     - No
     - How many permissions at most. Example: 50. Default: 50.
   * - ``fields``
     - list of text
     - No
     - Permission fields to return, for example ["id", "type", "role", "emailAddress", "displayName"]; blank returns Google's default set.
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Need it on every run?
---------------------

To run **List who has access** every time a flow reaches it, without the agent deciding, use the :doc:`List who has access App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/permission-getmany>`.

Other Permission tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="permission-create.html">Share a file</a></div>
