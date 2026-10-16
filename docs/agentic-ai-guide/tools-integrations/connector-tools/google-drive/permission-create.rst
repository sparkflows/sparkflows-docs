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
     <div><dt>Type</dt><dd>Write · asks for approval</dd></div>
     <div><dt>Tool name</dt><dd><code>google_drive_permission_create</code></dd></div>
     </dl>
   </div>

.. container:: tutorial-intro

   Gives a user, a group, a whole domain or anyone with the link access to a file or folder with the given role, and returns the new permission. Users and groups are emailed a notification unless sendNotificationEmail is false.

Before you start
----------------

* A Google connection. See :doc:`how to set one up <../google-drive>`.
* The account behind the connection must be allowed to change this data in Google Drive.

Add it to your agent
--------------------

#. In Agent Studio, open the **Tools** group and click **Add tools**, or click **+ Tool** on an Agent Node.
#. Choose **Google Drive** under **Connectors** and connect your Google connection.
#. Tick **create** in the **Permission** row, then click **Add to agent**.

The agent now sees ``google_drive_permission_create`` and calls it when a request needs it.

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
   * - ``role``
     - text
     - Yes
     - The access to grant: reader, commenter or writer, or fileOrganizer or organizer on a shared drive. One of: reader, commenter, writer, fileOrganizer, organizer.
   * - ``type``
     - text
     - Yes
     - Who gets the access: user or group (give emailAddress), domain (give domain) or anyone with the link. One of: user, group, domain, anyone.
   * - ``emailAddress``
     - text
     - No
     - The person's or group's address, for type user or group. Example: asha.rao@company.com.
   * - ``domain``
     - text
     - No
     - The domain to share with, for type domain. Example: company.com.
   * - ``sendNotificationEmail``
     - true or false
     - No
     - false shares without emailing; blank emails users and groups.
   * - ``emailMessage``
     - text
     - No
     - A note added to the notification email. Example: Here is the Q3 report for your review..
   * - ``supportsAllDrives``
     - true or false
     - No
     - true lets the call reach files that live in shared drives as well as My Drive; keep it on. Default: True.

.. note::

   Each call waits for :doc:`your approval </agentic-ai-guide/safety-guardrails/human-in-the-loop>` before it changes anything in Google Drive.

Need it on every run?
---------------------

To run **Share a file** every time a flow reaches it, without the agent deciding, use the :doc:`Share a file App Action </agentic-ai-guide/tools-integrations/app-action-apps/google-drive/permission-create>`.

Other Permission tools
----------------------

.. raw:: html

   <div class="tool-related"><a href="permission-getmany.html">List who has access</a></div>
