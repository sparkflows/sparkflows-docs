Databricks Python Integration Steps
======================

Fire Insights integrates with Databricks and can submit Python jobs. 

It submits jobs to the Databricks clusters using the REST API of Databricks and have the results displayed back in Fire Insights.

This document explains in detail the steps needed for Integrating Fire Insights with Databricks clusters for running Python jobs.

.. note::  The Machine on which Fire Insights is installed should have Python 3.7.0 or above.

Follow the steps given below :

Step 1 : Install Python
----------

* To install Python on Red Hat and CentOS, follow the steps given at the below link:
  
  `Python Installation Steps for Red Hat and CentOS <https://docs.sparkflows.io/en/latest/installation/installation/python-install-redhat-centos.html>`_

* To install Python on Ubuntu, follow the steps given at the below link:
  
  `Python Installation Steps for Ubuntu <https://docs.sparkflows.io/en/latest/installation/installation/python-install-ubuntu.html>`_

* To install Python on MacOS, follow the steps given at the below link: 
  
  `Python Installation Steps for MacOS <https://docs.sparkflows.io/en/latest/installation/installation/python-install-macos.html>`_

Step 2 : Install Fire Insights
-----------

Install Fire Insights on your machine. The machine has to be accessible from the Databricks cluster.

`Click here <https://docs.sparkflows.io/en/latest/installation/installation/index.html>`_ to know more.

Step 3 : Upload Fire Wheel File to Databricks
----------------------------------
Fire Insights wheel file has to be uploaded to Databricks. Fire Insights jobs running on Databricks make use of this wheel file.

Upload the file, **fire-x.y.z/dist/fire-3.1.0-py3-none-any.whl**, either under Workspace as a Library on to Databricks under DBFS or in S3 Bucket which is accessible from the Databricks Cluster.

 
**To upload as Library, follow the below steps :**

#. **Login** to your **Databricks Account** using your credentials.
#. Click on **Compute** located on the left side pane.
   
   .. figure:: ../../_assets/configuration/databricks_intsall_lib.PNG
      :alt: Databricks
      :width: 40%
   
#. Click on **Install new** from **Libraries** tab.

   .. figure:: ../../_assets/configuration/databricks_intsall_lib.PNG
      :alt: Databricks
      :width: 40%

#. Upload WHL File **fire-3.1.0-py3-none-any.whl** either from your machine or
   
   use the download link from the previous step by selecting the **Drop WHL here** option or you can upload it **dbfs** location and copy the full path.


   .. figure:: ../../_assets/configuration/databricks_lib.PNG
      :alt: Databricks
      :width: 40%

#. Once **fire-3.1.0-py3-none-any.whl** path is updated, click on **install**.

   .. figure:: ../../_assets/configuration/databricks_lib_update.PNG
      :alt: Databricks
      :width: 40%
   
   .. note:: This will install library on Databricks cluster.


**To upload via S3 bucket, follow the steps below :**

#. Upload **fire-3.1.0-py3-none-any.whl** file to S3 Bucket.
#. **Login** to Databricks Cluster. 
#. Go to Libraries tab.
#. Install new Library by selecting :

   **DBFS/S3** as Library Source.
    
   **Python Whl** as Library Type.

   Copy/Paste the location of python wheel file available in S3 in File Path.

   And finally, click on **Install**.
    
   .. figure:: ../../_assets/configuration/databricks_s3.PNG
      :alt: Databricks
      :width: 70%

   Once it is installed successfully, you can see that the python wheel inside Library is up.

   

Step 4 : Install Python Dependencies
-----------------------

You need to install the python dependencies required by Fire Insights on the machine, you can refer Step 1. 

   .. note:: Make sure that pip with latest version is already installed on that machine.


Step 5 : Install Dependency for JDBC Driver
--------------------------

#. Copy the **JDBC Driver** JAR to pyspark JAR path. 

   Once it is copied successfully, you can see the JDBC Driver JAR inside pyspark JAR path.

   ::

      cp -r SparkJDBC41.jar $PATH_VIRTUAL_ENV/venv/lib/python3.7/site-packages/pyspark/jars/

   .. figure:: ../../_assets/configuration/copy_view.PNG
      :alt: Databricks
      :width: 70%
   
 

Step 6 : Install Dependency for AWS
--------------------------

#. Copy the JARS **hadoop-aws** and **aws-java-sdk** to pyspark JAR path, if S3 is configured.

   .. figure:: ../../_assets/configuration/awssdkjar.PNG
      :alt: Databricks
      :width: 70%


Step 7 : Install Prophet Package on Databricks
-------------------------------------

#. Install the needed python package needed for Fire Insights using Init script on databricks cluster.

   Use the below command:

   ::

        #!/bin/bash
        pip install --upgrade pip
        pip uninstall -y pystan==3.1.1
        pip install pystan==2.19.1.1
        pip install prophet==1.1.1
        pip install numpy==1.17.3
        pip install nbconvert==6.0.0rc0
        pip install Jinja2==3.0.3
        pip install --upgrade jupyter_client
        pip install pycaret==2.3.10
        pip install catboost==1.0.4
        pip install h2o-pysparkling-3.2==3.36.1.2.post1
        pip install great_expectations==0.13.0
        pip install scorecardpy==0.1.9.2
        pip install black
        pip install numpy==1.21.4
        pip install numba==0.53.0
        pip install scikit-learn==0.24.0
        pip install holidays==0.14.2
        pip install openpyxl
        pip install huggingface-hub==0.14.1
        pip install shap
        pip install transformers
        pip install torch==1.9.1+cpu torchvision==0.10.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
        pip install urllib3==1.25.11
        pip install bs4
        pip install kfp==1.8.1
        pip install pulp    

   Add above in a **script file**, upload in **workspace** and go to **Advanced Options**, select **Init Scripts** and add **workspace path** to it. 

   
Step 8 : Upload Fire workflowexecutecloud.py file to DBFS
----------------------------------

#. For Python Job submission to Databricks Cluster:

   Upload **fire-x.y.z/dist/workflowexecutecloud.py**, file to **DBFS** or even  to **S3 Bucket**.

   You can upload it using the DBFS browser too.

   
Step 9 : Configure Uploaded Library in Fire Insights
------------------------------------

Configure the path of the uploaded **fire python wheel package file & workflowexecutecloud.py.py** in Compute Connection in Fire Insights.

`Click here <https://docs.sparkflows.io/en/latest/installation/connection/compute-connection/databricks.html>`_ to know more.

Step 10 : Submit Job using Pyspark Engine
-----------------------------------

Now, you can submit pyspark jobs to Databricks Cluster from Fire Insights.

  .. figure:: ../../_assets/configuration/databricks_job1.PNG
     :alt: Submit Job
     :width: 70%

  .. figure:: ../../_assets/configuration/databricks_job2.PNG
     :alt: Submit Job
     :width: 70%


