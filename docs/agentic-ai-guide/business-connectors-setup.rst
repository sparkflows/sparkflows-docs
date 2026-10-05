:orphan:

Set Up Salesforce, Jira and Slack
=================================

Start with a read-only test in a sandbox, test project or training channel.
The account's permissions determine what the connection can access; selecting
an action in Sparkflows does not grant permission in the external app.

Salesforce connection setup
---------------------------

#. Ask the Salesforce administrator for an API-enabled integration identity
   with access to the objects and fields you need.
#. In Sparkflows, add a **Salesforce** connection. Choose the authentication
   method your administrator provides: **User Credential** or **OAuth**.
#. For User Credential, fill the domain, username, password and security token.
   For OAuth, provide the instance URL and access token. Do not enter a client
   secret into the access-token field.
#. Test and save. Add an App Action for **Salesforce → List accounts** with
   a small limit, then load the fields.
#. Confirm the records belong to the intended Salesforce organisation before
   using create, update, convert or delete operations.

For a custom object, use its API name, not just the display label. Use
**Describe custom object fields** to inspect the available fields. For an
upsert, agree an external-ID field with the Salesforce administrator first.

The OAuth form accepts an access token; do not assume that this form creates
an OAuth application or automatically renews a supplied token. Follow your
administrator's token lifecycle policy.

Jira Cloud
----------

#. Obtain a Jira Cloud account with access to your test project and an API
   token through your organisation's approved process.
#. Add a **Jira** connection. Enter **Jira Site URL**, **Email** and **API Token**.
   The site URL is the site's base address, not a single issue's URL.
#. Test and save. Use **Search issues** with a small JQL query for the test
   project and load the returned fields.
#. Open one returned issue and confirm its key, summary and status match.

To change an issue's status, first use **List an issue's transitions**. Use a
transition offered for that issue; a status name is not a transition ID.
When assigning an issue, use the account identifier returned by Jira's user
lookup rather than assuming an email address is accepted.

Slack connection setup
----------------------

The **Slack** App Action is available, but its connection picker does not
declare a dedicated Slack connection type in this build. This is not a reason
to choose an unrelated saved connection.

#. Have your workspace administrator configure a Slack app with the scopes
   required by the intended operation and install it in the workspace.
#. Ask the Sparkflows administrator to provision a compatible connection
   holding the Slack token. The connector accepts ``botToken``, ``accessToken``,
   ``token`` or ``password`` as the credential field; this is an administrator
   detail, not something to paste into an App Action's message text.
#. Invite the app to the training channel where required. Start with
   **List channels** or **Read channel history**, then load the fields.
#. Use the returned channel ID for subsequent actions. For a reply, also keep
   the parent message timestamp.

Some Slack operations require a user token rather than a bot token. A missing
scope or wrong token type cannot be repaired by changing the channel name.
If compatible credential provisioning is not available in your deployment,
stop at setup and ask your administrator; do not claim the connection is ready.

Before enabling writes
----------------------

Confirm the destination and the smallest permission set. Test with one record
and inspect the returned status. Repeating a send, create or comment operation
can create duplicates; use an upsert or an explicit duplicate check when the
business process must be safe to rerun.

Provider reference
------------------

* `Salesforce OAuth and API applications <https://developer.salesforce.com/docs/platform/api-rest/guide/intro-oauth-and-connected-apps.html>`_
* `Jira Cloud email and API-token authentication <https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/>`_
* `Slack OAuth installation <https://docs.slack.dev/authentication/installing-with-oauth/>`_
* `Slack scopes <https://docs.slack.dev/reference/scopes/>`_
