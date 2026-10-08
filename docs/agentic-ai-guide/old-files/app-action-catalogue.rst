:orphan:

App Action Lookup
==================

Use this page when you know the app and want to find an action. For your
first connection, start with :doc:`app-setup`; for a complete flow, use
:doc:`end-to-end-examples/index`.

This lookup follows the 17 App definitions marked available in the October 5,
2026 documentation baseline. Action names follow the current app picker;
database reads use **List rows**. The required inputs below are in addition to
the connection. Where a row says **See the action details**, the required
fields depend on the selected resource or operation; open **Details** in the
picker to see those fields and any optional target or filter before saving.

.. warning::

   **Write** and **Destructive** actions change data when run. They include
   sends, creates, deletions and permission changes. Availability does not
   mean your credential has the permissions or token type the provider requires.

.. contents:: Find your app
   :local:
   :depth: 1

Salesforce actions
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Account
     - Get an account
     - Read
     - Account Id
   * - Account
     - List accounts
     - Read
     - See the action details
   * - Account
     - Create an account
     - Write
     - Account name
   * - Account
     - Update an account
     - Write
     - Account Id
   * - Account
     - Create or update an account by external id
     - Write
     - External id field, Fields
   * - Account
     - Delete an account
     - Destructive
     - Account Id
   * - Account
     - Search accounts
     - Read
     - See the action details
   * - Account
     - Describe account fields
     - Read
     - See the action details
   * - Account
     - Count accounts
     - Read
     - See the action details
   * - Account
     - Add a note to an account
     - Write
     - Account Id, Note
   * - Contact
     - Get a contact
     - Read
     - Contact Id
   * - Contact
     - List contacts
     - Read
     - See the action details
   * - Contact
     - Create a contact
     - Write
     - Last name
   * - Contact
     - Update a contact
     - Write
     - Contact Id
   * - Contact
     - Create or update a contact by external id
     - Write
     - External id field, Fields
   * - Contact
     - Delete a contact
     - Destructive
     - Contact Id
   * - Contact
     - Describe contact fields
     - Read
     - See the action details
   * - Contact
     - Add a note to a contact
     - Write
     - Contact Id, Note
   * - Contact
     - Add a contact to a campaign
     - Write
     - Campaign Id, Contact Id
   * - Lead
     - Get a lead
     - Read
     - Lead Id
   * - Lead
     - List leads
     - Read
     - See the action details
   * - Lead
     - Create a lead
     - Write
     - Last name, Company
   * - Lead
     - Update a lead
     - Write
     - Lead Id
   * - Lead
     - Create or update a lead by external id
     - Write
     - External id field, Fields
   * - Lead
     - Delete a lead
     - Destructive
     - Lead Id
   * - Lead
     - Describe lead fields
     - Read
     - See the action details
   * - Lead
     - Add a note to a lead
     - Write
     - Lead Id, Note
   * - Lead
     - Add a lead to a campaign
     - Write
     - Campaign Id, Lead Id
   * - Lead
     - Convert a lead
     - Write
     - Lead Id
   * - Opportunity
     - Get an opportunity
     - Read
     - Opportunity Id
   * - Opportunity
     - List opportunities
     - Read
     - See the action details
   * - Opportunity
     - Create an opportunity
     - Write
     - Opportunity name, Stage, Close date
   * - Opportunity
     - Update an opportunity
     - Write
     - Opportunity Id
   * - Opportunity
     - Create or update an opportunity by external id
     - Write
     - External id field, Fields
   * - Opportunity
     - Delete an opportunity
     - Destructive
     - Opportunity Id
   * - Opportunity
     - Describe opportunity fields
     - Read
     - See the action details
   * - Opportunity
     - Add a note to an opportunity
     - Write
     - Opportunity Id, Note
   * - Case
     - Get a case
     - Read
     - Case Id
   * - Case
     - List cases
     - Read
     - See the action details
   * - Case
     - Create a case
     - Write
     - See the action details
   * - Case
     - Update a case
     - Write
     - Case Id
   * - Case
     - Delete a case
     - Destructive
     - Case Id
   * - Case
     - Describe case fields
     - Read
     - See the action details
   * - Case
     - Add a case comment
     - Write
     - Case Id, Comment
   * - Task
     - Get a task
     - Read
     - Task Id
   * - Task
     - List tasks
     - Read
     - See the action details
   * - Task
     - Create a task
     - Write
     - See the action details
   * - Task
     - Update a task
     - Write
     - Task Id
   * - Task
     - Delete a task
     - Destructive
     - Task Id
   * - Task
     - Describe task fields
     - Read
     - See the action details
   * - Event
     - Get an event
     - Read
     - Event Id
   * - Event
     - List events
     - Read
     - See the action details
   * - Event
     - Create an event
     - Write
     - Starts, Ends
   * - Event
     - Update an event
     - Write
     - Event Id
   * - Event
     - Delete an event
     - Destructive
     - Event Id
   * - Campaign
     - Get a campaign
     - Read
     - Campaign Id
   * - Campaign
     - List campaigns
     - Read
     - See the action details
   * - Campaign
     - Create a campaign
     - Write
     - Campaign name
   * - Campaign
     - Update a campaign
     - Write
     - Campaign Id
   * - Campaign
     - Delete a campaign
     - Destructive
     - Campaign Id
   * - Attachment
     - Get an attachment
     - Read
     - Attachment Id
   * - Attachment
     - List attachments
     - Read
     - See the action details
   * - Attachment
     - Create an attachment
     - Write
     - Attached to (Id), File name, Content (base64)
   * - Attachment
     - Update an attachment
     - Write
     - Attachment Id
   * - Attachment
     - Delete an attachment
     - Destructive
     - Attachment Id
   * - Custom Object
     - Get a custom object record
     - Read
     - Custom object, Record Id
   * - Custom Object
     - List custom object records
     - Read
     - Custom object
   * - Custom Object
     - Create a custom object record
     - Write
     - Custom object, Fields
   * - Custom Object
     - Update a custom object record
     - Write
     - Custom object, Id and fields
   * - Custom Object
     - Create or update a custom object record by external id
     - Write
     - Custom object, External id field, Fields
   * - Custom Object
     - Delete a custom object record
     - Destructive
     - Custom object, Record Id
   * - Custom Object
     - Describe custom object fields
     - Read
     - Custom object
   * - Custom Object
     - Count custom object records
     - Read
     - Custom object
   * - User
     - Get a user
     - Read
     - User Id
   * - User
     - List users
     - Read
     - See the action details
   * - User
     - Describe user fields
     - Read
     - See the action details
   * - Flow
     - List flows
     - Read
     - See the action details
   * - Flow
     - Run a flow
     - Write
     - Flow
   * - Search
     - Run a SOQL query
     - Read
     - SOQL query

