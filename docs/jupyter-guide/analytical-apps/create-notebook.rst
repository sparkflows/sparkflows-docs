Create Jupyter Notebook
======

You can create Jupyter Notebook using the below sample code:

::
  
    import sys
    print(sys.argv)
    from fire_notebook.output.workflowcontext import RestWorkflowContext

    webserverURL = "http://localhost:8080/messageFromSparkJob"
    jobId = "123456789"
    from fire_notebook.output.workflowcontext import RestWorkflowContext
    restworkflowcontext = RestWorkflowContext(webserverURL=webserverURL, jobId=jobId)

    message = "Successfully Received the Message from Notebook!"
    restworkflowcontext.outStr(9, title="Message", text=message)

`Click here <https://docs.sparkflows.io/en/latest/jupyter-guide/analytical-apps/output-to-analytical-app.html>`_ to get more details on getting output from Jupyter Notebook to Analytical App.
