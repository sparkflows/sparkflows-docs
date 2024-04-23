Example Analytical App
==================

Sparkflows enable you to run the Application which uses Jupyter Notebook.

Applications
--------

The below Applications does the following:

* Reads jupyter notebook **jupyter_lab_3.ipynb**.
* Prints the output of the notebook.

.. figure:: ../../_assets/jupyter/example-app.PNG
   :alt: jupyter
   :width: 60%

Jupyter Notebook
------

Jupyter Notebook **jupyter_lab_3.ipynb**, Contains below:

::

    print("I am jupyter lab")
   I am jupyter lab

::
  
    import os
    os.getcwd()
    print()
    import sys
    print(sys.argv)

::
  
    webserverURL = "http://localhost:8080/messageFromSparkJob"
    jobId = "123456789"
    from fire_notebook.output.workflowcontext import RestWorkflowContext
    restworkflowcontext = RestWorkflowContext(webserverURL, jobId)

   message = "Successfully Received the Message from Notebook!"
   restworkflowcontext.outStr(9, title="Message", text=message)

Prints the Results
------------------

Once you run the application, It prints the response from Jupyter Notebook.

.. figure:: ../../_assets/jupyter/example-app-run.PNG
   :alt: jupyter
   :width: 60%

.. figure:: ../../_assets/jupyter/example-response.PNG
   :alt: jupyter
   :width: 60%