Microsoft Teams actions
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Team
     - List teams
     - Read
     - See the action details
   * - Team
     - Get a team
     - Read
     - Team
   * - Team
     - List team members
     - Read
     - Team
   * - Channel
     - List channels
     - Read
     - Team
   * - Channel
     - Get a channel
     - Read
     - Team, Channel
   * - Channel
     - Create a channel
     - Write
     - Team, Name
   * - Channel
     - Delete a channel
     - Destructive
     - Team, Channel
   * - Channel
     - List channel members
     - Read
     - Team, Channel
   * - Channel Message
     - List channel messages
     - Read
     - Team, Channel
   * - Channel Message
     - Post a channel message
     - Write
     - Team, Channel, Message
   * - Channel Message
     - List replies to a post
     - Read
     - Team, Channel, Post
   * - Chat
     - List chats
     - Read
     - See the action details
   * - Chat
     - Get a chat
     - Read
     - Chat
   * - Chat
     - List chat messages
     - Read
     - Chat
   * - Chat
     - Send a chat message
     - Write
     - Chat, Message
   * - Meeting
     - Create an online meeting
     - Write
     - Organizer, Subject
   * - Meeting
     - Get an online meeting
     - Read
     - Organizer, Meeting

Slack actions
-------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Message
     - Send a message
     - Write
     - Channel, Message
   * - Message
     - Update a message
     - Write
     - Channel, Message ts, New text
   * - Message
     - Delete a message
     - Destructive
     - Channel, Message ts
   * - Message
     - Send an ephemeral message
     - Write
     - Channel, Shown to, Message
   * - Message
     - Get a message link
     - Read
     - Channel, Message ts
   * - Message
     - Search messages
     - Read
     - Search
   * - Channel
     - Get a channel
     - Read
     - Channel
   * - Channel
     - List channels
     - Read
     - See the action details
   * - Channel
     - Read channel history
     - Read
     - Channel
   * - Channel
     - Read thread replies
     - Read
     - Channel, Thread
   * - Channel
     - List channel members
     - Read
     - Channel
   * - Channel
     - Create a channel
     - Write
     - Name
   * - Channel
     - Invite members to a channel
     - Write
     - Channel, Users
   * - Channel
     - Remove a member from a channel
     - Destructive
     - Channel, User
   * - Channel
     - Join a channel
     - Write
     - Channel
   * - Channel
     - Leave a channel
     - Destructive
     - Channel
   * - Channel
     - Archive a channel
     - Destructive
     - Channel
   * - Channel
     - Unarchive a channel
     - Write
     - Channel
   * - Channel
     - Rename a channel
     - Write
     - Channel, New name
   * - Channel
     - Set a channel topic
     - Write
     - Channel, Topic
   * - Channel
     - Set a channel purpose
     - Write
     - Channel, Purpose
   * - User
     - Get a user
     - Read
     - User
   * - User
     - List users
     - Read
     - See the action details
   * - User
     - Get a user's profile
     - Read
     - See the action details
   * - User
     - Get a user's presence
     - Read
     - See the action details
   * - User
     - Find a user by email
     - Read
     - Email
   * - File
     - Get a file
     - Read
     - File
   * - File
     - List files
     - Read
     - See the action details
   * - File
     - Delete a file
     - Destructive
     - File
   * - Reaction
     - Add a reaction
     - Write
     - Channel, Message ts, Emoji
   * - Reaction
     - Get a message's reactions
     - Read
     - Channel, Message ts
   * - Reaction
     - Remove a reaction
     - Destructive
     - Channel, Message ts, Emoji
   * - User Group
     - List user groups
     - Read
     - See the action details
   * - User Group
     - Create a user group
     - Write
     - Name
   * - User Group
     - Update a user group
     - Write
     - User group
   * - User Group
     - Enable a user group
     - Write
     - User group
   * - User Group
     - Disable a user group
     - Destructive
     - User group

