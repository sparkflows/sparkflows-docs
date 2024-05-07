Generate Pyspark Code
====================

Fire Inisghts enables you to Generate PySpark Code even with Spark engine and run the job using Python engine.

This document explains in detail the steps involved in the process.

Step 1 : Login in to Fire Insights
----------------
#. Go to Fire Insights Home page.
#. Enter you credentials and click **Sign in**.

Step 2 : Enable Auto Pyspark Code Generation
---------------
#. From the Dashborad, click **ADMINISTRATION** tab located in the top-menu bar.
#. From Administration page, click **Configurations**.
#. On the Configurations page, select **MODULE** tab.
#. In the Module tab, search for **module.enableAutoPysparkCodeGeneration** and set it to **true**.


   **Note:** 'module.enableAutoPysparkCodeGeneration' is initially set to false by default.

   .. figure:: ../../_assets/user-guide/generate-pyspark-code/pyspark_code.png
      :alt: Pyspark code generate
      :width: 60%

Step 3 : Generate Pyspark Code
----------------

#. Once the Configuration gets enabled for Generating Pyspark Code, create a sample workflow using Spark engine and save it.

   .. figure:: ../../_assets/user-guide/generate-pyspark-code/pyspark_wf.PNG
      :alt: Pyspark code generate
      :width: 60%
   
#. Once the workflow gets saved, go to **Workflow Editor** page, click on the **three dots** on the top right corner of workflow editor page, and select **Generate Pyspark Code**.

   .. figure:: ../../_assets/user-guide/generate-pyspark-code/pyspark_generate.PNG
      :alt: Pyspark code generate
      :width: 60%

#. Once you select the option of Generate Pyspark Code, a window will open with Pyspark sample code for the sample workflow, **copy** it and **save** it into **.py** file.

   .. figure:: ../../_assets/user-guide/generate-pyspark-code/pyspark_code.PNG
      :alt: Pyspark code generate
      :width: 70%

Step 4 : Upload Generated Pyspark Code in DBFS
--------------

#. Now, as you have the Generated Pyspark Code saved in your local system, upload it into DBFS which is accessible from databricks cluster.

   .. figure:: ../../_assets/user-guide/generate-pyspark-code/5.PNG
      :alt: Pyspark code generate
      :width: 70%

Step 5 : Submit Jobs on Databricks Cluster
----------

#. Once you have uploaded the Generated Pyspark Code in DBFS, create Jobs in databricks using the details given below:

   ::

       Task name: Add Unique Task name
       Type : Select Type as Python & Enter the URI of the Python file to be executed
       Cluster : Select any existing databricks cluster or even new one.
       Parameters : If any
       Advanced options : Add dependency if any
    
   .. figure:: ../../_assets/user-guide/generate-pyspark-code/6.PNG
      :alt: Pyspark code generate
      :width: 60%    

#. Once the above parameters gets added, click on **Create** button, to create a new job with your selected parameters.


   .. figure:: ../../_assets/user-guide/generate-pyspark-code/6.PNG
      :alt: Pyspark code generate
      :width: 70% 

#. **Run** the Job.
   
   Once the Job runs successfully, you will see the **Status** of the Job as **Succeeded**.

   .. figure:: ../../_assets/user-guide/generate-pyspark-code/code_generate_databricks.png
      :alt: Pyspark code generate
      :width: 70% 


