Workflow Execution API
======================

Execute
------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow/execute
     - POST
     
An Example request to Execute specific workflow:   

::

    {
     "emailOnFailure": "string",
     "emailOnSuccess": "string",
     "libJars": "string",
     "programParameters": "string",
     "sparkConfig": "string",
     "workflowId": 1
    },

Request Structure

For Executing specific workflow, we need to add below parameters

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
      
   * - workflowId
     - The canonical identifier of the workflow to Execute. This field is required.
     

An Example response:

::

   200


List all Executions
------------------------

.. list-table:: 
   :widths: 20 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions?
     - GET
     
Request Structure

For Listing all the executions, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - page
     - The number of pages can be added.
   
   * - size
     - The different size can be added. 
     
An Example response:

::

   200 
   
List Executions of Workflow
------------------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/workflows/
     - GET
     
Request Structure

For Listing executions of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowId
     - The canonical identifier of the List execution of workflow. This field is required.   
     
An Example response:

::

    200     

Stops workflow Execution
------------------------

.. list-table:: 
   :widths: 40 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-execution/{workflowExecutionId}/stop
     - GET
     
Request Structure

For Stopping execution of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowExecutionId
     - The canonical identifier of the Execution of workflow. This field is required.   
     
An Example response:

::

    200

Kill workflow Execution
-----------------------

.. list-table:: 
   :widths: 40 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-execution/{workflowExecutionId}/kill
     - GET
     
Request Structure

For Killing execution of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - workflowExecutionId
     - The canonical identifier of the Execution of workflow. This field is required.   
     
An Example response:

::

    200
    
Delete Workflow Executions by days
-----------------------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/days/{days}
     - DELETE
     
Request Structure

For deleting execution of a workflow, we need to add below parameters:

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - days
     - The canonical identifier of the Execution of workflow. This field is required.   
     
An Example response:

::

    200

Get Executed Task Count
-----------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/tasks/count
     - GET
     
    
An Example response:

::

    200

Get Latest Executions
---------------------

.. list-table:: 
   :widths: 30 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions/latest
     - GET
     
An Example response:

::

    200     