OneDrive actions
----------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - File
     - List files in a folder
     - Read
     - User
   * - File
     - Get a file or folder
     - Read
     - User, Item id
   * - File
     - Download a file and read its text
     - Read
     - User, Item id
   * - File
     - Upload a file
     - Write
     - User, File on the engine
   * - File
     - Delete a file or folder
     - Destructive
     - User, Item id
   * - File
     - Move or rename a file
     - Write
     - User, Item id
   * - File
     - Copy a file
     - Write
     - User, Item id
   * - File
     - Create a folder
     - Write
     - User, Folder name
   * - File
     - Create a sharing link
     - Write
     - User, Item id, Link type
   * - Drive
     - Get a user's OneDrive
     - Read
     - User
   * - Drive
     - List drives
     - Read
     - See the action details

Outlook Calendar actions
------------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Event
     - List events
     - Read
     - Mailbox
   * - Event
     - Get an event
     - Read
     - Mailbox, Event id
   * - Event
     - Create an event
     - Write
     - Mailbox, Starts, Ends
   * - Event
     - Update an event
     - Write
     - Mailbox, Event id
   * - Event
     - Delete an event
     - Destructive
     - Mailbox, Event id
   * - Event
     - Accept a meeting invitation
     - Write
     - Mailbox, Event id
   * - Event
     - Decline a meeting invitation
     - Write
     - Mailbox, Event id
   * - Event
     - Cancel a meeting
     - Destructive
     - Mailbox, Event id
   * - Calendar
     - List calendars
     - Read
     - Mailbox
   * - Calendar
     - Get a calendar
     - Read
     - Mailbox, Calendar id
   * - Free Time
     - Find meeting times
     - Read
     - Organizer
   * - Free Time
     - Get free/busy schedules
     - Read
     - Mailbox, People or rooms, From, To

