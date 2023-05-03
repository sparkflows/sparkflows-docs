GCP Configuration
=====

Fire Insights is seamlessly integrated with Google cloud platform. With Fire Insights you can perform self-serve data processing, analytics and machine learning on Google Cloud.

Below are steps:

1. Specify GCP Configuration
============

GCP Configuration details can be specified in the Fire Insights Administration UI.

- Enable Google CLoud Integration flag
- Specify the Project Id
- Specify the path to the Service Account Key file


.. figure:: ../_assets/gcp/GCP_Configuration.jpg
   :alt: GCP Configuration Details
   :width: 40%

2. Enable Dataproc Connection
============

Enable Dataproc Connection from ``CONNECTION`` tab

::

    connection.dataproc.enabled : true

3. Specify Dataproc Connection
============

Dataproc Connections details can be specified in Global Connections.

- Specify the Connection Name
- Specify the Postback Url
   
 .. figure:: ../_assets/gcp/Edit_Connection_2.jpg
   :alt: GCP Configuration Details
   :width: 40%

- Specify the location of Fire Core jar
- Specify the Project Id
- Specify the Region
- Specify the Dataproc Cluster name

.. figure:: ../_assets/gcp/Edit_Connection_1.jpg
   :alt: Dataproc Configuration Details
   :width: 40%
 
