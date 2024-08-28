HANA using JDBC
===========

Fire Insights enables you to read from and write to SAP HANA through HANA JDBC Driver.

Below are the steps to download and configure HANA JDBC Driver and to read and write to HANA in Fire Insights.

Download SAP HANA JDBC Driver from MVN Repository
-----

The SAP HANA JDBC Driver can be downloaded from the link given below::

https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc

CData also provides JDBC drivers for reading and writing data to SAP::

https://www.cdata.com/drivers/sap/jdbc

Download SAP HANA JDBC Driver from SAP Service Marketplace
------------

The SAP JDBC Driver can also be downloaded using the steps below:

  * Go to the SAP Service Marketplace through the link provided here: http://service.sap.com/connectors
  * You will need SAP credentials to access the Service Marketplace.
  * Download the ``ngdbc.jar`` file and install it on the Fire Insights machine.
  
  
Configure HANA JDBC Driver in Fire Insights
-----------

Now, the JDBC Driver jar can be configured in Fire Insights to read and write to SAP HANA with the use of JDBC processors.

Below are the steps to configure the driver in Fire Insights in order to read and write to HANA:

- Copy the ``ngdbc.jar`` to ``fire-user-lib & fire-server-lib`` and restart the Fire server. Or if you wait for 60 minutes then the driver would be loaded automatically.
- In administration/global connection, use add a connection with storage type and select the JDBC type. Enter the connection details like URL, driver name, username, password etc for SAP HANA.
   More details on connection: https://docs.sparkflows.io/en/latest/installation/connection/storage-connection/index.html

Create workflow for reading/writing data to SAP HANA
-----------

- Login to the Fire Insights application and go inside the ``Project and Workflow tab`` to create a sample workflow for reading and writing to HANA through Read JDBC and Save JDBC Processors. Select the connection in Read and Save nodes.
