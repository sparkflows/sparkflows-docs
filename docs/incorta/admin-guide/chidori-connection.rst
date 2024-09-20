Configure Chidori Connection
=====================

Sparkflows allows you to create a Chidori connection for submitting jobs and workflows. Connections can be created at various levels:

  * **Global**: Everyone has access to these connections.
  * **Group**: Users belonging to the group have access to these connections.
  * **Project**: The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This document provides steps to create a Chidori Connection in Fire Insights.

Step 1 : Enable Chidori in Sparkflows
++++++++++

#. Login to **Sparkflows application**
#. Navigate to **Administration -> Configurations -> Connection** and enable **Chidori connection** by setting the below parameter:

::

    connection.chidori.enabled	 : true

.. figure:: ../../_assets/incorta/chidori_1.png
   :alt: chidori
   :width: 60%

Step 2 : Navigate to Add Connections
+++++

Once you save the above Configuration, navigate to **Administration -> Global Connections -> Add Connections** as shown below:

.. figure:: ../../_assets/aws/livy/administration.png
   :alt: livy
   :width: 60%
   
Step 3 : Add Connection for Group
++++++++++++

#. Navigate to **Administration -> Global Connections -> Add Connections -> Add Connection For Group** 
#. On the pop up window, select **Compute Connection** and other parameters as shown below:

   .. figure:: ../../_assets/aws/livy/add_connection.PNG
      :alt: livy
      :width: 60%
   
   .. figure:: ../../_assets/incorta/chidori_2.png
      :alt: chidori
      :width: 60%
   
Step 4 : Add Additional Parameters 
++++++

Once you have selected  the connection type & groups, add the additional connection parameters as per your environment. For more details refer the following tables and images:

For GENERAL Tab
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Connection name
     - Connection Name
     - Name of Connection
   * - Token 
     - Token 
     - Token used for Chidori
   * - Postback Url
     - Postback Url
     - Postback Url through which Chidori sent result back to Fire Insights
   * - Title 
     - Title of Selected Connection
     - Title of Selected Connection  
   * - Description 
     - Connection Description 
     - Connection Description
   * - Url
     - Url for selected Connection type
     - Add URL for Chidori Connection
   * - Driver Class
     - Driver Class for selected Connection type 
     - It Comes with default value  
     
.. figure:: ../../_assets/incorta/chidori_3.png
   :alt: chidori
   :width: 60%

For CHIDORI Tab
++++++
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Jars
     - Jars to be used in Chidori session
     - Jars path located in Chidori Cluster
   * - Pyspark Files
     - Pyspark Files to be used in emr livy session
     - Pyspark file located in Chidori Cluster 
   * - Spark Conf
     - Spark Conf
     - Spark Conf used while Job Submission
   * - Log File location
     - Location to be used to store Chidori Log
     - Update the path ie File system accessible  
     
.. figure:: ../../_assets/incorta/chidori_4.png
   :alt: chidori
   :width: 60%

For MV Tab
++++++
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - HostName 
     - HostName 
     - HostName 
   * - Token
     - Token
     - Token 
        
.. figure:: ../../_assets/incorta/chidori_5.png
   :alt: chidori
   :width: 60%


.. Note::  Ensure that the **fire-spark_x.y.z-core-x.y.z-jar-with-dependencies.jar** and **workflowexecutecloud.py** files are uploaded to an S3 bucket or the Incorta cluster path. These files must be accessible from the Sparkflows webserver UI. The required jar files can be found in the Sparkflows binary by untarring **fire-x.y.z/fire-core-lib** and **fire-x.y.z/dist/**.

           For PySpark integration, install the Fire Python Wheel and the necessary Python packages on the Chidori cluster. You can download them from the following links:

           * Get the Fire Python wheel file from this link:  `Fire Python Wheel File Download Link <https://sparkflows-release.s3.amazonaws.com/fire/incorta/spark_3.3.1/fire-3.1.0-py3-none-any.whl>`_
           * Get the Fire Python wheel file from any of the following links: 

             * `Fire Python dependency 1 Download Link <https://sparkflows-release.s3.amazonaws.com/fire/incorta/spark_3.3.1/python_dependency/requirements-0-100.txt>`_

             * `Fire Python dependency 2 Download Link <https://sparkflows-release.s3.amazonaws.com/fire/incorta/spark_3.3.1/python_dependency/requirements-101-150.txt>`_

             * `Fire Python dependency 3 Download Link <https://sparkflows-release.s3.amazonaws.com/fire/incorta/spark_3.3.1/python_dependency/requirements-151-end.txt>`_
