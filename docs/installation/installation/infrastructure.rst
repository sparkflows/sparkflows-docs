Infrastructure Deployment Requirements
=====
Recommended setup for deploying Fire Insights on a cloud provider in your tenant. Supported cloud providers are:

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)
- Digital Ocean (DO)
- International Business Machines Corporation(IBM)



Amazon Web Services (AWS)
----

Fire Insights Infrastructure Pre-requisites for deploying on AWS:

The memory Pre-requisites to run Fire Insights:

Memory
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 16GB+
     - More the memory would be preferable
   * - vCPU
     - 8+
     - More the vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 500GB+
     - Depending on Job Compute, If running locally

Instance type & OS Supported
++++

Instance Type & OS Supported
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - OS
     - Instance type
     - AMI ID
   * - RHEL 8.X
     - m4.xlarge
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - m4.2xlarge
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - t2.xlarge
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - t2.2xlarge
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - t3.xlarge
     - ami-096fda3c22c1c990a 
   * - RHEL 8.X
     - t3.2xlarge
     - ami-096fda3c22c1c990a
   * - Ubuntu 20.04
     - c5a.8xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - c3.8Xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t2.xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t2.2xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t3.xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t3.2xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - m5.xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - m5.2xlarge
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - r5.2xlarge
     - ami-0261755bbcb8c4a84

Software Specifications
++++

Ensure that you have the following prerequisites with regard to software specifications :

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
     - Python 3.7
     - Python 3.7 is needed
   * - Users
     - Root access is needed during installation for installing JDK, Another user (can be called sparkflows) would be used for the installation of Sparkflows
     - This user can be “sparkflows”
   * - HTTPS
     - Ensure DNS and https certificates are set up
     - HTTPS certificate available


Virtual networks
++++

A virtual network is an object representing the networking setup of instances created into it.

The virtual network defines in which VPC and subnet the instances will be launched, as well as how DNS hostnames and HTTPS certificates for the instances will be used.

Each instance belongs to a virtual network. At least one virtual network is required to deploy instances.

Networking requirements
++++

.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Name
     - Port
     - Comment
   * - SSH
     - 22
     - For SSH to ec2 instance
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

HTTPS configuration
++++

By default, Fire Insights instances are deployed with self-signed certificates. These will trigger security alerts in your browser.

Single Sign-On
++++

Single sign-on (SSO) refers to the ability for users to log in just one time with one set of credentials to get access to all corporate apps, websites, and data for which they have permission.

By setting up SSO in Fire Insights, your users will be able to access Fire Insights using their corporate credentials.

- Users database

Reference URL : https://docs.sparkflows.io/en/latest/installation/authentication/database-authentication.html

- SAML

Single sign-on (SSO) enables you to authenticate your users using your organization’s identity provider. If your identity provider supports the SAML 2.0 protocol, you can use Fire Insights SSO to integrate with your identity provider.

Reference URL : https://docs.sparkflows.io/en/latest/installation/authentication/sso/index.html

Microsoft Azure
----

Fire Insights Infrastructure Pre-requisites for deploying on Azure:

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
   :widths: 10 30
   :header-rows: 1

   * - OS
     - Instance type
   * - Ubuntu 20.04
     - D4s_v3
   * - Ubuntu 20.04
     - D8s_v3
   * - Ubuntu 20.04
     - Standard_D8s_v3
   * - Ubuntu 20.04
     - Standard_E8bds_v5

More details can be found here : https://learn.microsoft.com/en-us/azure/virtual-machines/fsv2-series

Software Specifications
++++

Ensure that you have the following prerequisites with regard to software specifications :

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
     - Python 3.7
     - Python 3.7 is needed
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

Ensure that you have Databricks Cluster URL is accessible from Sparkflows Instance.

Google Cloud Platform (GCP)
----

Fire Insights Infrastructure Pre-requisites for deploying on GCP:

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
   :widths: 10 30
   :header-rows: 1

   * - OS
     - Instance type
   * - Ubuntu 20.04
     - e2-standard-16
   * - Ubuntu 20.04
     - e2-standard-8
   * - Ubuntu 20.04
     - e2-standard-4


Software Specifications
++++

Ensure that you have the following prerequisites with regard to software specifications :

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
     - Python 3.7
     - Python 3.7 is needed
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

Ensure that you have Databricks Cluster URL is accessible from Sparkflows Instance.


Digital Ocean (DO)
----

Fire Insights Infrastructure Pre-requisites for deploying on DO:

The memory Pre-requisites to run Fire Insights:

Memory
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - Title
     - Recommended
     - Value
   * - Memory
     - 16GB+
     - More the memory would be preferable
   * - vCPU
     - 8
     - More the vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 500GB+
     - Depending on Job Compute, If running locally

Droplet & OS Supported
++++

.. list-table:: 
   :widths: 20 30
   :header-rows: 1

   * - OS
     - Droplet type
   * - CentOS 7 x64
     - Memory-Optimized 3x SSD / 32 GB
   * - CentOS 7 x64
     - Memory-Optimized 16 GB / 8 vCPUs
   * - CentOS 8 x64
     - Memory-Optimized 3x SSD / 32 GB
   * - CentOS 8 x64
     - Memory-Optimized 16 GB / 8 vCPUs
   * - Ubuntu 20.04(LTS)x64
     - Memory-Optimized 3x SSD / 32 GB
   * - Ubuntu 20.04(LTS)x64
     - Memory-Optimized 16 GB / 8 vCPUs
   
Virtual networks
++++

A virtual network is an object representing the networking setup of instances created into it.

The virtual network defines in which VPC and subnet the Droplet will be launched, as well as how DNS hostnames and HTTPS certificates for the instances will be used.

Each Droplet belongs to a virtual network. At least one virtual network is required to deploy on Droplet.

Networking requirements
++++

.. list-table:: 
   :widths: 20 10 30
   :header-rows: 1

   * - Name
     - Port
     - Comment
   * - SSH
     - 22
     - For SSH to Droplet
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

HTTPS configuration
++++

By default, Fire Insights Droplet are deployed with self-signed certificates. These will trigger security alerts in your browser.

Single Sign-On
++++

Single sign-on (SSO) refers to the ability for users to log in just one time with one set of credentials to get access to all corporate apps, websites, and data for which they have permission.

By setting up SSO in Fire Insights, your users will be able to access Fire Insights using their corporate credentials.

- Users database

Reference URL : https://docs.sparkflows.io/en/latest/installation/authentication/database-authentication.html

- SAML

Single sign-on (SSO) enables you to authenticate your users using your organization’s identity provider. If your identity provider supports the SAML 2.0 protocol, you can use Fire Insights SSO to integrate with your identity provider.

Reference URL : https://docs.sparkflows.io/en/latest/installation/authentication/sso/index.html
