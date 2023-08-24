Infrastructure Deployment Requirements
=====
Recommended setup for deploying Fire Insights on a cloud provider in your tenant. Supported cloud providers are:

- Amazon Web Services (AWS)
- Digital Ocean (DO)
- International Business Machines Corporation(IBM)
- Google Cloud Platform (GCP)
- Microsoft Azure

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
     - 16gb
     - More the memory would be preferable
   * - vCPU
     - 8
     - More the vCPU would be preferable, if data size is bigger
   * - Disk Size
     - 500GB
     - Depending on Job Compute, If running locally

Instance type & OS Supported
++++

.. list-table:: 
   :widths: 10 20 30
   :header-rows: 1

   * - OS
     - Instance type
     - AMI ID
   * - RHEL8.X
     - m4.xlarge
     - ami-096fda3c22c1c990a
   * - RHEL8.X
     - m4.2xlarge
     - ami-096fda3c22c1c990a
   * - RHEL8.X
     - t2.xlarge
     - ami-096fda3c22c1c990a
   * - RHEL8.X
     - t2.2xlarge
     - ami-096fda3c22c1c990a
   * - RHEL8.X
     - t3.xlarge
     - ami-096fda3c22c1c990a 
   * - RHEL8.X
     - t3.2xlarge
     - ami-096fda3c22c1c990a
   * - ubuntu20.04
     - t2.xlarge
     - ami-0261755bbcb8c4a84
   * - ubuntu20.04
     - t2.2xlarge
     - ami-0261755bbcb8c4a84
   * - ubuntu20.04
     - t3.xlarge
     - ami-0261755bbcb8c4a84
   * - ubuntu20.04
     - t3.2xlarge
     - ami-0261755bbcb8c4a84
   * - ubuntu20.04
     - m5.xlarge
     - ami-0261755bbcb8c4a84
   * - ubuntu20.04
     - m5.2xlarge
     - ami-0261755bbcb8c4a84
   * - ubuntu20.04
     - r5.2xlarge
     - ami-0261755bbcb8c4a84

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
   * - Sparkflows(HTTP) 
     - 8080
     - Fire Insights by default run on port 8080 on http
   * - Sparkflows(HTTPS) 
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
