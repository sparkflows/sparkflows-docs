EMR LIVY CONNECTION
--------------

Sparkflows enables you to create Apache Livy Connection and use it to submit Jobs/Workflows.

Connections can be at various levels:

  * Global : Everyone has access to these connections
  * Group : Users belonging to the group have access to these connections
  * Project : The owner of the project and the groups with which the Project has been shared with have access to the Project level connections

Below are the steps to create a Livy Connection in Sparkflows.

1. Enable Livy in Sparkflows

Login to ``Sparkflows`` application -> ``Administration`` -> ``Configurations`` -> ``Connection`` -> and enable Livy connection by setting the below parameter:

::

    connection.livy.enabled : true

.. figure:: ../../_assets/aws/livy/livy_configuration.PNG
   :alt: livy
   :width: 60%

2. Create Global Connections

Once you save the above Configuration, navigate to ``Administration`` -> ``Global Connections`` -> ``Add Connections`` as shown below:

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/administration.PNG
   :alt: livy
   :width: 60%
   
3. Add Connection For Group

Navigate to ``Administration`` -> ``Global Connections`` -> ``Add Connections`` -> ``Add Connection For Group`` which pop up a new windows -> Select ``Compute Connection`` and other parameters as shown below:

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_connection.PNG
   :alt: livy
   :width: 60%
   
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_livy_connection.PNG
   :alt: livy
   :width: 60%   
   
4. Additional parameter as per your environment

Once you Selected Connection Type & Groups, add the additonal Connection parameters needed.

For GENERAL tab :

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
     - Postback Url
     - Postback Url through which Livy sent result back to Fire Insights
   * - Title 
     - Title of Selected Connection
     - Title of Selected Connection  
   * - Description 
     - Connection Description 
     - Connection Description
   * - Url
     - Url for selected Connection type
     - Add URL for Livy Connection
   * - Driver Class
     - Driver Class for selected Connection type 
     - It Comes with default value  
     
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_general.PNG
   :alt: livy
   :width: 60%

For LIVY tab :

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Jars
     - Jars to be used in emr livy session
     - Jars path located in S3 Location
   * - Pyspark Files
     - Pyspark Files to be used in emr livy session
     - Pyspark file located in S3 Location  
   * - Files
     - Files to be used in emr livy session
     - Any Files if needed
   * - Archives Files
     - Archives Files to be used in emr livy session
     - Value  
   * - Driver Memory 
     - Driver Memory to be used in emr livy session
     - Driver Memory if any specific memory you need to pass
   * - Driver Cores
     - Driver Cores to be used in emr livy session
     - Driver Cores if any specific Cores you need to pass  
   * - Executor Memory
     - Executor Memory to be used in emr livy session
     - Executor Memory if any specific Executor Memory you need to pass  
   * - Executor Cores
     - Executor Cores to be used in emr livy session
     - Executor Cores if any specific Executor Cores you need to pass  
   * - Num Executors
     - Num Executors to be used in emr livy session
     - Num Executors if any specific Num Executors you need to pass  
     
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_livy.PNG
   :alt: livy
   :width: 70%     

.. Note:: Make sure to upload ``fire-spark_x.y.z-core-x.y.z-jar-with-dependencies.jar`` to S3 bucket and is accessible from Saprkflows webserver UI. This jar is available in Sparkflows binary. Untar the binary to find it inside ``fire-x.y.z/fire-core-lib``. 

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/livy_jar.PNG
   :alt: livy
   :width: 70% 


For HDFS tab :

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
 
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_hdfs.PNG
   :alt: livy
   :width: 60%

For HIVE tab :

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
     
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_hive.PNG
   :alt: livy
   :width: 60%    

For KERBEROS tab :

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
     
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_kerberos.PNG
   :alt: livy
   :width: 60%      

For YARN tab :

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Resource Manager URL
     - Resource Manager URL
     - Value  
     
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_yarn.PNG
   :alt: livy
   :width: 60%      

5. Test Connection and Save

Once you have updated the above parameters, click on ``Test Connection``, if the Connection is Successful, ``Save`` the connection.

.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_test_connection.PNG
   :alt: livy
   :width: 60%
   
.. figure:: https://github.com/sparkflows/sparkflows-docs/blob/master/docs/_assets/aws/livy/add_list.PNG
   :alt: livy
   :width: 60%   

Documentation
+++++

Reference guide : https://docs.sparkflows.io/en/latest/aws/emr-livy/index.html

.. Note:: Make sure that Apache Livy URL will be accessible from Sparkflows webserver URL.
