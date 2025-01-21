Google Cloud Platform (GCP)
----

This document outlines the necessary prerequisites for deploying Fire Insights Infrastructure on Google Cloud Platform.

Memory
++++

The memory pre-requisites needed to run Fire Insights:

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 16GB+
     - More memory would be preferable
   * - vCPU
     - 8+
     - More vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 500GB+
     - Depending on Job Compute, if running locally

Instance Type & OS Supported
++++

.. list-table:: 
   :widths: 10 10 10 30
   :header-rows: 1

   * - OS
     - Instance type
     - Virtual CPUs
     - Memory (GB)
   * - Ubuntu 20.04
     - e2-standard-16
     - 16
     - 64
   * - Ubuntu 20.04
     - e2-standard-8
     - 8
     - 32
   * - Ubuntu 20.04
     - e2-standard-4
     - 4
     - 16

Visit `GCP Documentation <https://cloud.google.com/compute/all-pricing?_ga=2.4671216.-296646568.1599141903>`_ to get more details.

Software Specifications
++++

Ensure that you have the following prerequisites with regard to software specifications:

.. list-table:: 
   :widths: 10 40 30
   :header-rows: 1

   * - Title
     - Details
     - Notes
   * - Java
     - JDK 8
     - Java 8 is needed
   * - Python
     - Python 3.8
     - Python 3.8 is needed
   * - Users
     - Root access is needed during installation for installing JDK, Another user (can be called sparkflows) would be used for the installation of Sparkflows
     - This user can be “sparkflows”
   * - HTTPS
     - Ensure DNS and https certificates are set up
     - HTTPS certificate available

Virtual Networks
++++

A virtual network is an object representing the networking setup of instances created into it.

The virtual network defines in which VPC and subnet the instances will be launched, as well as how DNS hostnames and HTTPS certificates for the instances will be used.

Each instance belongs to a virtual network. At least one virtual network is required to deploy instances.

Networking Requirements
++++

.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Name
     - Port
     - Comment
   * - SSH
     - 22
     - For SSH to vm
   * - HTTP
     - 80
     - For Accessing on HTTP
   * - HTTPS
     - 443
     - For Accessing on HTTPS
   * - Fire Insights(HTTP) 
     - 8080
     - Fire Insights by default run on port 8080 on http
   * - Fire Insights(HTTPS) 
     - 8443
     - Fire Insights by default run on port 8443 on https

.. note:: A security group that opens SSH (22), HTTP (80) and HTTPS (443) on all traffic.


HTTPS Configuration
++++

By default, Fire Insights instances are deployed with self-signed certificates. These will trigger security alerts in your browser.

Single Sign-On
++++

Single sign-on (SSO) refers to the ability for users to log in just one time with one set of credentials to get access to all corporate apps, websites, and data for which they have permission.

By setting up SSO in Fire Insights, your users will be able to access Fire Insights using their corporate credentials.

- Users database 

  For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/authentication/database-authentication.html>`_

- SAML 

  Single sign-on (SSO) enables you to authenticate your users using your organization’s identity provider. 

  If your identity provider supports the SAML 2.0 protocol, you can use Fire Insights SSO to integrate with your identity provider.

  For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/authentication/sso/index.html>`_

Before you begin, ensure that you have the following prerequisites in place:

VM Privilege
++++

Ensure that you have VM with sufficient privileges to install packages.


Databricks Cluster Access
++++

Ensure that you have Databricks Cluster URL accessible from Sparkflows Instance.
