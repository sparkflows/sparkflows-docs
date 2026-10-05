:orphan:

Set Up Microsoft 365 Apps
=========================

Use **Microsoft Graph** for Outlook Mail, Outlook Calendar, OneDrive and
Microsoft Teams. SharePoint also accepts this connection type. Set up only
the permissions required by the action you intend to use.

Before connecting Microsoft apps
--------------------------------

Ask your Microsoft 365 administrator for an app registration, a test mailbox
or site, and the permissions for your intended action. The Sparkflows
Microsoft Graph form takes **Client Id**, **Client Secret** and **Tenant Id**.
This authenticates the application, not a person signed in to Outlook.

.. important::

   Not every Microsoft Graph operation supports application-only access.
   In particular, ordinary Teams message posting requires delegated user
   access. Do not assume that adding more application permissions will make
   **Post a channel message** or **Send a chat message** work.

1. Prepare the app registration
-------------------------------

#. In Microsoft Entra, open **App registrations** and use an app registration
   approved for this integration.
#. Record its application/client ID and directory/tenant ID.
#. Create or obtain a client secret through your organisation's approved
   process. Use its **value**, not the secret's identifier.
#. Under **API permissions**, add the Microsoft Graph application permissions
   for the actions you need. Have an administrator grant consent.

Use a restricted test identity and resource scope. The exact permission is
operation-specific: reading mail, sending mail, editing calendar events and
accessing site files are separate capabilities. Consult the permission table
for the Microsoft Graph operation rather than granting every permission in
the portal.

2. Save the connection in Sparkflows
------------------------------------

#. Open **Add Connection** and select **Microsoft Graph**.
#. Enter a descriptive **Connection Name**.
#. Fill **Client Id**, **Client Secret** and **Tenant Id** with the values from
   the app registration.
#. Test and save the connection. Keep its scope limited to the builders who
   need it.

For an existing **SharePoint** connection, use it only for SharePoint actions
that accept it. It is not a replacement for Microsoft Graph in Outlook or
OneDrive nodes.

3. Test the app you will use
----------------------------

.. list-table:: A small read for each app
   :header-rows: 1
   :widths: 24 31 45

   * - App
     - First action
     - What to provide and check
   * - Outlook Mail
     - **List emails**
     - A test mailbox and a small limit. Confirm the expected subjects.
   * - Outlook Calendar
     - **List events**
     - A test mailbox/calendar and a short date window. Check times and time zone.
   * - OneDrive
     - **Get a user's OneDrive**, then **List files in a folder**
     - The target user and the drive/folder returned by the preceding lookup.
   * - SharePoint
     - **Get a site**, then **List document libraries**
     - The site identifier; use the returned library/drive ID for file actions.
   * - Microsoft Teams
     - **List teams**, then **List channels**
     - The team ID returned by the first read. Confirm your app may read it.

Use **Load the fields** and inspect the sample. Copy identifiers from returned
records; a display name or a browser URL is not always the ID an action needs.

4. Add a write only when the read works
---------------------------------------

For Outlook, start with **Create a draft email** rather than **Send an email**.
For calendar examples, create events in a test calendar without attendees.
For files, use a dedicated training folder and a new filename.

Check ``result_status``, ``result_id`` and any ``result_error`` after the run.
Then open the destination app and verify the actual draft, event or file.

Teams message access
--------------------

The engine can use a delegated access token supplied on a connection, but the
standard Microsoft Graph wizard is an application-credential form. If your
deployment does not expose a supported way to provision delegated access,
ask an administrator before using Teams send actions. Use Outlook drafts for
the beginner tutorials instead. Do not use migration permissions as a shortcut
for normal message posting.

Microsoft reference
-------------------

* `Application-only authentication <https://learn.microsoft.com/en-us/graph/auth-v2-service>`_
* `Microsoft Graph permissions reference <https://learn.microsoft.com/en-us/graph/permissions-reference>`_
* `Send a channel message and its supported permissions <https://learn.microsoft.com/en-us/graph/api/channel-post-messages>`_
