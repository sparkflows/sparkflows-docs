Digital Ocean (DO)
----

This document outlines the necessary prerequisites for deploying Fire Insights Infrastructure on Digital Ocean.

Memory
++++
The memory Pre-requisites to run Fire Insights:

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

Visit `DO Documentation <https://docs.digitalocean.com/products/droplets/concepts/choosing-a-plan/>`_ to get more details.


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

  Visit documentation page for `Database Authentication <https://docs.sparkflows.io/en/latest/installation/authentication/database-authentication.html>`_ to get more details.

- SAML

  Single sign-on (SSO) enables you to authenticate your users using your organization’s identity provider. If your identity provider supports the SAML 2.0 protocol, you can use Fire Insights SSO to integrate with your identity provider.

  Visit documentation page for `SSO Authentication <https://docs.sparkflows.io/en/latest/installation/authentication/sso/index.html>`_ to get more details.
