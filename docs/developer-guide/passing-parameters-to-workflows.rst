Passing Parameters to Workflows
===============================


Sparkflows runs the spark jobs with ``spark-submit``. It takes in the workflow JSON as a parameter. There are multiple ways to pass extra parameters to the workflow.
 
  * Though a Parameter Node in the workflow
  * As more parameters on the command line when running the workflow with spark-submit with --var
  * Specifying it in Administration/Configuration to be passed to all the jobs submitted.
  
Through a Parameter Node in the Workflow
-----------------------------------------
 
A Parameter Node can be added to the workflow. It allows passing key/value pairs to the workflow.

Through ``--var`` parameters with spark-submit
--------------------------------------------------
 
Workflows can be submitted to be run on the cluster with spark-submit. Extra parameters can be passed with ``--var``::

 
    spark-submit    --class fire.execute.WorkflowExecuteFromFile    --master yarn    --deploy-mode client    --executor-memory 1G    --num-executors 1    --executor-cores 1    fire-core-1.4.2-jar-with-dependencies.jar    --postback-url http://<machine>:8080 --job-id 1      --workflow-file kmeans.wf    --var name1=value1  --var  name2=value2

 
In the workflow, these variables can be used with ``$name1    $name2``
 
Specific nodes make use of the variables by **substituting   $name   with the value** provided for the name.


An **example** would be :     ``--var id=3``

When specifying the expression in the RowFilter Node we can use :   ``id > $id``

In the above **$id** would be replaced with **3**.
 
 

Specifying ``--var`` parameters for all in Sparkflows User Interface
-----------------------------------------------------------------
 
Sparkflows also allows specifying the **--var** parameters to be passed to all the jobs submitted through Sparkflows. Below is the screen under Administration/Configuration.

In the above, **app.vars** parameter allows specifying a space separated list of name=value pairs. 

Each of these are passed to the jobs submitted by Sparkflows with ``--var name=value``
