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

Fire Insights Infrastructure requirements setup for deploying on AWS:

The memory needed to run Fire Insights:

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
     - More the vCPU would be preferabler, if data size is bigger
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
   :widths: 10 20 30
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
     - Sparkflows by default run on port 8080 on http
   * - Sparkflows(HTTPS) 
     - 8443
     - Sparkflows by default run on port 8443 on https

.. note:: Auto-creation of security groups adds two groups:

A security group that opens SSH (22), HTTP (80) and HTTPS (443) on all traffic.
