Databricks Prerequisites
=======================

Prerequisites
-------------


Below are the prerequisites for installing Fire Insights on a Databricks Cluster:

.. list-table:: Prerequisites
   :widths: 10 20 40
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


Enabling Scala on High Concurrency Cluster
-------------------------------------------

The Databricks High Concurrency cluster does not enable scala by default. You can do it manually by following the steps given below:

Go to Configurations-->> Advanced Options -->> Spark -->> and add the below in Spark Config

::

    spark.databricks.repl.allowedLanguages sql,python,r,scala

.. note::  

   1. Path to Fire core jar in Databricks Environment is required.
   2. User who is sharing the token for databricks connection, must have manage permission.
   3. Path to main python file in Databricks Environment, if using python engine.