Outlook Mail actions
--------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Message
     - List emails
     - Read
     - Mailbox
   * - Message
     - Get an email
     - Read
     - Mailbox, Message id
   * - Message
     - Search emails
     - Read
     - Mailbox, Search text
   * - Message
     - Send an email
     - Write
     - From mailbox, To
   * - Message
     - Reply to an email
     - Write
     - Mailbox, Message id, Reply text
   * - Message
     - Reply to everyone on an email
     - Write
     - Mailbox, Message id, Reply text
   * - Message
     - Forward an email
     - Write
     - Mailbox, Message id, Forward to
   * - Message
     - Update an email
     - Write
     - Mailbox, Message id
   * - Message
     - Move an email to a folder
     - Write
     - Mailbox, Message id, To folder
   * - Message
     - Delete an email
     - Destructive
     - Mailbox, Message id
   * - Message
     - Create a draft email
     - Write
     - Mailbox
   * - Folder
     - List mail folders
     - Read
     - Mailbox
   * - Folder
     - Get a mail folder
     - Read
     - Mailbox, Folder
   * - Folder
     - List the emails in a folder
     - Read
     - Mailbox, Folder
   * - Folder
     - Create a mail folder
     - Write
     - Mailbox, Folder name
   * - Folder
     - Delete a mail folder
     - Destructive
     - Mailbox, Folder id
   * - Attachment
     - Read email attachments
     - Read
     - Mailbox
   * - Attachment
     - Download email attachments
     - Read
     - Mailbox
   * - Attachment
     - Read one email attachment
     - Read
     - Mailbox, Message and attachment id

SharePoint actions
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Site
     - Get a site
     - Read
     - See the action details
   * - Site
     - List sites
     - Read
     - See the action details
   * - Site
     - Search sites
     - Read
     - Keywords
   * - Drive
     - List document libraries
     - Read
     - See the action details
   * - Drive
     - Get a document library
     - Read
     - Library id
   * - File
     - List files in a folder
     - Read
     - See the action details
   * - File
     - Get a file or folder
     - Read
     - File or folder
   * - File
     - Search files
     - Read
     - Search text
   * - File
     - Download a file and read its text
     - Read
     - File
   * - File
     - Upload a file
     - Write
     - File on the engine
   * - File
     - Create a folder
     - Write
     - Folder name
   * - File
     - Delete a file or folder
     - Destructive
     - File or folder
   * - File
     - Move or rename a file
     - Write
     - File or folder
   * - File
     - Copy a file
     - Write
     - File or folder
   * - List
     - List the site's lists
     - Read
     - See the action details
   * - List
     - Get a list
     - Read
     - List
   * - List
     - Create a list
     - Write
     - List name
   * - List
     - Delete a list
     - Destructive
     - List
   * - List Item
     - List items in a list
     - Read
     - List
   * - List Item
     - Get a list item
     - Read
     - List, Item id
   * - List Item
     - Create a list item
     - Write
     - List
   * - List Item
     - Update a list item
     - Write
     - List, Item id
   * - List Item
     - Delete a list item
     - Destructive
     - List, Item id
   * - Page
     - List site pages
     - Read
     - See the action details
   * - Page
     - Get a site page
     - Read
     - Page id

Gmail actions
-------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Message
     - List messages
     - Read
     - See the action details
   * - Message
     - Get a message
     - Read
     - Message
   * - Message
     - Search messages
     - Read
     - Search
   * - Message
     - Send an email
     - Write
     - To
   * - Message
     - Move a message to trash
     - Destructive
     - Message
   * - Message
     - Delete a message permanently
     - Destructive
     - Message
   * - Message
     - Change a message's labels
     - Write
     - Message
   * - Draft
     - List drafts
     - Read
     - See the action details
   * - Draft
     - Get a draft
     - Read
     - Draft
   * - Draft
     - Create a draft
     - Write
     - To
   * - Draft
     - Send a draft
     - Write
     - Draft
   * - Draft
     - Delete a draft
     - Destructive
     - Draft
   * - Label
     - List labels
     - Read
     - See the action details
   * - Label
     - Get a label with counts
     - Read
     - Label
   * - Label
     - Create a label
     - Write
     - Name
   * - Label
     - Update a label
     - Write
     - Label
   * - Label
     - Delete a label
     - Destructive
     - Label
   * - Attachment
     - Read attachments
     - Read
     - See the action details
   * - Attachment
     - Download attachments
     - Read
     - See the action details
   * - Thread
     - List threads
     - Read
     - See the action details
   * - Thread
     - Get a thread
     - Read
     - Thread
   * - Thread
     - Move a thread to trash
     - Destructive
     - Thread

