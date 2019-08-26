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
     
An example request to Execute specific workflow:   

::

    {
  "emailOnFailure": "string",
  "emailOnSuccess": "string",
  "libJars": "string",
  "programParameters": "string",
  "sparkConfig": "string",
  "workflowId": 0
}

Request Structure

For Executing specific workflow, we need to add below parameters

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
   
   * - projectId
     - The canonical identifier of the workflow to Execute. This field is required.
   
   * - workflowId
     - The canonical identifier of the workflow to Execute. This field is required.
     

An Example response:

::

   200


List all the executions
------------------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - /api/v1/workflow-executions?page=0&size=1000'
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
     
     

