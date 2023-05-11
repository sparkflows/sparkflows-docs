Executing Workflows
===================

The ways in which the Fire workflows can be executed are: 
 
 #. Interactively within the User Interface.
 #. Submitting the workflows using Spark-Submit through the command line.
 #. Scheduling for execution with your Scheduler of Choice.
 
Interactively within the User Interface
------------------------------------------

Workflows can be executed from the browser by going into the Execute page of the workflow.


   .. figure:: ../../../_assets/user-guide/workflow/Executing-Workflow/Execute1.png
      :alt: Workflow
      :width: 70%

Executing Workflows with Spark-Submit
--------------------------------------
 
Workflows are saved as JSON files.
Workflows can be submitted to be run on the cluster with Spark-Submit::
  
    spark-submit    --class    fire.execute.WorkflowExecuteFromFile    --master yarn    --deploy-mode client    --executor-memory 1G    --num-executors 1    --executor-cores 1       fire-core-1.4.2-jar-with-dependencies.jar       --postback-url http://<machine>:8080/messageFromSparkJob        --job-id 1         --workflow-file      kmeans.wf


In the above:

+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter          | Details                                                                                                                                                                                                |
+====================+========================================================================================================================================================================================================+
| fire-core jar file | It is the fire-core jar file required code for executing the workflow. The fire-core jar file is in the fire-lib directory of the sparkflows install                                                   |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| postback-url       | http://<machine>:8080/messageFromSparkJob is the postback URL for fire UI. <machine> should be the machine name on which Sparkflows is running. 8080 should be the port on which Sparkflows is running |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| job-id             | 1 is the job id. It can be of any value for now                                                                                                                                                           |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| workflow-file      | kmeans.wf is the json workflow file containing the kmeans workflow in this case.                                                                                                                       |
+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


 For providing extra variables to the workflow, the following parameters can be added to Spark-Submit::
 
    --var name1=value1   --var name2=value2    --var name3=value3
 
In the workflow, these variables can be used with $name1    $name2.
Specific nodes make use of the variables by substituting $name with the value provided for the name.
 
For running the workflow in Debug Mode, add the following parameters::

    --debug true
    

Workflow JSON
--------------
 
In Fire Insights, workflows are saved as JSON Strings. 
  
The View JSON Workflow page of the workflow displays the JSON representations of the workflow. 



  .. figure:: ../../../_assets/user-guide/workflow/Executing-Workflow/ViewJSON.png
     :alt: Sparkflows Json Workflow
     :width: 70%


Scheduling Workflow Execution with Scheduler of Choice
----------------------------------------------------------
 
Since Fire workflows can be submitted with Spark-Submit, you can use your scheduler of choice for scheduling the execution of the workflows.
 
#. Click on the *Schedule button* of the workflow you want to schedule.

   .. figure:: ../../../_assets/user-guide/workflow/Executing-Workflow/Schedule1.png
     :alt: Workflow
     :width: 70%  
 
 
#. Click on the *Schedule New Job for Workflow* tab for the workflow.
 
   .. figure:: ../../../_assets/user-guide/workflow/Executing-Workflow/Schedule2.png
      :alt: Workflow
      :width: 70% 

#. Update the *scheduled timing* & *email notifications* after the success & failure of the workflow as per your requirements.
 
   .. figure:: ../../../_assets/user-guide/workflow/Executing-Workflow/Schedule3.png
      :alt: Workflow
      :width: 50%    

#. Click on *Submit* to save the changes.

   .. figure:: ../../../_assets/user-guide/workflow/Executing-Workflow/Schedule4.png
      :alt: Workflow
      :width: 70%  

 
Debugging Workflows
-------------------
 
Many times it is helpful to be able to debug the workflows. One easy way is to check the *Debug Checkbox* in the UI when executing the workflow.
 
Running in Debug Mode does a few things:

#. Performs a count() after executing each processor. This makes it easier to debug and understand the pipeline. It takes out Fire Insights’ lazy execution from the picture.
#. Displays the number of records processed at each stage.
#. Displays more information for each SQL, etc., which are being executed.





