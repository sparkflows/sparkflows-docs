Databricks Python Integration Steps
======================

Sparkflows integrates with Databricks and can submit Python jobs. It submits jobs to the Databricks clusters using the REST API of Databricks and have the results displayed back in Sparkflows.

Below are the steps for Integrating Sparkflows with your Databricks Clusters for running Python jobs.

.. note::  The Machine on which Sparkflows is installed should have Python 3.7.0 or above.

Python Installation Steps:

  * https://docs.sparkflows.io/en/latest/installation/python-install-linux.html


Install Sparkflows
-----------

Install Sparkflows on your machines. The machine has to be reachable from the Databricks cluster.

Upload Fire wheel file to Databricks
----------------------------------

Sparkflows wheel file has to be uploaded to Databricks. Sparkflows jobs running on Databricks make use of this wheel file.

Upload ``fire-x.y.z/dist/fire-3.1.0-py3-none-any.whl`` to Databricks. Upload it under Workspace as a Library on to Databricks under DBFS or even in S3 Bucket which is accessible from the Databricks Cluster.


.. figure:: ../_assets/configuration/wheelfile.PNG
   :alt: Wheel File
   :width: 90%

1. Login to ``Databricks Cluster``


2. Click on ``workspace`` in the left side pane


.. figure:: ../_assets/configuration/azure_workspace.PNG
   :alt: Databricks
   :width: 60%
   
3. Create a new Library

You can select Library Source as ``DBFS``, Library Type as ``Python Whl``, provide any ``Library Name`` field, & add File Path of ``fire-3.1.0-py3-none-any.whl`` located in DBFS.

.. figure:: ../_assets/configuration/python-lib.PNG
   :alt: Databricks
   :width: 60%

On Clicking on ``Create`` button it will ask to install on specific databricks Cluster, select cluster on which you want to install.

.. figure:: ../_assets/configuration/create.PNG
   :alt: Databricks
   :width: 60%
   
.. figure:: ../_assets/configuration/install.PNG
   :alt: Databricks
   :width: 60%
   
On Successfull installation of wheel file on Databricks Cluster, it would be displayed under ``Libraries``.

.. figure:: ../_assets/configuration/wheelpack.PNG
   :alt: Databricks
   :width: 70%

Another option is to upload ``fire-3.1.0-py3-none-any.whl`` file to s3 Bucket which is accessible from Databricks Cluster.

Once you upload ``fire-3.1.0-py3-none-any.whl`` file to s3 Bucket, login to Databricks Cluster & inside Libraries tab.

Install New Library & select ``DBFS/S3`` in Library Source, ``Python Whl`` in Library Type and copy paste the location of python wheel file available in s3 in File Path & Click on Install.

.. figure:: ../_assets/configuration/s3wheel.PNG
   :alt: Databricks
   :width: 70%

Once it is installed successfully, you can see the python wheel inside Library is up.

.. figure:: ../_assets/configuration/uploads3wheel.PNG
   :alt: Databricks
   :width: 90%


Install Python dependencies
-----------------------

You need to install the python dependencies required by Sparkflows on the machine by running below Command from ``fire-x.y.z/dist/fire/`` directory::

    pip install -r requirements.txt

.. figure:: ../_assets/configuration/pip_dependency.PNG
   :alt: Databricks
   :width: 90%

Note: Make sure that pip etc. is already installed on that machine


Install dependency for JDBC Driver
--------------------------

Copy the ``JDBC Driver`` jar to pyspark jar path, Once it is copied successfully, you can see the JDBC Driver jar inside pyspark jar path::

    cp -r SparkJDBC41.jar $PATH_VIRTUAL_ENV/venv/lib/python3.7/site-packages/pyspark/jars/

.. figure:: ../_assets/configuration/copy_view.PNG
   :alt: Databricks
   :width: 90%
   
 

Install dependency for AWS
--------------------------

Copy the jars ``hadoop-aws`` and ``aws-java-sdk`` to pyspark jar path.

.. figure:: ../_assets/configuration/awssdkjar.PNG
   :alt: Databricks
   :width: 90%

Install any specific package of python, if Need to use in Custom Processors on databricks Cluster aswellas Sparkflows Machine.

Use the command below to install it on the Sparkflows machine::

    pip install scorecardpy

.. figure:: ../_assets/configuration/scorecard-machine.PNG
   :alt: Databricks
   :width: 90%

Install it on your Databricks cluster with the below::

   * Open a Notebook and attach to Databricks Cluster.
   * %sh pip install scorecardpy

.. figure:: ../_assets/configuration/scorecard.PNG
   :alt: Databricks
   :width: 90%

Install prophet package on databricks
-------------------------------------

Install needed python package for prophet using init script on databricks cluster

::

    #!/bin/bash
    pip install pip==20.0.2
    pip uninstall -y pystan
    pip install pystan==2.19.1.1
    pip install numpy==1.17.3
    pip install prophet==1.1.1
    

add above in a script file, upload in DBFS and go to Advanced Options, select Init Scripts and add DBFS path to it 

.. figure:: ../_assets/configuration/initscript.PNG
   :alt: Databricks
   :width: 90%

Upload Fire workflowexecutedatabricks.py file to DBFS
----------------------------------

For Python Job submission to Databricks Cluster.

Upload ``fire-x.y.z/dist/workflowexecutedatabricks.py``, file to DBFS or even S3 Bucket too.

.. figure:: ../_assets/configuration/workflow.PNG
   :alt: Databricks
   :width: 90%

You can ``UPLOAD`` it, using DBFS Browser too.

.. figure:: ../_assets/configuration/databr_wf.PNG
   :alt: Databricks
   :width: 90%

Configure the Uploaded Library in Sparkflows
------------------------------------

Configure the path of the uploaded fire python wheel package file & workflowexecutedatabricks.py under ``databricks.pythonFile`` & ``databricks.pythonPackages`` respectively in Sparkflows.

It can be two source either ``DBFS`` or ``S3`` path.

If you have Uploaded in ``DBFS`` path.

.. figure:: ../_assets/configuration/db_configure.PNG
   :alt: Databricks
   :width: 90%

If you have Uploaded in ``S3`` path.

.. figure:: ../_assets/configuration/s3db_configure.PNG
   :alt: Databricks
   :width: 90%

Job Submission using Pyspark Engine
-----------------------------------

Now You can submit pyspark jobs to Databricks Cluster from Sparkflows.

.. figure:: ../_assets/configuration/job_1.PNG
   :alt: Submit Job
   :width: 90%


