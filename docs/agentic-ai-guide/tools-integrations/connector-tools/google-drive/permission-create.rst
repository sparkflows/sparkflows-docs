:orphan:

.. rst-class:: agentic-tutorial

.. raw:: html

   <p class="tool-crumbs"><a href="../index.html">Connector Tools</a> › <a href="../google-drive.html">Google Drive</a> › Permission</p>

Share a file
============

.. raw:: html

   <div class="tool-hero">
     <img class="tool-hero-logo" src="../../../../_static/img/tools/google_drive.svg" alt="Google Drive logo">
     <dl class="tool-facts">
     <div><dt>Connector</dt><dd>Google Drive</dd></div>
     <div><dt>Resource</dt><dd>Permission</dd></div>
     <div><dt>Type</dt><dd>Write · approval-gated</dd></div>
     <div><dt>Available as</dt><dd>Agent tool · <a href="../../app-action-apps/google-drive.html">App Action</a></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Gives a user, a group, a whole domain or anyone with the link access to a file or folder with the given role, and returns the new permission. Users and groups are emailed a notification unless sendNotificationEmail is false.

Prerequisites
-------------

* **Connection:** Google connection. See :doc:`the Google Drive prerequisites <../google-drive>`.
* The connection's account must be allowed to change this data in Google Drive.

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
   * - ``fileId``
     - File id
     - text
     - Yes
     - The file or folder's id, from Search files or List files, never its name. Example: 1Q2w3E4r5T6y7U8i9O0pAsDfGhJkLzXcVb.
   * - ``role``
     - Role
     - text
     - Yes
     - The access to grant: reader, commenter or writer, or fileOrganizer or organizer on a shared drive. One of: reader, commenter, writer, fileOrganizer, organizer.
   * - ``type``
     - Share with
     - text
     - Yes
     - Who gets the access: user or group (give emailAddress), domain (give domain) or anyone with the link. One of: user, group, domain, anyone.
   * - ``emailAddress``
     - Email address
     - text
     - No
     - The person's or group's address, for type user or group. Example: asha.rao@company.com.
   * - ``domain``
     - Domain
     - text
     - No
     - The domain to share with, for type domain. Example: company.com.
   * - ``sendNotificationEmail``
     - Email a notification
     - true or false
     - No
     - false shares without emailing; blank emails users and groups.
   * - ``emailMessage``
     - Message
     - text
     - No
     - A note added to the notification email. Example: Here is the Q3 report for your review..
   * - ``supportsAllDrives``
     - Reach shared drives
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

Use it
------

**As an agent tool.** Open the Agent Node's **+ Tool**, choose **Google Drive**, connect, and tick **create** in the **Permission** row. The model sees it as ``google_drive_permission_create``. Each call waits for human approval before it changes anything.

**As an App Action.** Drop **App Action** on the canvas, pick **Google Drive**, then **Share a file**, and fill in the inputs above. It runs every time the flow reaches it. A canvas run skips it unless **Write when run from the canvas** is on.

Other Permission tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="permission-getmany.html">List who has access</a></div>
