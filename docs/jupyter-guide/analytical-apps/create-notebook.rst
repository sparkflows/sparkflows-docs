Create Jupyter Notebook
======

The Jupyter Notebook serves as the backend logic for the Analytical Apps. It would receive inputs from the App, process it and output results to be displayed back in the App. In order to process and parameters and to send output results to the App a library is made available.

You can create Jupyter Notebook using the below sample code:

::
  
    import sys
    print(sys.argv)
    from fire_notebook.output.workflowcontext import RestWorkflowContext
    import sys
    parameters_list = sys.argv
    restworkflowcontext = RestWorkflowContext(parameters=parameters_list)

    message = "Successfully Received the Message from Notebook!"
    restworkflowcontext.outStr(9, title="Message", text=message)

`Click here <https://docs.sparkflows.io/en/latest/jupyter-guide/analytical-apps/output-to-analytical-app.html>`_ to get more details on getting output from Jupyter Notebook to Analytical App.
