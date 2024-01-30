Amazon Web Services (AWS)
----

This document outlines the necessary prerequisites for deploying Fire Insights Infrastructure on AWS.


Memory
++++
Ensure that you have the following prerequisites with regard to memory specifications:

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
Ensure that you have the following prerequisites with regard to Instance type and OS specifications :

.. list-table:: 
   :widths: 10 10 10 10 30
   :header-rows: 1

   * - OS
     - Instance type
     - vCPU
     - Memory (GiB)
     - AMI ID
   * - RHEL 8.X
     - m4.xlarge
     - 4
     - 16
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - m4.2xlarge
     - 8
     - 32
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - t2.xlarge
     - 4
     - 16
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - t2.2xlarge
     - 8
     - 32
     - ami-096fda3c22c1c990a
   * - RHEL 8.X
     - t3.xlarge
     - 4
     - 16
     - ami-096fda3c22c1c990a 
   * - RHEL 8.X
     - t3.2xlarge
     - 8
     - 32
     - ami-096fda3c22c1c990a
   * - Ubuntu 20.04
     - c5a.8xlarge
     - 32
     - 64
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - c3.8Xlarge
     - 32
     - 64 
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t2.xlarge
     - 4
     - 16 
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t2.2xlarge
     - 4
     - 16
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t3.xlarge
     - 4
     - 16
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - t3.2xlarge
     - 8
     - 32 
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - m5.xlarge
     - 4
     - 16
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - m5.2xlarge
     - 8
     - 32 
     - ami-0261755bbcb8c4a84
   * - Ubuntu 20.04
     - r5.2xlarge
     - 8
     - 64 
     - ami-0261755bbcb8c4a84

Visit `AWS Documentation <https://aws.amazon.com/ec2/instance-types>`_ to get more details.

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
Ensure that you meet the following prerequisites with regard to networking requirements:

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

  Visit `Database Authentication Page <https://docs.sparkflows.io/en/latest/installation/authentication/database-authentication.html>`_ for more details.

- SAML

  Single sign-on (SSO) enables you to authenticate your users using your organization’s identity provider. If your identity provider supports the SAML 2.0 protocol, you can use Fire Insights SSO to integrate with your identity provider.

  Visit `SSO Documentation <https://docs.sparkflows.io/en/latest/installation/authentication/sso/index.html>`_ for more details.
