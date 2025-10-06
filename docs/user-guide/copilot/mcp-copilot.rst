Copilot with MCP Connection
====

This guide explains how to use an MCP connection with Copilot to automatically generate nodes for workflows or pipelines.

Steps to Use MCP Connection with Copilot
----

Step 1: Create an MCP Connection
++++
Follow the steps below to create an MCP connection to use it with copilot.

 * Go to **Administration -> Global/Group Connections**.
 * Click on **Add Connection** button and choose **Add Connection For All**.
 * Select the Connection Category - **API** and Connection Type - **MCP**.
 * Fill the required MCP connection details as shown below.


 .. figure:: ../../_assets/user-guide/copilot/create-mcp-connection.png
     :alt: copilot configuration
     :width: 60%

Step 2: Select the MCP Connection in Copilot
++++
Once the MCP connection is created, the user needs to select the MCP connection in the copilot.

 .. figure:: ../../_assets/user-guide/copilot/update-copilot.png
     :alt: copilot configuration
     :width: 60%

Step 3: Access Copilot in Designer Pages
++++
Once the Copilot is set up, it can be used from Workflow Designer page or Pipeline Designer page.


Step 4: Add Query in Copilot
++++
Enter the query in Copilot and it will return the next steps in JSON format, including parameters, as shown below.

 .. figure:: ../../_assets/user-guide/copilot/add-query-in-copilot-1.png
     :alt: copilot configuration
     :width: 60%

 .. figure:: ../../_assets/user-guide/copilot/add-query-in-copilot-2.png
     :alt: copilot configuration
     :width: 60%


Step 5: Confirm to Create Node
++++
Once the user clicks on **Confirm**, the specific node will be created automatically in the editor.

 .. figure:: ../../_assets/user-guide/copilot/copilot-auto-node-creation.png
     :alt: copilot configuration
     :width: 60%

.. note::

   MCP Request and Response should follow the below Sparkflows format.

   Example User Queries:
   
   1. create read csv node with path S3://testdir/test.csv  
   2. create legoblockXMl with clusterid=jbh1875 and stepname=lego and deploy-mode=client

   Tool Api/Method should be present with tools/list

   Tools List Request:

   {
     "jsonrpc" : "2.0",
     "id" : 1,
     "method" : "tools/list",
     "params" : { }
   }

   Tools List Response:

   {
     "result": {
       "tools": [
         {
           "input_schema": {
             "type": "object",
             "properties": {
               "StepName": {
                 "description": "Name of the execution step",
                 "type": "string"
               },
               "deploy-mode": {
                 "description": "Deployment mode (e.g., cluster, client)",
                 "type": "string"
               },
               "ClusterId": {
                 "description": "Cluster identifier for the logo block",
                 "type": "string"
               }
             },
             "required": ["ClusterId", "StepName", "deploy-mode"]
           },
           "name": "logoblockXMl",
           "description": "Parse XML for Logo Block with cluster and deployment configuration",
           "output_schema": {
             "type": "object",
             "properties": {
               "isError": {"type": "boolean"},
               "content": {
                 "items": {
                   "properties": {
                     "text": {"type": "string"},
                     "type": {"type": "string"}
                   },
                   "type": "object"
                 },
                 "type": "array"
               }
             },
             "required": ["content", "isError"]
           },
           "next_steps": {}
         },
         {
           "input_schema": {
             "type": "object",
             "properties": {
               "path": {
                 "description": "Path to the CSV file to read",
                 "type": "string"
               }
             },
             "required": ["path"]
           },
           "name": "ReadCSV",
           "description": "Read CSV file from the specified path",
           "output_schema": {
             "type": "object",
             "properties": {
               "isError": {"type": "boolean"},
               "content": {
                 "items": {
                   "properties": {
                     "text": {"type": "string"},
                     "type": {"type": "string"}
                   },
                   "type": "object"
                 },
                 "type": "array"
               }
             },
             "required": ["content", "isError"]
           },
           "next_steps": {}
         }
       ]
     },
     "id": "1",
     "jsonrpc": "2.0"
   }

   Tools call request for node:

   Tool Api/Method should be present with tools/call

   Params : {
   Name :  tool name 
   Arguments : parameter’s key 
   }

   Json:

   {
     "jsonrpc" : "2.0",
     "params" : {
       "name" : "ReadCSV",
       "arguments" : {
         "path" : "D://testDir/test.csv"
       }
     },
     "method" : "tools/call",
     "id" : 1
   }

   Tool Call response from MCP:

   Parameters = Fields in the workflow/pipelines name should match

   {
     "status" : "success",
     "tool_name" : "ReadCSV",
     "result" : {
       "message" : "Read CSV file from path"
     },
     "next_steps" : [ {
       "parameters" : [ {
         "description" : "Path to the CSV file",
         "type" : "string",
         "path" : "D://testDir/test.csv"
       }, {
         "description" : "CSV Configuration Parameter",
         "type" : "string",
         "csvConfig" : "{\"delimiter\":\",\",\"header\":true,\"blockId\":\"a84033f4\",\"timestamp\":\"2025-10- 
       01T17:36:53.5835424\",\"path\":\"D://testDir/test.csv\",\"encoding\":\"utf-8\"}"
       }, {
         "description" : "Position Parameter",
         "type" : "string",
         "position" : "{\"zIndex\":1,\"gridAlign\":true,\"y\":200,\"x\":150,\"height\":120,\"width\":250}"
       } ],
       "node_name" : "Read CSV",
       "required" : [ "message", "next_steps" ],
       "action" : "create_node"
     } ]
   }
   
















