HANA using JDBC
===========

Fire Insights enable to Read from and Write to SAP HANA using HANA JDBC Driver.

Below are the steps for Downloading and Configuring HDNA JDBC Driver and Reading and Writing to HANA in Fire Insights.

Download SAP HANA JDBC Driver from MVN Repository
-----

The SAP HANA JDBC Driver can be downloaded from : https://mvnrepository.com/artifact/com.sap.cloud.db.jdbc/ngdbc

Download SAP HANA JDBC Driver from SAP Service Marketplace
------------

  * Go to the SAP Service Marketplace: http://service.sap.com/connectors.
  * You will need SAP credentials to access the Service Marketplace.
  * Download the ngdbc.jar file and install it on the Fire Insights machine.
  
  
Configure HANA JDBC Driver in Fire Insights
-----------

Now JDBC Driver jar can be configured in Fire Insights to Read and Write to SAP HANA using JDBC Processors.

Below are steps to configure the driver in Fire Insights and Read and Write to HANA.

- Copy the ``ngdbc.jar`` to ``fire-user-lib & fire-server-lib`` and restart the Fire server.
- Login to Fire Insights application and Go inside project and workflow tab to create an example workflow with Read and Write to HANA using Read JDBC & Save JDBC Processors
