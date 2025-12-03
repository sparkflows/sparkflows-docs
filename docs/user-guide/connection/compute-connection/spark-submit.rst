Spark Submit Connection
===============

Sparkflows enables you to create spark submit connection and use it to submit jobs/workflows. Connections can be at various levels:

  * **Global:** Everyone has access to these connections.
  * **Group:** Users belonging to the group have access to these connections.
  * **Project:** The owner of the project and the groups with which the project has been shared with have access to the project level connections.

Follow the steps below to create a Spark Submit Connection in Sparkflows:

Step 1 : Enable Spark Submit in Sparkflows
-----

* Login to **Sparkflows**.
* Navigate to **Administration -> Configurations -> CONNECTION**.
* Enable spark submit connection by setting the **value** of below parameter to **true** and save the configuration.

  ::

      connection.sparkCluster.enabled = true

  .. figure:: ../../../_assets/installation/connection/spark-submit_enabled.PNG
     :alt: livy
     :width: 60%

Step 2 : Add a Connection for Group
-----

* Once you save the above configuration, navigate to **Administration -> Global/Group Connections**, as shown below. 

  .. figure:: ../../../_assets/aws/livy/livy_7.png
     :alt: livy
     :width: 50%
   
* From the Connections page click on **Add Connections** button and choose **Add Connection For Group** from the dropdown. An 'Add Connection' dialog box opens up.
* Now, select connection category as **Compute** and connection type as **Spark Submit**, as shown below:

  .. figure:: ../../../_assets/installation/connection/spark-submit_compute.PNG
     :alt: connection
     :width: 60%
   
  
   
Step 3 : Add Additional Parameters as per your Environment
-----

* Once you have selected the connection type & groups, add the additonal connection parameters needed. For more details on the additional parameters refer the following images and tables:

For GENERAL Tab
+++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Connection name
     - Connection Name
     - Name of Connection
   * - Postback Url
     - Postback URL
     - Postback Url through which Spark Cluster sent result back to Sparkflows
   * - Title 
     - Title of Selected Connection
     - Title of Selected Connection  
   * - Description 
     - Connection Description 
     - Connection Description
        
.. figure:: ../../../_assets/installation/connection/spark-submit_general.PNG
   :alt: connection
   :width: 55%

For SPARK Tab
+++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Master
     - Spark-Submit run locally or on the cluster
     - possible value would be (local/yarn/spark)
   * - Deploy Mode
     - Whether to deploy spark driver on the worker node (cluster) or locally.
     - client/cluster  
   * - Context
     - Whether to use SQL Context or Hive Context.
     - SQLContext or HiveContext
   * - WaitAppCompletion
     - Whether spark-submit should wait for YARN App Completion
     - Whether spark-submit should wait for YARN App Completion  
   * - History Server URL 
     - Spark History Server URL
     - Spark History Server URL
   * - Executor Memory
     - Spark Executor Memory size to be used in spark-submit. Not used if it is empty.
     - Spark Executor Memory size to be used in spark-submit. Not used if it is empty.  
   * - Executors
     - Enable dynamic allocation instead on the spark cluster - spark.dynamicAllocation.enabled
     - Not used  
   * - Executor Cores
     - Number of Spark Executor Cores to be used in spark-submit. Not used if its value is less than or equal to 0
     - Not used if its value is less than or equal to 0  
   * - Command
     - Use spark2-submit with spark2, depending on your setup
     - by default it should take spark-submit
   * - Impersonate Users
     - Whether to impersonate the logged in user, or run everything as the user Fire is running with
     - update accordingly  
   * - Spark Submit jar
     - Absolute path of the Fire jar file to be used for submitting the spark jobs
     - Absolute path of the Fire jar file to be used for submitting the spark jobs
   * - Spark Submit zip
     - Absolute path of the Python zip file to be used for submitting the spark jobs
     - Absolute path of the Python zip file to be used for submitting the spark jobs
   * - Workflow Files Directory
     - Directory used for writing the workflow files. An HDFS location can also be specified. 
     - eg: hdfs:///tmp/fire/workflowsUse an HDFS location when running in YARN cluster mode  
     
     
     
.. figure:: ../../../_assets/installation/connection/spark-submit_spark.PNG
   :alt: connection
   :width: 70%     


For HDFS Tab
+++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - NameNode URI
     - NameNode URI 
     - NameNode URI for HDFS
   * - Home Dir
     - Home Dir under which various directories exist
     - Value  
 
.. figure:: ../../../_assets/installation/connection/spark-submit_hdfs.PNG
   :alt: connection
   :width: 60%

For HIVE Tab
+++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - JDBC Driver
     - JDBC Driver
     - JDBC Driver for Hive
   * - JDBC DB URL
     - JDBC DB URL
     - JDBC DB URL for Hive
     
.. figure:: ../../../_assets/installation/connection/spark-submit_hive.PNG
   :alt: connection
   :width: 60%    

For KERBEROS Tab
+++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Keytab
     - Keytab
     - Kerberos Keytab for Fire user   
   * - Principal
     - Principal 
     - Kerberos Principal for Fire user  
   * - REALM
     - REALM
     - Value   
   * - KDC
     - KDC
     - Value 
   * - HiveServer2 Principal
     - Kerberos Principal for HiveServer2
     - Value  
     
.. figure:: ../../../_assets/installation/connection/spark-submit_kerberos.PNG
   :alt: connection
   :width: 60%      

For YARN Tab
+++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Resource Manager URL
     - Resource Manager URL
     - Value  
     
.. figure:: ../../../_assets/installation/connection/spark-submit_yarn.PNG
   :alt: connection
   :width: 60%      

Step 4 : Save the Connection
-----
* Once you have updated the above parameters, click on  **Save** button to save the newly created spark submit connection.


.. Note:: Make sure that the above configured configuration is accessible from the Sparkflows web server URL. 
