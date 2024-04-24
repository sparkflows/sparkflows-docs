Create Jupyter Notebook
======

You can create Jupyter Notebook as below:

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

 `Click here <https://docs.sparkflows.io/en/latest/jupyter-guide/analytical-apps/output-to-analytical-app.html>`_ to get more details on getting Output from Jupyter Notebook to Analytical App.
