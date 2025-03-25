Cassandra DB - Connection Setup
=============

This document outlines the steps for setting up the connection to Cassandra Database. Follow the steps below:


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




