Google Calendar actions
-----------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Event
     - Get an event
     - Read
     - Event id
   * - Event
     - List events
     - Read
     - See the action details
   * - Event
     - Create an event
     - Write
     - See the action details
   * - Event
     - Update an event
     - Write
     - Event id
   * - Event
     - Delete an event
     - Destructive
     - Event id
   * - Event
     - Quick add an event
     - Write
     - Event in one sentence
   * - Calendar
     - List calendars
     - Read
     - See the action details
   * - Calendar
     - Get a calendar
     - Read
     - See the action details
   * - Free Time
     - Find busy times
     - Read
     - From, Until

Google Docs actions
-------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Document
     - Get a document
     - Read
     - Document
   * - Document
     - Read a document as text
     - Read
     - Document
   * - Document
     - Create a document
     - Write
     - Title
   * - Document
     - Update a document
     - Write
     - Document

Google Drive actions
--------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - File
     - Get a file
     - Read
     - File id
   * - File
     - List files
     - Read
     - See the action details
   * - File
     - Search files
     - Read
     - See the action details
   * - File
     - Download a file
     - Read
     - File id
   * - File
     - Create a file or folder
     - Write
     - Name
   * - File
     - Update a file
     - Write
     - File id
   * - File
     - Copy a file
     - Write
     - File id, Name of the copy
   * - File
     - Delete a file permanently
     - Destructive
     - File id
   * - File
     - Upload a file
     - Write
     - File path
   * - Permission
     - List who has access
     - Read
     - File id
   * - Permission
     - Share a file
     - Write
     - File id, Role, Share with
   * - Drive
     - List shared drives
     - Read
     - See the action details

Google Sheets actions
---------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Row
     - Read rows
     - Read
     - Spreadsheet
   * - Row
     - Append rows
     - Write
     - Spreadsheet, Rows
   * - Row
     - Update rows
     - Write
     - Spreadsheet, Range, New values
   * - Row
     - Clear a range
     - Destructive
     - Spreadsheet, Range
   * - Spreadsheet
     - Get a spreadsheet
     - Read
     - Spreadsheet
   * - Spreadsheet
     - Create a spreadsheet
     - Write
     - Title
   * - Sheet
     - List tabs
     - Read
     - Spreadsheet
   * - Sheet
     - Add a tab
     - Write
     - Spreadsheet, Tab name
   * - Sheet
     - Delete a tab
     - Destructive
     - Spreadsheet, Tab id

Jira actions
------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Issue
     - Get an issue
     - Read
     - Issue key
   * - Issue
     - List issues
     - Read
     - See the action details
   * - Issue
     - Search issues
     - Read
     - See the action details
   * - Issue
     - Create an issue
     - Write
     - Project key, Issue type, Summary
   * - Issue
     - Update an issue
     - Write
     - Issue key
   * - Issue
     - Delete an issue
     - Destructive
     - Issue key
   * - Issue
     - Change an issue's status
     - Write
     - Issue key, Transition id
   * - Issue
     - List an issue's transitions
     - Read
     - Issue key
   * - Issue
     - Assign an issue
     - Write
     - Issue key, Assignee account id
   * - Issue
     - Get an issue's history
     - Read
     - Issue key
   * - Comment
     - Get a comment
     - Read
     - Issue key, Comment id
   * - Comment
     - List comments on an issue
     - Read
     - Issue key
   * - Comment
     - Add a comment
     - Write
     - Issue key, Comment
   * - Comment
     - Edit a comment
     - Write
     - Issue key, Comment id, Comment
   * - Comment
     - Delete a comment
     - Destructive
     - Issue key, Comment id
   * - Attachment
     - Get an attachment's details
     - Read
     - Attachment id
   * - Attachment
     - List an issue's attachments
     - Read
     - Issue key
   * - Attachment
     - Delete an attachment
     - Destructive
     - Attachment id
   * - Worklog
     - List an issue's worklogs
     - Read
     - Issue key
   * - Worklog
     - Log work on an issue
     - Write
     - Issue key, Time spent, Started
   * - Project
     - Get a project
     - Read
     - Project key or id
   * - Project
     - List projects
     - Read
     - See the action details
   * - Sprint
     - Get a sprint
     - Read
     - Sprint id
   * - Sprint
     - List a board's sprints
     - Read
     - Board id
   * - Board
     - List boards
     - Read
     - See the action details
   * - User
     - Get a user
     - Read
     - Account id
   * - User
     - List users
     - Read
     - See the action details
   * - User
     - Find users
     - Read
     - Name or email

