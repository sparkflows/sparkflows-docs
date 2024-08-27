
Kubernetes Guide
=========

Fire Insights is integrated with Kubernetes.

There are two scenarios:

* You have a Kubernetes Cluster and Fire Insights can integrate with it.
* You have VM's and need Kubernetes installed on it along with Fire Insights.

If you are on-premise, we recommend installing Rancher.

Fire Insights adds the following services:

  * Fire Insights : for self-serve Advanced Data Analytics.
  * Minio : for distributed storage.
  * Apache HIVE : for Data Catelog.
  * Apache Spark : for Distributed Processing.
  * Jupyter : For Machine Learning with Notebooks.

This document captures the steps for installing Fire Insights.

  
.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

    :doc:`/kubernetes/rancher`

    Installing Rancher Kubernetes Edition and Rancher.

    ---

    :doc:`/kubernetes/fire-insights`

    Installing Fire Inisights on Kubernetes Cluster.

    ---

    :doc:`/kubernetes/minio`

    Installing minio on Kubernetes Cluster.

    ---

    :doc:`/kubernetes/spark`

    Installing Apache Spark on Kubernetes Cluster.

    ---

    :doc:`/kubernetes/hive`

    Installing Hive.

    ---

    :doc:`/kubernetes/jupyter`

    Installing Jupyter.

    ---

    :doc:`/kubernetes/spark-job`

    Submitting a Spark Job on a Kubernetes Cluster.
   
 
.. toctree::
   :hidden:
   
   kubernetes/index.rst
   rancher.rst
   fire-insights.rst
   minio.rst
   spark.rst
   hive.rst
   jupyter.rst
   spark-job.rst
   
   
   
   
   
   

   
   
   
   

   
   
