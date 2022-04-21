Validate Address
=========== 

This node validate the USA address

Input
--------------
It accepts a DataFrame as input from the previous Node

Output
--------------
A new column isValidAddress is added which contains valid or inValid values

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeValidateAddress

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputColName
        - Input Column Name
        - input column name


Details
-------


This node validates an address.

It creates a new Dataframe by adding a column stating where Address Column contains valid address or not.

Some of the valid address formats are as below:

*  123 xyx avenue
*  1/1 block-D street


Examples
-------


Incoming Dataframe has following rows:

CUST_CD    |    Address
-----------------------------------
CUST001    |    123 xyx avenue
CUST002    |    abc 986 street
CUST003    |    1/1 block-D street
CUST004    |    123 9876block park

If ValidateAddress node is configured to validate address mentioned in [Address] column then outgoing Dataframe would be created as below:

CUST_CD    |    Address               |    isValidAddress
--------------------------------------------------------------
CUST001    |    123 xyx avenue        |    valid
CUST002    |    abc 986 street        |    inValid
CUST003    |    1/1 block-D street    |    valid
CUST004    |    123 9876block park    |    inValid
