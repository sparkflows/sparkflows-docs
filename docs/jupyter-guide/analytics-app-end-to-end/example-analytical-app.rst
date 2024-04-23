Example Analytical App
==================

This is a Hello World Analytical App. It enables the user to run the app and view the output produced by the Jupyter Notebook.

Analytical App Overviw
--------

The below Applications does the following:

* Reads jupyter notebook **jupyter_lab_3.ipynb**.
* Prints the output of the notebook.

.. figure:: ../../_assets/jupyter/example-app.PNG
   :alt: jupyter
   :width: 60%

Jupyter Notebook
------

Below is the Jupyter Notebook which gets invoked by the Analytical App and to output the results back to the Analytical App.

Jupyter Notebook **jupyter_lab_3.ipynb**, contains the below:

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

Once you run the application, It uses **Jupyter Notebook** connection to submit and prints the response back from Jupyter Notebook to Sparkflows UI.

.. figure:: ../../_assets/jupyter/example-app-run.PNG
   :alt: jupyter
   :width: 60%

.. figure:: ../../_assets/jupyter/example-response.PNG
   :alt: jupyter
   :width: 60%
