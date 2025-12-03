Airflow Connection
--------------

Sparkflows enables you to create Airflow Connection and use it to submit Pipeline. Connections can be at various levels:

  * **Global**  : Everyone has access to these connections.
  * **Group**   : Users belonging to the group have access to these connections.
  * **Project** : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This page explains how to create an Airflow Connection in Sparkflows. Follow the steps below:

Step 1 : Enable Airflow in Sparkflows
======================================

* Login to **Sparkflows**.

* Navigate to  **Administration -> Configurations -> AIRFLOW** and enable Airflow by setting the value of below parameter to **true** and save the configuration.

  ::

     airflow.enabled : true

  .. figure:: ../../../_assets/aws/livy/airflow-enabled.png
     :alt: mwaa
     :width: 60%

Step 2 : Navigate to Connections Page
======================================

* Once you save the above Configuration, navigate to **Administration -> Global/Group Connections -> Add Connections** as shown below:

  .. figure:: ../../../_assets/aws/livy/fire_administration.png
     :alt: livy
     :width: 60%
   
Step 3 : Add Connection for Group
=================================

* From the Connections page, click on **Add Connections** button and select **Add Connection For Group** from the dropdown.


  .. figure:: ../../../_assets/aws/mwaa/connections-add.png
     :alt: mwaa
     :width: 60%

* Now, select **Pipeline** as storage category and other parameters as shown below:

  .. figure:: ../../../_assets/aws/mwaa/mwaa-airflow.png
     :alt: mwaa
     :width: 60%

Step 4 : Add Additional Parameters as Per Your Environment
==========================================================

* Once you have selected the connection type & group, add the additional connection parameters needed. For more details refer the following tables and images:

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
     * - Postback Url
       - Postback Url
       - Postback Url through which Airflow sent result back to Sparkflows
     * - Title 
       - Title of Selected Connection
       - Title of Selected Connection  
     * - Description 
       - Connection Description 
       - Connection Description

  .. figure:: ../../../_assets/aws/mwaa/mwaa-general.png
     :alt: mwaa
     :width: 60%


For AIRFLOW Tab
++++++
  .. list-table:: 
     :widths: 10 20 30
     :header-rows: 1

     * - Title
       - Description
       - Value
     * - Auth Type
       - Auth Type
       - BASIC
     * - Username
       - Username
       - Username
     * - Password
       - Password
       - Password
     * - Airflow Dag
       - Airflow Dag
       - Airflow Dag path configured in Airflow
     * - Airflow Endpoint URL
       - Airflow Endpoint URL
       - Airflow Endpoint URL in Airflow
     * - Airflow IAMRole
       - Airflow IAMRole
       - Airflow IAMRole being assume for accessing Airflow
     * - Airflow Jar Location
       - Airflow Jar Location
       - Fire Core Jar Location path added in s3
     * - Airflow Python Script Location
       - Airflow Python Script Location
       - Fire Python Script Location path added in s3
     * - AWS Region
       - AWS Region
       - AWS Region of aws mwaa resources
   
  .. figure:: ../../../_assets/configuration/airflow/airflow_v2.png
     :alt: airflow
     :width: 60%

Step 5 : Test and Save the Airflow Connection
===============================================

* Once the Updated Parameter is added, you can **Test Connection** & **Save** it.


  .. figure:: ../../../_assets/configuration/airflow/airflow_v3.png
     :alt: mwaa
     :width: 60%

* Now you can use this connection to submit pipeline on Airflow.

.. note:: Make sure that Airflow Machine is accessible from the Sparkflows Machine.
