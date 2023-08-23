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
     - More the memory would be better
   * - vCPU
     - 8
     - More the vCPU would be better, if data size is bigger
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

