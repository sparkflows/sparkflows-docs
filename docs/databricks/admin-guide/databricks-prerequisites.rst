Databricks Prerequisites
=======================

Prerequisites
-------------

Below are the prerequisites for installing Fire Insights on a Databricks Cluster:

.. list-table::
   :widths: 15 20 40
   :header-rows: 1

   * - Package
     - Description
     - Value
   * - Python version
     - Python version on Databricks cluster
     - 3.7.0 or above
   * - pip version
     - pip version on Databricks cluster
     - 20.0 or above
   * - Spark version
     - Spark Version on Databricks cluster
     - 3.2.x.
   * - DBR Runtime version
     - DBR Runtime version
     - 10.4
   * - Fire Running Port
     - Port on which Fire is running
     - The machine and port on which Fire is running has to be accessible from the databricks cluster


Enable Scala on High Concurrency Cluster
-------------------------------------------

By default, Scala is not enabled on the Databricks High Concurrency cluster. 

To enable Scala, you can manually configure it by following these steps:

#. Access the Databricks Platform.

#. Go to the **Configurations** section.

#. Navigate to **Advanced Options**.

#. Find the **Spark** section within the advanced options.

#. Add the following configuration entry under **Spark Config**:

   ::

    spark.databricks.repl.allowedLanguages sql,python,r,scala

.. note::  

   #. To operate in the Databricks Environment, you need to specify the path to the Fire core jar.
   #. When sharing a token for Databricks connection, ensure that the user has the requisite manage permissions.
   #. If you are using the Python engine in the Databricks Environment, remember to specify the path to the main Python file.

