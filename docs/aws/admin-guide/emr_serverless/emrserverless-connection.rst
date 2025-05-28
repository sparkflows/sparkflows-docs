Amazon EMR Serverless Connection
--------------

Sparkflows enables you to create "Amazon EMR Serverless Connection" and use it to submit Spark Job. Connections can be at various levels:

  * Global  : Everyone has access to these connections.
  * Group   : Users belonging to the group have access to these connections.
  * Project : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This document guides on how to create a "Amazon EMR Serverless Connection" in Fire Insights. Follow the steps below:

Step 1 : Enable Amazon EMR Serverless Connection in Sparkflows
===========

* Login to **Fire Insights**.
* Go to **Administration -> Configurations -> CONNECTION**.
* Enable Amazon EMR Serverless by setting the **value** of below parameter to **true** and save the configuration.

  ::

    connection.emr.serverless.enabled = true

  .. figure:: ../../../_assets/aws/emrserverless/emrserverless_8.png
         :alt: emrserverless
         :width: 60%

Step 2 : Navigate to Connections Page
===========

* Once you save the above configuration, navigate to **Administration -> Global/Group Connections** as shown below. You will land on Connections page.

  .. figure:: ../../../_assets/aws/livy/admin-page.png
     :alt: livy
     :width: 60%
   
Step 3 : Add Connection for a Group
========

* On Connections page, click on **Add Connection** button.
* Select **Add Connection For Group** from the dropdown, as shown below. An 'Add Connection' pop up window appears.

  .. figure:: ../../../_assets/aws/mwaa/mwaa-addconnection.png
     :alt: mwaa
     :width: 60%

* Select connection category as **Compute** and connection type as **EMR Serverless**, as shown below.

  .. figure:: ../../../_assets/aws/emrserverless/emrserverless_9.png
         :alt: emrserverless
         :width: 60%




Step 4 : Configure Other Connection Parameters as per your environment
======

* Once you have selected the connection type & groups, add the additional connection parameters needed. For more details refer the following tables and images:

For GENERAL tab
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
   * - Postback Url
     - Postback Url
     - Postback Url through which Amazon EMR Serverless sent result back to Fire Insights
   * - Title 
     - Title of Selected Connection
     - Title of Selected Connection  
   * - Description 
     - Connection Description 
     - Connection Description

.. figure:: ../../../_assets/aws/emrserverless/emrserverless_10.png
         :alt: emrserverless
         :width: 60%


For EMR SERVERLESS tab
++++++
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Output S3Bucket
     - Auth Type
     - The bucket to use for storage and logs
   * - Execution Role ARN
     - Execution Role ARN
     - The Execution Role ARN while submitting Spark job
   * - Main Class
     - Main Class to Exceute
     - fire.execute.WorkflowExecuteFromAPI
   * - Jar File
     - The Entrypoint for Spark Job
     - The Entrypoint for Spark Job
   * - Release Label
     - The EMR Release associated with application
     - EMR 6.9.0
   * - Application Type
     - The Type of Application to start
     - SPARK
   * - Spark Config
     - The Spark config parameter
     - The Spark config parameter
   * - Jars
     - Environment Name
     - Environment Name of aws mwaa resources
   * - Files 
     - Environment Name
     - Environment Name of aws mwaa resources
   * - Custom EMR Image URI 
     - Environment Name
     - Environment Name of aws mwaa resources

.. figure:: ../../../_assets/aws/emrserverless/emrserverless_11.png
         :alt: emrserverless
         :width: 60%

.. figure:: ../../../_assets/aws/emrserverless/emrserverless_12.png
         :alt: emrserverless
         :width: 60%


For NETWORK tab
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Subnet Ids
     - Subnet Ids
     - Subnet Ids for accessing Amazon EMR Serverless
   * - Security Group Ids
     - Security Group Ids
     - Security Group Ids for accessing Amazon EMR Serverless

.. figure:: ../../../_assets/aws/emrserverless/emrserverless_13.png
         :alt: emrserverless
         :width: 60%


.. note:: Make sure that **Subnet Ids and Security Group Ids** created in the previous steps are used here and that they allow access from the ecs or ec2 instance where the Fire Insights application is running.

Step 5 : Submit Job on Amazon EMR Serverless
=========

* Now that the Amazon EMR Serverless Connection ready, you can submit the Spark job and view response back to UI and validate same from AWS Console.

  .. figure:: ../../../_assets/aws/emrserverless/emrserverless_14.png
         :alt: emrserverless
         :width: 60%

  .. figure:: ../../../_assets/aws/emrserverless/emrserverless_15.png
         :alt: emrserverless
         :width: 60%

  .. figure:: ../../../_assets/aws/emrserverless/emrserverless_16.png
         :alt: emrserverless
         :width: 60%

.. note:: Currently, only Spark Engine is supported for EMR Serverless in Sparkflows.
