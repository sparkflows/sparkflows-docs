Airflow Connection
--------------

Sparkflows enables you to create "AWS MWAA Airflow Connection" and use it to submit Pipeline. Connections can be at various levels:

  * Global  : Everyone has access to these connections.
  * Group   : Users belonging to the group have access to these connections.
  * Project : The owner of the project and the groups with which the project has been shared with have access to the project level connections.

This page show how to create a "Livy Connection" in Fire Insights.

Enable Airflow in Sparkflows
===========

Login to ``Sparkflows`` application -> ``Administration`` -> ``Configurations`` -> ``Connection`` -> and enable Livy connection by setting the below parameter:

::

    airflow.enabled	: true

.. figure:: ../../_assets/aws/mwaa/mwaa_airflow_enabled.png
   :alt: mwaa
   :width: 60%

Navigate to Add Connections
===========

Once you save the above Configuration, navigate to ``Administration`` -> ``Global Connections`` -> ``Add Connections`` as shown below:

.. figure:: ../../_assets/aws/livy/administration.png
   :alt: livy
   :width: 60%
   
Add connection for group
========

Navigate to ``Administration`` -> ``Global Connections`` -> ``Add Connections`` -> ``Add Connection For Group`` which pop up a new windows -> Select ``Compute Connection`` and other parameters as shown below:

.. figure:: ../../_assets/aws/mwaa/mwaa-addconnection.png
   :alt: mwaa
   :width: 60%

.. figure:: ../../_assets/aws/mwaa/mwaa-airflow.png
   :alt: mwaa
   :width: 60%

Add additional parameters as per your environment
======

Once you have selected  the connection type & groups, add the additional connection parameters needed. For more details refer the following tables and images:

For GENERAL tab
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Description
     - Value
