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
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-drive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Lists the shared drives the account is a member of, with each drive's id and name. Pass a drive's id as driveId, with corpora drive, to List files or Search files to see what is inside it.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Drive prerequisites <../google-drive>`.

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
   * - ``limit``
     - Limit
     - whole number
     - No
     - How many shared drives at most, from 1 to 100; sent as Google's page size, since only one page is read. Example: 50. Default: 50.
   * - ``query``
     - Drive name filter
     - text
     - No
     - A shared-drive query, for example name contains 'Finance'.
   * - ``fields``
     - Fields to return
     - list of text
     - No
     - Shared-drive fields to return, for example ["id", "name", "createdTime"]; blank returns Google's default set, which has id and name.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Drive**, connect, and tick **list** in the **Drive** row. The model sees it as ``google_drive_drive_getmany``.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Drive**, then **List shared drives**, and fill in the inputs above. It runs every time the flow reaches it.
