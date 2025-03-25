Cassandra
==========

Fire Insights has a processor that allows you to connect with Cassandra. Apache Cassandra is a distributed NoSQL database designed for handling large amounts of data. 

Before creating a workflow using the Read and Save Cassandra nodes, you must first set up a connection to the Cassandra database in Fire Insights. To learn how to create this connection, click on  :ref:`Create Cassandra Connection<Cassandra Connection>`.

This document will cover the following key aspects:

* Read Cassandra Node Configuration
* Save Cassandra Node Configuration
* Workflow Creation




Read Cassandra
------------------
This node can be used to **read data** from a **Cassandra Database Table**.



Node Configuration
+++++++++++++++++++++++++++++++++++++

To configure the Read Cassandra node, define the following connection details:

  .. figure:: ../../_assets/tutorials/cassandra/cassandra-read.png
     :alt: Connectors
     :width: 60%

 
* ``CONNECTION`` : Select a **Cassandra Connection** from the dropdown menu.
* ``CASSANDRA TABLE NAME`` : Enter a table name from the Cassandra Database whose data is intended to be fetched.
* ``CASSANDRA KEYSPACE NAME`` : Enter Cassandra Keyspace name to which the table belongs. A Keyspace refers to a group of tables within a Cassandra database.
* Click the **Refresh Schema** button to fetch and load the selected table schema and then click on **Okay** button.

Save Cassandra
--------------------------------------
This node can be used to **save data** to a **Cassandra Database Table**.


Node Configuration
++++++++++++++++++++++++++++++++++++++++++

To configure the Save Cassandra node, define the following connection details

 .. figure:: ../../_assets/tutorials/cassandra/cassandra-save.png
    :alt: Connectors
    :width: 60%

* ``CONNECTION`` : Select a **Cassandra Connection** from the dropdown menu.
* ``CASSANDRA TABLE NAME`` : Enter a table name from the Cassandra Database whose data is intended to be fetched.
* ``CASSANDRA KEYSPACE NAME`` : Enter Cassandra Keyspace name to which the table belongs and click on **Okay** button. A Keyspace refers to a group of tables within a Cassandra database.
   
Workflow
------------------

A sample workflow to read and save data to Cassandra database table can be created as shown below. It uses the **Cassandra nodes** to read and write data.

 .. figure:: ../../_assets/tutorials/cassandra/cassandra-workflow.png
    :alt: Connectors
    :width: 60%

