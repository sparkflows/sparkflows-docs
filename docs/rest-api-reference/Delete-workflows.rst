Delete workflow
----------------

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Endpoint
     - HTTP Method
     
   * - http://hostname:port/api/v1/workflows/id/130
     - GET  
     
An example request to delete the workflow:    
 
::

     {
    "workflowId": 130
    }    
     
Request Structure

For Deleting a workflow, No action occurs if the workflow has already been deleted. After the workflow is deleted, neither its details nor its run history is visible via the workflow UI or API 

.. list-table:: 
   :widths: 10 40
   :header-rows: 1

   * - Field Name
     - Description
     
   * - workflowId
     - The canonical identifier of the workflow to delete. This field is required.
     
An Example Response:
 
::
 
    Workflow deleted successfully.
