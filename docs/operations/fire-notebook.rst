Fire Notebook
==========
This document explains in detail the steps to effectively use Fire Notebook, a robust platform for executing code in the EMR environment using Livy.

.. Note:: Make sure there is a Livy connection for executing the notebook code in EMR environment using Livy.

Step 1: Enable Notebook Editor
----------
#. Go to Administration > Configurations.
#. Click on Module tab -> Set **module.enableFireNotebook** value to **true**.
#. Set Notebook S3 folder location -> Go to app tab and set value of **app.notebookFiles.s3.location**. 
   
   Example - s3a://db-8be1940f53aa6aeb86bdd8de9439e142-s3-root-bucket/notebook

   .. figure:: ..//_assets/operating/fire-notebook/enable-notebook-using-configuration-1.png
      :alt: operating-fire-notebook
      :width: 60%
#. Click on **Save Configurations** button.

   .. figure:: ../_assets/operating/fire-notebook/notebook-list-2.png
      :alt: operating-fire-notebook
      :width: 60%

Step 2 : Create and Execute Notebook
-------------
#. Go to any existing Project or Create a new Project.
#. Click on **Notebooks** tab > click on **Create Notebook** button.

   .. figure:: ../_assets/operating/fire-notebook/notebook-editor-3.png
      :alt: operating-fire-notebook
      :width: 60%

#. Input the **name** of the notebook and select engine type as either **Scala** or **PySpark**.
#. Select **Livy connection** that will be used to execute scala or pyspark code to execute in the EMR environment.

   .. figure:: ../_assets/operating/fire-notebook/s3-location.png
      :alt: operating-fire-notebook
      :width: 60%
#. Write **Code** in editor and click on **Execute icon** to execute.

Step 3 : View Results
------------
#. Results are displayed in the result section. To fetch the latest result from livy server :

   Click on the **Refresh icon** that is in the right top corner of the result section.

Step 4 : Save, Download or Copy Code
---------------
#. Code can be saved in the backend storage by clicking on **Save icon**.
#. Code can be downloaded from editor by clicking on **Download icon**.
#. Code can be copied from editor by clicking on **Copied icon**.

Step 5 : Close the Notebook Editor
-------------
#. Click on **Close icon (x)** located in top corner to close the editor.

Executions Section
------------
The Execution tab contains all the executions of the notebook executed by the user.

#. **View Log**: Click on **File icon** to see the log of execution.

#. **Refresh State**: Click on **Refresh icon** to update the state of execution and see the state.

#. **Delete**: Click on **Delete icon** to delete the execution.

   

      
