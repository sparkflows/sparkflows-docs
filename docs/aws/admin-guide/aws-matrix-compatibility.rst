AWS Matrix Compatibility
===============

This document outlines the Matrix Compatibility details on AWS.

Spark, EMR, Java and Python Support Compatibility Matrix
++++++++

.. list-table:: 
   :widths: 10 10 10 10
   :header-rows: 1

   * - Spark Version	
     - EMR Vesrion
     - Java Version
     - Python Version
   * - 3.2.1
     - 6.7.0
     - Java 8
     - 3.7.0
   * - 3.3.0
     - 6.9.0
     - Java 8 
     - 3.7.0

Airflow Support Compatibility Matrix
++++++++

.. list-table:: 
   :widths: 10 10 
   :header-rows: 1

   * - Airflow Standalone Version	
     - Airflow MWAA Version
   * - V2.3.x
     - 2.8.1

Spark, Databricks, Java and Python Support Compatibility Matrix
++++++++

.. list-table:: 
   :widths: 10 10 10 10
   :header-rows: 1

   * - Spark Version	
     - Databricks Vesrion
     - Java Version
     - Python Version
   * - 3.2.1
     - 10.4
     - Java 8
     - 3.8.0


Matrix Compatibility
++++
Ensure that you have the following AWS specifications while Integrating with Fire Insights :

.. list-table:: 
   :widths: 20 10 40
   :header-rows: 1

   * - Title
     - supported Version
     - Details
   * - EMR
     - 6.6.0
     - https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-660-release.html
   * - EMR
     - 6.7.0
     - https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-670-release.html
   * - EMR
     - 6.9.0
     - https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-690-release.html
   * - Spark
     - 3.2.1
     - Compatible with EMR 6.7.0
   * - Spark
     - 3.3.0
     - Compatible with EMR 6.9.0
   * - Airflow (Standalone Installation)
     - V2.3.x
     - Standalone installations on ec2
   * - Airflow MWAA Support
     - 2.8.1
     - https://aws.amazon.com/blogs/big-data/introducing-amazon-mwaa-support-for-apache-airflow-version-2-8-1/


It also lists the compatability matrix of Spark version and Delta lake version:

`Spark and Delta Lake Compatibility Matrix <https://docs.delta.io/latest/releases.html>`_

