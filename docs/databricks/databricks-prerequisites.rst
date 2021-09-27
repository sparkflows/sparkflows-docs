Databricks Prerequisites
=======================

Prerequisites
-------------


Below are the Prerequisites for installing Fire Insights on a Databricks Cluster:

.. list-table:: Below are the Needed Package
   :widths: 10 20 40
   :header-rows: 1

   * - Package
     - Description
     - Value
   * - Python version
     - python version on Databricks Cluster
     - 3.6.0 or above
   * - pip version
     - pip version on Databricks Cluster
     - 20.0 or above
   * - Spark version
     - Spark Version on Databricks Cluster
     - 2.4
   * - Fire Running Port
     - Port on Which Fire is Running
     - Accessible from databricks Cluster 


Enabling Scala on High Concurrency Cluster
-------------------------------------------

The Databricks High Concurrencly cluster does not enable scala by default. It can be done with the below steps:

Go to Configurations-->> Advanced Options -->> Spark -->> and add the below in Spark Config

::

    spark.databricks.repl.allowedLanguages sql,python,r,scala

.. note::  

   1. Databricks job submit jar path is required
   2. User who is sharing the token for databricks connection, must have manage permission

