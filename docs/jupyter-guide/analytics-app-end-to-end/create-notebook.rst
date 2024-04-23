Create Notebook
==================

This document describes the steps to create the Notebook. Follow the steps given below:

Create the Notebook with below two default parameters:

#. webserverUrl 
#. jobID

then create the RestWorfklowContext to send the messages back to Sparkflows Apps ::

  webserverURL = sys.argv[1]
  jobId = sys.argv[2]
  from fire_notebook.output.workflowcontext import RestWorkflowContext
  restworkflowcontext = RestWorkflowContext(webserverURL, jobId)
  
`Example Notebook <https://github.com/sparkflows/fire-tools/tree/main/jupyter-docker/notebooks>`_
