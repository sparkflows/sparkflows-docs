Execute Stored Procedure In Snowflake
=====

Sparkflows provides a node to execute Snowflake stored procedures with **input and output parameters**, enabling seamless integration of Snowflake logic within workflows. The output DataFrame contains return values which can be referenced in subsequent nodes using parameter placeholders (schema: parameter name & value).

The **Execute Stored Procedure in Snowflake** node can be added at the start, middle, or end of a workflow.


Configuration Steps
-----
  
1. Set Auth-Type and Connection Details
++++
  
  Configure the following: 
  
  * ``Auth Type``: Select **KeyPair** from the dropdown.
  * ``Connection``: Select **SNOWFLAKE_KEYPAIR** from the dropdown.
  * ``Warehouse``: Select the required **Snowflake Warehouse** by using browse button.
  * ``Database``: Select the required **Snowflake Database** by using browse button.
  * ``Schema``: Select the Snowflake Schema as **PUBLIC**. 


  .. figure:: ../../_assets/user-guide/utilities/execute-sf-sp-node-config.png
   :alt: Snowflake Stored Procedure
   :width: 80%
  
  
  
  
  
  
2. Set the Call Statement with Input Parameters
++++
  Configure the call statement of the stored procedure, including its input parameters, as shown below.

  It supports both **single** and **multiple** input parameters with parameter types: **String**, **Integer**, and **Datetime**.


  .. figure:: ../../_assets/user-guide/utilities/config-call-stmt.png
     :alt: Snowflake Stored Procedure
     :width: 80%
  
  
  
  
3. Configure Return Parameters
+++++

  Define the return parameters and their types. The return parameter name can be accessed in the subsequent nodes using the syntax: **${SP_Return_Value_Name}**

  .. figure:: ../../_assets/user-guide/utilities/config-return-parameters.png
     :alt: Snowflake Stored Procedure
     :width: 80%
  
  
  
  
  
  
  **Example Usage**
  
  If the stored procedure returns fields such as **C_CUSTKEY** and **C_NAME**, their values can be accessed in next nodes like **AddAdvancedColumn** using: **${C_CUSTKEY}** and **${C_NAME}**.

  .. figure:: ../../_assets/user-guide/utilities/return-parameters-example.png
     :alt: Snowflake Stored Procedure
     :width: 80%
  

























