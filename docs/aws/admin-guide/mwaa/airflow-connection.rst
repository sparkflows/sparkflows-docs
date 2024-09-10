Airflow Connection
--------------

Sparkflows enables you to create **AWS MWAA Airflow Connection** and use it to submit Pipeline. Connections can be at various levels:

  * **Global**  : Everyone has access to these connections.
  * **Group**   : Users belonging to the group have access to these connections.
  * **Project** : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This document outlines the steps to create an Airflow Connection in Fire Insights.

Enable Airflow in Sparkflows
=========================

Login to **Sparkflows -> Administration -> Configurations -> AIRFLOW ->** and enable Airflow by setting the below parameter:

::

    airflow.enabled	: true

.. figure:: ../../../_assets/aws/mwaa/mwaa_airflow_enabled.png
   :alt: mwaa
   :width: 60%

Navigate to Add Connections
=========================

Once you save the above Configuration, navigate to **Administration -> Global Connections -> Add Connections** as shown below:

.. figure:: ../../../_assets/aws/livy/administration.png
   :alt: livy
   :width: 60%
   
Add Connection for Group
=======================

Navigate to **Administration -> Global Connections -> Add Connections -> Add Connection For Group which pops up a new window -> Select Pipeline and other parameters** as shown below:

.. figure:: ../../../_assets/aws/mwaa/mwaa-addconnection.png
   :alt: mwaa
   :width: 60%

.. figure:: ../../../_assets/aws/mwaa/mwaa-airflow.png
   :alt: mwaa
   :width: 60%

Add Additional Parameters as per your Environment
===============================================

Once you have selected  the connection type & groups, add the additional connection parameters needed. For more details refer the following tables and images:

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
     - Postback Url through which Airflow sent result back to Fire Insights
   * - Title 
     - Title of Selected Connection
     - Title of Selected Connection  
   * - Description 
     - Connection Description 
     - Connection Description

.. figure:: ../../../_assets/aws/mwaa/mwaa-general.png
   :alt: mwaa
   :width: 60%


For AIRFLOW tab
++++++
.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
   * - Auth Type
     - Auth Type
     - Assume Role
   * - Airflow Dag
     - Airflow Dag
     - Airflow Dag path configured in AWS MWAA
   * - Airflow Endpoint URL
     - Airflow Endpoint URL
     - Airflow Endpoint URL in AWS MWAA
   * - Airflow IAMRole
     - Airflow IAMRole
     - Airflow IAMRole being assume for accessing aws mwaa resources
   * - Airflow Jar Location
     - Airflow Jar Location
     - Fire Core Jar Location path added in s3
   * - Airflow Python Script Location
     - Airflow Python Script Location
     - Fire Python Script Location path added in s3
   * - AWS Region
     - AWS Region
     - AWS Region of aws mwaa resources
   * - Environment Name
     - Environment Name
     - Environment Name of aws mwaa resources

.. figure:: ../../../_assets/aws/mwaa/mwaa_airflow_tab.png
   :alt: mwaa
   :width: 60%

.. note:: Ensure that the Execution role attached to Amazon MWAA can be assumed by the ECS or EC2 instance role where the Fire Insights application is running. Attach the role to the ECS or EC2 instance to access the DAG location in S3 and upload the DAG. For example, **AmazonMWAA-sparkflows-air-4HboCJ** is the Execution role attached to Amazon MWAA, and **ecsTaskExecutionRole** is the role used by ECS Execution. You need to update the **Trust relationship** for both roles to allow them to assume each other."

Trust relationsship for **AmazonMWAA-sparkflows-air-4HboCJ** as below:

.. figure:: ../../../_assets/aws/mwaa/trustpolicy_1.png
   :alt: mwaa
   :width: 60%


Trust relationsship for **ecsTaskExecutionRole** as below:

.. figure:: ../../../_assets/aws/mwaa/trustpolicy_2.png
   :alt: mwaa
   :width: 60%


Test and Save the Airflow Connection
===========

After adding the updated parameters, click the **Test Connection** button, and **Save** it once the test is successful.


.. figure:: ../../../_assets/aws/mwaa/mwaa_testconnection.png
   :alt: mwaa
   :width: 60%

