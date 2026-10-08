:orphan:

Set Up a Database App Action
============================

Connect **PostgreSQL**, **MySQL** or **SQL Server**, then prove a small read
before allowing the agent to write. Use a training database, not production.

No language model is required. These are :doc:`fixed App Actions
<app-actions>`: you choose the operation and the values it uses.

.. contents:: On this page
   :local:
   :depth: 1

Choose an App Action or a JDBC workflow node
--------------------------------------------

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - You are building…
     - Use
   * - A small read, lookup or record write in an agent flow
     - **App Action** → **PostgreSQL**, **MySQL** or **SQL Server**.
   * - A larger data-processing job with dataset reads and bulk saves
     - The database/JDBC nodes in a workflow. Configure and test that
       workflow with its execution engine, then use :doc:`workflows-as-tools`
       if an agent needs to invoke it.
   * - A connection to one of these databases using a JDBC URL
     - A matching **JDBC** connection may be selected by the App Action.
       The connection type does not turn the step into a Spark JDBC node.

The generic **SQL Database** App entry is marked **Coming soon** in this
build. Use the three available database apps; do not assume that a JDBC
connection makes every database vendor available in the App Action picker.
Workflow JDBC support is a separate capability and depends on its engine
and installed drivers.

1. Ask for a database connection
--------------------------------

Your database administrator supplies the host, port, database, username,
authentication details and required TLS settings. The database must be
reachable from the Sparkflows execution engine, not only from your laptop.

Start with a user allowed to read the test table. Grant insert or update
permissions separately if the tutorial needs them.

2. Create and test it
---------------------

#. Open **Add Connection** and choose **PostgreSQL**, **MySQL** or **SQL**
   for SQL Server. A **JDBC** connection is also accepted by these App Actions
   when it points to the corresponding database.
#. Fill the connection details requested by the wizard. Use the JDBC URL,
   driver and TLS settings supplied by the administrator when using JDBC.
#. Test and save the connection with a recognisable name.
#. In an App Action, select the matching database app and connection. Start
   with **List schemas** or **List tables**, then choose your test table.

**Database, schema and table are different settings.** The connection selects
the database. **Schema (optional)** selects a namespace inside it, when
needed—commonly ``public`` in PostgreSQL or ``dbo`` in SQL Server. In MySQL,
schema and database names refer to the same namespace. Put just the table
name in **Table** when a schema is entered separately; do not repeat the
schema in both places.

A connection test is not a test of table access, write permission or every
TLS option. Verify an actual small read from the execution engine. For
Polars-backed App Actions, JDBC-style connection details are translated to
native database drivers; not every Java JDBC URL option is supported. Ask
your administrator to verify the required TLS configuration rather than
disabling certificate checks to make a connection work.

3. Read five records
--------------------

#. Select **List rows** in the database action picker.
#. Set the schema/table, a simple filter if needed, and **Limit** to ``5``.
#. Click **Load the fields**. Check column names, data types and sample values.
#. Connect **Output** and run. Confirm the same rows in your database client.

.. figure:: ../_assets/agentic-ai-guide/app-actions/read-details.png
   :alt: PostgreSQL read settings and the returned table schema
   :width: 100%

   Load a small sample before mapping a later write.

4. Map a write deliberately
---------------------------

Use **Insert a row** for new records. Use **Insert or update a row** when
reruns should update an existing record. Choose a stable key, such as
``ticket_id``, and make sure the destination table has the appropriate key
constraint. The action does not design your table for you.

Use **Set Fields** before the write if incoming columns need to be renamed or
removed. Leaving **Fields to set** empty writes the arriving record fields;
do this only when they already match the destination.

After a one-record test, inspect ``result_status`` and read the row back.
Repeat the same input to check that your upsert does not create duplicates.

**Where does the key go?** For **Get a row by key**, put the key's value in
**Row key value**. For **Update a row by key** and **Insert or update a row**,
set **Key column** and include that column's value in the record you write.
Choosing the column alone does not supply the value.

For a dynamic lookup inside a one-record Loop, the value might be
``${4.fields.customer_id}``, where ``4`` is your Loop's actual node number.
Do not put that reference into **Table**, **Key column** or a SQL fragment.

.. figure:: ../_assets/agentic-ai-guide/app-actions/lookup-v5.png
   :alt: Current PostgreSQL Get a row by key action using the meeting Loop's customer_id as its Row key value

   The target table is fixed; the key value comes from the current meeting.
   This configuration screenshot is not a completed database read.

Every available database action
--------------------------------

The same eleven actions are offered by PostgreSQL, MySQL and SQL Server.
Start with the read actions; leave changes and SQL statements until the
small read succeeds.

