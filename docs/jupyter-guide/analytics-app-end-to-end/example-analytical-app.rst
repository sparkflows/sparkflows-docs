First Analytical App Example
============================

This is a Hello World Analytical App. It enables the user to run the Jupyter notebook and view the results in the Sparkflows Analytical App UI.

Analytical App Overview
-----------------------

The following Analytical App performs the below listed tasks:

* Reads the Jupyter Notebook named **jupyter_lab_3.ipynb** which is in the docker image in the `home directory` set in the docker image. The notebook can reside on any path inside the docker image.
* Displays the results returned from the Jupyter Notebook on the Sparkflows Analytical App UI


.. figure:: ../../_assets/jupyter/example-app.PNG
   :alt: jupyter
   :width: 60%

Jupyter Notebook
----------------

Below is the Jupyter Notebook that gets invoked by the Analytical App and the results are seen in the Sparkflows Analytical App UI.

Jupyter Notebook **jupyter_lab_3.ipynb**, contains the below code:

::

    webserverURL = "http://localhost:8080/messageFromSparkJob"
    jobId = "123456789"
    from fire_notebook.output.workflowcontext import RestWorkflowContext
    restworkflowcontext = RestWorkflowContext(webserverURL, jobId)

    message = "Successfully Received the Message from Notebook!"
    restworkflowcontext.outStr(9, title="Message", text=message)

Display the Results
------------------

When you run the Analytical App, it utilizes the Jupyter Notebook `connection` to submit the job to Kubernetes cluster and streams back the response back from the Jupyter Notebook to the Sparkflows Analytical App UI.

.. figure:: ../../_assets/jupyter/example-app-run.PNG
   :alt: jupyter
   :width: 60%

.. figure:: ../../_assets/jupyter/example-response.PNG
   :alt: jupyter
   :width: 60%

