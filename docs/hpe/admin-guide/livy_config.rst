Configure Livy Connection
=====

Sparkflows connects with Livy to submit the Spark and PySpark jobs of the workflow on the cluster powered by HPE UA. 

Follow the below steps to configure the Livy connection in Sparkflows:

.. Note :: Before you start setting up the Livy connection make sure of have uploaded the following files to maprfs as shown below

   ::

      1. hdfs:///apps/sparkflows/fire-spark_3.3.0-core-3.1.0-jar-with-dependencies.jar
      2. hdfs:///apps/sparkflows/workflowexecutecloud_livy.py
      3. hdfs:///apps/sparkflows/fire-python-dep.zip
      4. hdfs:///apps/sparkflows/fire-3.1.0-py3-none-any.whl

      Delta File Processing Jars:
      5. hdfs:///apps/sparkflows/delta-core_2.12-2.1.0.jar
      6. hdfs:///apps/sparkflows/delta-storage-2.1.0.jar


Step 1 : Livy Connection Configuration
----------------
#. After you’ve logged into Sparkflows, navigate to the **Administration** > **Global Connections** and then click on **Add Connection**. Select **Livy** as the **Compute Connection**. 

   .. figure:: ../../_assets/hpe/livy-add-connections.png
      :width: 60%
      :alt: Sparkflows On UA
   
#. Now, enter the **Livy URLs** and the **credentials**, that has been provided by the HPE UA Team.


   .. figure:: ../../_assets/hpe/livy-connection-general.png
      :width: 60%
      :alt: HPE UA Data sources

   .. figure:: ../../_assets/hpe/livy-connection-general-1.png
      :width: 60%
      :alt: HPE UA Data sources


Enter the **Livy** connection details in the **General** Tab as follows.

* **Connection Name** - A unique name for the connection
* **Postback URL** - Enter an URL that Sparkflows application can Call Back to. It should follow below format
	
	::

		https://<sparkflows-host>/messageFromSparkJob

* **Auth Type:** Select one of the Authentication Method that needs to be used from the options **None**, **Basic** and **OAUTH**. 

	#. **None:** Select None when no authentication is required.
	#. **Basic:** Select it when basic authentication is needed using username and password.
	#. **OAUTH:** Select it when more secure authentication is needed. It may involve third party application.

* **Username:** Enter the username for the Livy Connection
* **Password:** Enter the password of the Livy Connection
* **Title:** (Optional) Give a short title
* **Description:** (Optional) Give a brief description
* **URL:** Enter the Livy endpoint
* **Driver Class:** Enter the Driver Class Name to be used.

Step 2 : Upload JAR and Python Files
------

1. Click on next, and you’ll be presented with the below screen.

   .. figure:: ../../_assets/hpe/livy-connection-livytab-delta.png
      :width: 60%
      :alt: HPE UA Data sources

* **JAR:** Enter the path of the maprfs where the jar was uploaded
* **File:** Enter the path of the maprfs where workflowexecutecloud_livy.py has been stored
* **Pyspark Files:** Enter the path of the maprfs where all the python dependencies zip files are located and the whl package
* **Archive Files:** Enter the path of the maprfs where all the python dependencies zip files are located and the whl package

.. Note :: Both of the files need to be uploaded with the help from HPE & Sparkflows team.

2. Navigate to the bottom section of the screen.

   .. figure:: ../../_assets/hpe/livy-connection-livytabconf-delta.png
      :width: 60%
      :alt: HPE UA Data sources

**Conf:** Enter the below conf that will be passed as a spark configuration to the Livy REST API. 

	::

		spark.driver.extraJavaOptions:-Dcom.amazonaws.sdk.disableCertChecking=true,spark.executor.extraJavaOptions:-Dcom.amazonaws.sdk.disableCertChecking=true,spark.pyspark.python:/usr/local/bin/python3.8,spark.pyspark.driver.python:/usr/local/bin/python3.8


**Livy Log File S3 location:** Enter a location to be used to store EMR Livy Logs

3. Navigate to the **Hive** tab and add details as below

   .. figure:: ../../_assets/hpe/livy-connection-hivetab.png
      :width: 60%
      :alt: HPE UA Data sources

* **JDBC Driver:** Add the JDBC driver details to connect to the Hive Database
* **DB URL:** Add the Hive Data specific URL to access the database


4. Navigate to the **Yarn** tab and add details as below

   .. figure:: ../../_assets/hpe/livy-connection-yarntab.png
      :width: 60%
      :alt: HPE UA Data sources

* **Resource Manager URL:** Enter a Resource Manager URL
* **Node Manager URL:** Enter a Node Manager URL

5. Navigate to the **Lineage** tab and add details as below

   .. figure:: ../../_assets/hpe/livy-connection-lineagetab.png
      :width: 60%
      :alt: HPE UA Data sources

* **Connections:** Select a OpenLineage connetion from the dropdown.
* **Lineage Enable:** Select either True or False based on whether Lineage has been enabled.


Also, update the **Docker image** designated for executing PySpark jobs in the above configuration.

.. note:: you can configure **datafabric** path to Configure Apache Livy logs in Fire Insights.

   `Click Here <https://docs.sparkflows.io/en/latest/aws/admin-guide/emr/livy-logs.html>`_ to access detailed documentation on configuring Apache Livy logs in Fire Insights.

Step 3 : Handle SSL Bypass (If Necessary)
------------------

#. If you're connecting to an S3-compatible storage without a verified SSL certificate, include the following configuration to bypass SSL validation :
   ::

     spark.driver.extraJavaOptions:-Dcom.amazonaws.sdk.disableCertChecking=true,spark.executor.extraJavaOptions:-Dcom.amazonaws.sdk.disableCertChecking=true,spark.kubernetes.container.image:sparkflows/fire-hpe:3.1.0_13

Step 4 : Test and Save the Connection
------------------

#. Click on the YARN tab and then click on the **Test Connection** button, to validate the connection.
#. To ensure that the connection is working correctly, perform a connection test.
#. Once the test is successful, **Update** or **Save** the Connection.

   .. figure:: ../../_assets/hpe/livy-test-connection.png
      :width: 60%
      :alt: HPE UA Data sources

   Now, you can start submitting the workflows on the Livy cluster.