Read and discover
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 23 40 37

   * - Action
     - Configure
     - Check the result
   * - **List schemas**
     - Select the connection. No table is needed.
     - A ``schema`` field names each visible schema. Visibility depends on
       the account's privileges.
   * - **List tables**
     - Optionally enter **Schema (optional)**.
     - Read the returned ``schema`` and ``table`` names before typing a target.
   * - **Describe a table**
     - Enter **Table** and its schema if needed.
     - Compare the columns and types with the fields you intend to write.
       Describing a table does not create or alter it.
   * - **List rows**
     - Enter **Table**, start with **Limit** ``5``, and optionally choose
       **Columns to return** and a trusted **Where** condition.
     - Check values as well as field names. A limited sample is not the
       whole table, and its order is not guaranteed without working ordering.
   * - **Get a row by key**
     - Enter **Table**, **Key column** and **Row key value**.
     - Confirm the returned record has that key. An empty result means no
       matching row; route it deliberately instead of inventing a customer.
   * - **Count rows**
     - Enter **Table** and, optionally, **Where**.
     - Read ``row_count``. This is a count of matching table rows, not the
       number of rows in a previous preview.

For predictable ordering before a Loop, add **Sort** after the read and
choose an explicit key. Sorting a five-row sample does not select the first
five records of the whole table. If selection depends on database ordering,
use a reviewed, read-only SQL query with ``ORDER BY`` and a database-specific
row limit, then verify its output.

Write selected records
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 23 40 37

   * - Action
     - Configure
     - Check before a retry
   * - **Insert a row**
     - Enter the table and map a record whose fields match its columns.
       Include required values; omit generated columns when appropriate.
     - A retry can create another row or hit a unique-key error. Look up the
       key before deciding whether to insert again.
   * - **Update a row by key**
     - Set **Key column**. Include the key and only the fields to change in
       **Fields to set**, or in the arriving record.
     - Read back the key and changed values. A successful request alone
       does not prove that the intended row existed or changed.
   * - **Insert or update a row**
     - Set **Key column** and include it in the mapped record. Create the
       destination's key constraint before using the action.
     - Repeat the same record and confirm one row remains. Serialize
       competing practice writes; do not treat an upsert as a guarantee
       against every concurrent race or duplicate key in incoming data.
   * - **Delete rows**
     - Prefer one known **Row key value** with its **Key column**. Use a
       trusted **Where** condition only when deletion of the matching set
       is explicitly intended.
     - Preview the target with a read first and require review for important
       data. A delete is not a harmless connection test.

**Map one practice record.** Suppose a training table contains
``customer_id``, ``company`` and ``status``, with ``customer_id`` as its key.
To update customer ``C-001`` without changing its name, choose **Update a
row by key**, set **Key column** to ``customer_id``, and map only:

.. code-block:: json

   {"customer_id": "C-001", "status": "reviewed"}

The names must match your actual table. This is a sample record, not a
command to create the table. In a flow, use **Set Fields** to build the same
shape from the original record and validated values. Leave out unrelated
model text and connector result fields.

Run a SQL statement
~~~~~~~~~~~~~~~~~~~~

**Run a SQL statement** takes **SQL** and an optional **Limit**. A query
returns records; a modifying statement changes the database. Use reviewed
SQL appropriate to that database's dialect and a connection with only the
permissions it needs.

For example, after your administrator creates the training table, this
literal query reads one known customer:

.. code-block:: sql

   SELECT customer_id, company, status
   FROM docs_tutorial_customers
   WHERE customer_id = 'C-001'

Use **Get a row by key** instead when the key comes from a user's message,
an event or a model. Its key value is bound as a parameter. **SQL** and
**Where** remain SQL text; a placeholder inside either is not a safe
parameter-binding interface. Never let a model supply unrestricted SQL to
a connection that can modify production data.

5. Verify the result and the second run
---------------------------------------

For writes, inspect ``result_status``, ``result_id`` and ``result_error``.
Then use a separate read or your database client to check the actual key,
values and row count. A generated id is not guaranteed for every database
operation, so keep your original business key as well.

Under **Advanced settings**, **If a row is rejected** chooses ``stop`` or
``continue``. Start with ``stop``. It stops on a rejection but does not undo
earlier writes in the flow. If you choose ``continue``, handle the failed
rows explicitly; do not send a success summary for the whole batch merely
because some rows succeeded.

Before enabling a schedule, try the same input twice in the training table.
Check that inserts, updates and upserts behave as intended, and that a
failure after the write does not cause a blind duplicate write on retry.

.. warning::

   **Run a SQL statement** is not inherently read-only. It can execute statements that
   change or delete data. Use a read-only account for exploration, and do not
   paste untrusted text into a SQL statement. Prefer the row actions for the
   introductory tutorials.

Common setup problems
---------------------

* **Connection times out:** check engine-to-database networking and the port.
* **Table not found:** check database, schema, spelling and account access.
* **Key error:** confirm the chosen key exists and has the required constraint.
* **Column/type error:** compare the incoming fields with **Describe a table**.

Continue with :doc:`end-to-end-examples/ticket-triage` for a read, classification
and upsert flow.
