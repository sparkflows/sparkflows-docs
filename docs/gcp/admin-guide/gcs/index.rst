Google Cloud Storage Guide
====

Fire Insights integrates with various data systems, including Google Cloud Storage (GCS), allowing users to configure and automate the flow of data to and from GCS.

Google Cloud Storage (GCS) can be configured and accessed using two primary methods for authentication and authorization: Service Account. Here's a description of each:

#. Using Service Account

   In Google Cloud Platform (GCP), a service account is a special kind of Google account intended for use by applications or virtual machines (VMs), rather than individuals. It provides an identity for applications to interact with GCP services, enabling them to access resources, execute tasks, and perform operations within the GCP environment. 

   Service accounts are typically used for automated processes, APIs, and background tasks that require authentication and authorization.

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
    
    :doc:`/gcp/admin-guide/gcs/service-account`

    Service account setup
    
    ---

    :doc:`/gcp/admin-guide/gcs/gcs-configuration`

    GCS Configuration In Sparkflows
     


.. toctree::
   :hidden:

   service-account.rst
   gcs-configuration.rst
  