MySQL actions
-------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Table
     - List rows
     - Read
     - Table
   * - Table
     - Get a row by key
     - Read
     - Table, Row key value
   * - Table
     - Count rows
     - Read
     - Table
   * - Table
     - Describe a table
     - Read
     - Table
   * - Table
     - Insert a row
     - Write
     - Table, Row
   * - Table
     - Update a row by key
     - Write
     - Table, Key column, Row
   * - Table
     - Insert or update a row
     - Write
     - Table, Key column, Row
   * - Table
     - Delete rows
     - Destructive
     - Table
   * - Table
     - List tables
     - Read
     - See the action details
   * - Table
     - List schemas
     - Read
     - See the action details
   * - Query
     - Run a SQL statement
     - SQL-dependent
     - SQL

PostgreSQL actions
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Table
     - List rows
     - Read
     - Table
   * - Table
     - Get a row by key
     - Read
     - Table, Row key value
   * - Table
     - Count rows
     - Read
     - Table
   * - Table
     - Describe a table
     - Read
     - Table
   * - Table
     - Insert a row
     - Write
     - Table, Row
   * - Table
     - Update a row by key
     - Write
     - Table, Key column, Row
   * - Table
     - Insert or update a row
     - Write
     - Table, Key column, Row
   * - Table
     - Delete rows
     - Destructive
     - Table
   * - Table
     - List tables
     - Read
     - See the action details
   * - Table
     - List schemas
     - Read
     - See the action details
   * - Query
     - Run a SQL statement
     - SQL-dependent
     - SQL

SQL Server actions
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Table
     - List rows
     - Read
     - Table
   * - Table
     - Get a row by key
     - Read
     - Table, Row key value
   * - Table
     - Count rows
     - Read
     - Table
   * - Table
     - Describe a table
     - Read
     - Table
   * - Table
     - Insert a row
     - Write
     - Table, Row
   * - Table
     - Update a row by key
     - Write
     - Table, Key column, Row
   * - Table
     - Insert or update a row
     - Write
     - Table, Key column, Row
   * - Table
     - Delete rows
     - Destructive
     - Table
   * - Table
     - List tables
     - Read
     - See the action details
   * - Table
     - List schemas
     - Read
     - See the action details
   * - Query
     - Run a SQL statement
     - SQL-dependent
     - SQL

Web Search actions
------------------

.. list-table::
   :header-rows: 1
   :widths: 18 33 17 32

   * - Resource
     - Action
     - Effect
     - Required inputs
   * - Request
     - Send a GET request
     - Read
     - URL
   * - Request
     - Send a POST request
     - Write
     - URL
   * - Request
     - Send a PUT request
     - Write
     - URL
   * - Request
     - Send a PATCH request
     - Write
     - URL
   * - Request
     - Send a DELETE request
     - Destructive
     - URL
   * - Page
     - Fetch a web page
     - Read
     - URL
   * - Page
     - List the links on a page
     - Read
     - URL
   * - Page
     - Check a URL
     - Read
     - URL
   * - Page
     - Crawl a site
     - Read
     - URL
   * - Search
     - Search the web
     - Read
     - Search text
   * - Search
     - Search the news
     - Read
     - Search text
   * - Search
     - Search images
     - Read
     - Search text
   * - Search
     - Search places
     - Read
     - Search text
   * - Feed
     - Read a feed
     - Read
     - URL

Not yet available
-----------------

The following catalogue entries are marked **Coming soon** in this baseline.
Do not build a tutorial that requires them until your installed version makes
them available:

Apache Airflow, Asana, Azure DevOps, Box, ClickUp, Confluence, Discord, Dynamics 365, Elasticsearch, Email (IMAP and SMTP), Freshservice, GitHub, GitLab, HubSpot, Intercom, Jenkins, Kubernetes, Linear, Mailchimp, Marketo, Monday.com, MongoDB, NetSuite, Notion, Object Storage, PagerDuty, Pipedrive, SQL Database, SendGrid, ServiceNow, Shopify, Stripe, Telegram, Trello, Twilio, Vector Store, Veeva Vault, Zendesk, Zoho CRM.
