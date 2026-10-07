Windows Installation using TGZ file
===================================

Install Sparkflows directly on a Windows machine from the Sparkflows TGZ package. This is a bare-metal installation: Sparkflows runs as a set of Windows processes started from the scripts in the package, without Docker.

Before You Choose This Method
-----------------------------

**Use the TGZ package if** you want Sparkflows on a Windows laptop, desktop or server, with full control over where it is installed and how its processes are started.

**What is available on bare-metal Windows:**

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Available
     - Not available on bare-metal Windows
   * - * The Sparkflows web application and workflow execution
       * Agents and Polars jobs, after the optional Python 3.9 setup
     - * The PySpark engine, and the features that depend on it: AutoML, Prophet, ARIMA, Scikit-learn and Keras/TensorFlow models, and other Python-native packages

**Use another method instead if:**

* You need the features in the right-hand column. Use :doc:`/installation/installation/docker-windows-install` on Windows, or install Sparkflows on Linux with :doc:`/installation/installation/linux-installation/index`.
* You want a guided install on a laptop or desktop. Use :doc:`/installation/installation/windows-laptop-desktop-installer`.
* You need to submit jobs to a Spark cluster. Install Sparkflows on an edge node of the cluster instead.

Installation Steps
------------------

Follow these pages in order:

#. :doc:`prerequisites-install`: check Windows, hardware and disk, and install Java 17, winutils.exe and hadoop.dll. Optionally install Python 3.9 for Agents and Polars.
#. :doc:`windows-install`: download and extract Sparkflows, set up the database, start Sparkflows, verify it, log in and secure it, and optionally enable Agents and Polars.
#. :doc:`windows-upgrade`: back up, upgrade to a new release, verify, and roll back if needed.
#. :doc:`troubleshooting`: find the cause of a problem and the fix.


.. toctree::
   :hidden:

   prerequisites-install.rst
   windows-install.rst
   troubleshooting.rst
   windows-upgrade.rst
