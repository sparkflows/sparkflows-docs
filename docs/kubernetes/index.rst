
Kubernetes Guide
=========

Fire Insights is integrated with Kubernetes.

There are two scenarios:

* You have a Kubernetes Cluster and Fire Insights can integrate with it.
* You have VM's and need Kubernetes installed on it along with Fire Insights.

If you are on-premise, we recommend installing Rancher.

Fire Insights adds the following services:

  * Fire Insights : for self-serve Advanced Data Analytics
  * Minio : for distributed storage
  * Apache HIVE : for Data Catelog
  * Apache Spark : for Distributed Processing
  * Jupyter : For Machine Learning with Notebooks

This document captures the steps for installing Fire Insights.

Below are the steps:

 * Install Rancher with RKE
 * Install Minio
 * Install Apache Spark
 * Install Apache HIVE
 * Install Jupyter
 * Install Fire Insights
 
.. toctree::
   :maxdepth: 2

   rancher.rst
   minio.rst
   spark.rst
   hive.rst
   jupyter.rst
   fire-insights.rst
   spark-job.rst
   
   
   
   
   
   

   
   
   
   

   
   
