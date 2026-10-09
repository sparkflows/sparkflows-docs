Installation and Upgrade
========================

Install Sparkflows on a laptop, virtual machine, cloud environment, Docker, or Kubernetes.

Choose Your Deployment Option
-----------------------------

Before installing Sparkflows, choose the deployment model that best fits your environment, use case, scalability, and operational requirements.

* **Deployment Overview** — Compare supported deployment models. See :doc:`/installation/deployment-overview/index`.
* **Docker Deployment** — Recommended for simple VM and container-based installations.
* **Linux VM Deployment** — Install Sparkflows directly on a Linux server.
* **Windows Deployment** — Install Sparkflows in Windows environments.
* **macOS / Developer Installation** — Lightweight setup for development, demos, and evaluation.
* **Cloud Deployment** — Guidance for AWS, Azure, GCP, and other cloud platforms.
* **Kubernetes Deployment** — Recommended for scalable and highly available enterprise environments.

.. list-table::
   :widths: 40 60
   :header-rows: 1

   * - Environment
     - Recommended Deployment
   * - Developer laptop
     - Docker, TGZ
   * - Single VM
     - Docker or TGZ installation
   * - Production enterprise
     - Kubernetes
   * - Cloud VM
     - Docker or TGZ installation
   * - Large-scale HA deployment
     - Kubernetes


.. panels::
   :container: container-lg pb-3
   :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2

   :doc:`/installation/installation/linux-installation/index`

   Sparkflows Installation on Linux

   ---

   :doc:`/installation/installation/docker-linux-install`

   Running Sparkflows Docker Image on Linux

   ---

   :doc:`/installation/installation/macos-install/index`

   Sparkflows Installation on MacOS

   ---

   :doc:`/installation/installation/windows-tgz/index`

   Sparkflows Installation on Windows

   ---

   :doc:`/installation/installation/windows-laptop-desktop-installer`

   Sparkflows Installer for Windows Laptop and Desktops

   ---

   :doc:`/installation/installation/docker-windows-install`

   Running Sparkflows Docker Image on Windows 10

   ---

   :doc:`/installation/installation/kubernetes-install`

   Sparkflows Installation on Kubernetes

   ---

   :doc:`AWS Installation </aws/admin-guide/deploy-aws>`

   Deploy Sparkflows on AWS

   ---

   :doc:`Azure Installation </azure/admin-guide/deploy-azure>`

   Deploy Sparkflows on Azure

   ---

   :doc:`GCP Installation </gcp/admin-guide/installation-guide/index>`

   Deploy Sparkflows on GCP


.. toctree::
   :hidden:

   linux-installation/index.rst
   macos-install/index.rst
   windows-tgz/index.rst
   windows-laptop-desktop-installer.rst
   docker-windows-install.rst
   docker-linux-install.rst
   kubernetes-install.rst
