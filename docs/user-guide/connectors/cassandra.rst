Cassandra
==========

Fire Insights has a processor that allows you to connect with Cassandra. Apache Cassandra is a distributed NoSQL database designed for handling large amounts of data.

Setting Up a Connection to Cassandra Database
---------------------------------------
Follow the steps below to set up a connection to a Cassandra Database in Fire Insighs.


**Step 1 : Navigate to Connections**
++++++++++++++++++++++++++++++++++++++++++

* Login to **Fire Insights**.
* From the Dashboard, navigate to **Administration -> Global/Group Connections -> Add Connection**. The connection can be setup Globally at application level by choosing **Add Connection for All** option. It can also be setup locally for a Project.

 .. figure:: ../../_assets/tutorials/cassandra/cassandra-connection.png
    :alt: Connectors
    :width: 60%

**Step 2 : Configure the Connection**
++++++++++++++++++++++++++++++++++++++++
* Select connection category as **storage** and choose **Cassandra** from the dropdown in the connection type.
  
 .. figure:: ../../_assets/tutorials/cassandra/choose-cassandra.png
    :alt: Connectors
    :width: 60%


* Define the connection details as follows:

   * **Connection Type:** Select **Cassandra** from the dropdown menu.
   * **Connection Name:** Enter an Identifier for the connection.
   * **URL:** Enter the Cassandra database URL.
   * **Usename:** Enter the login username to access the Cassandra database.
   * **Password:** Enter the login password to access the Cassandra database.
   * **Title:** Enter a meaningful title for the Cassandra connection.
   * **Description:** Optionally, enter a description for the Cassandra connection.

.. note::  Make sure that the Cassandra host URL is accessible from the Fire Machine.

Read Cassandra
------------------
Read Cassandra connector can be used to **read data** from a **Cassandra Database Table**.

To read data from a Cassandra Database Table, follow the steps below:

**Step 1 : Configure the Connector**
+++++++++++++++++++++++++++++++++++++

To configure the connector, define the following connection details:

  .. figure:: ../../_assets/tutorials/cassandra/cassandra-read.png
     :alt: Connectors
     :width: 60%

 
* **Connection:** Select a **Cassandra Connection** from the dropdown menu.
* **Cassandra Table Name:** Enter a table name from the Cassandra Database whose data is intended to be fetched.
* **Cassandra Keyspace Name:** Enter Cassandra Keyspace name to which the table belongs. A Keyspace refers to a group of tables within a Cassandra database.
* Click the **Refresh Schema** button to fetch and load the selected table schema and then click on **Okay** button.

Save Cassandra
---------------------------------------
Save Cassandra connector can be used to **save data** to a **Cassandra Database Table**.

To save data to a Cassandra Database Table, follow the steps below:

**Step 1 : Configure the Connector**
++++++++++++++++++++++++++++++++++++++++++

To configure the connector, define the following connection details

 .. figure:: ../../_assets/tutorials/cassandra/cassandra-save.png
    :alt: Connectors
    :width: 60%

* **Connection:** Select a **Cassandra Connection** from the dropdown menu.
* **Cassandra Table Name:** Enter a table name from the Cassandra Database whose data is intended to be fetched.
* **Cassandra Keyspace Name:** Enter Cassandra Keyspace name to which the table belongs and click on **Okay** button. A Keyspace refers to a group of tables within a Cassandra database.
   
Workflow
------------------

A sample workflow to read and save data to Cassandra database table can be created as shown below. It uses the **Cassandra nodes** to read and write data.

 .. figure:: ../../_assets/tutorials/cassandra/cassandra-workflow.png
    :alt: Connectors
    :width: 60%

