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
Sample MCP Query
++++

.. code-block:: sql

     First, inspect these two parquet files to understand their schemas and sample data:
     
     - 278 request data:
       /home/sparkflows/sparkflows-mcp/data/part-00000-278-requests.snappy.parquet
     
     - 278 response data:
       /home/sparkflows/sparkflows-mcp/data/part-00000-278-responses.snappy.parquet
     
     Then, load and parse this extraction config template:
     
     - /home/sparkflows/sparkflows-mcp/data/extraction_config_template.json
     
     Using:
     
     - the schemas of the 278 request and 278 response parquet files, and
     - the structure of the extraction config template,
     
     do the following:
     
     1. Show me the parsed config from the template and briefly explain the main sections (for example: sources, filters, dedupe/join).
     
     2. Based on the schemas and the 278 use case, generate a NEW extraction config JSON that:
        - Defines four aliases: inReq, outReq, inRes, outRes, each pointing to the appropriate request or response parquet file.
        - For inReq, filters on metadata so that:
          - event_source ends with `GatewayRequest` or `PayerInteractionRequest`
          - msg_domain = 'PA'
          - payload_format = 'X12'
          - event_type = 'IN'
          - market_base IN ('ARK', 'IMN')
          - payload_schema_version IN ('005010X215', '005010X216', '005010X217')
          - trace_id does NOT start with 'e2e-'
        - For outReq, uses the same filters as inReq except event_type = 'OUT'.
        - For inRes, applies the same filter logic as inReq to the response parquet.
        - For outRes, applies the same filter logic as outReq to the response parquet.
        - Includes an expression or configuration that:
          - Deduplicates incoming and outgoing requests/responses by trace_id using the latest event_time.
          - Joins the paired request and response records.
          - Filters for a specific target batch and excludes earlier batch data.
        - Specifies that inReq_batch, outReq_batch, inRes_batch, and outRes_batch are mapped to themselves, and any NULL batch value is replaced with the string "null".
     
     3. Return ONLY:
        - The final extraction config as a single valid JSON object (ready to be saved to a file).

Enter the query in Copilot, and it will return the tool response, including parameters, as shown below.

 .. figure:: ../../_assets/user-guide/copilot/MCP_Response.png
     :alt: copilot configuration
     :width: 60%

 .. figure:: ../../_assets/user-guide/copilot/MCP_Response_1.png
     :alt: copilot configuration
     :width: 60%

