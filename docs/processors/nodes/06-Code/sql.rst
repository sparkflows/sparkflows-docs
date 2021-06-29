SQL
=========== 

This node runs the given SQL on the incoming DataFrame

Input
--------------
This type of node takes in a DataFrame and transforms it to another DataFrame

Output
--------------
This node runs the given SQL on the incoming DataFrame to generate the output DataFrame

Type
--------- 

transform

Class
--------- 

fire.nodes.etl.NodeSQL

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - tempTable
        - Temp Table
        - Temp Table Name to be used
      * - sql
        - SQL
        - SQL to be run
      * - schema
        - Schema
      * - outputColNames
        - Output Column Names
        - Name of the Output Columns
      * - outputColTypes
        - Output Column Types
        - Data Type of the Output Columns
      * - outputColFormats
        - Output Column Formats
        - Format of the Output Columns


Details
-------


This node receives an input data frame, creates a temporary table on top of that data frame.
Allows the user to write a SQL which would be executed on the temporary table.
The resulting data frame of running the SQL is passed on to the next node.


Examples
-------


Format Examples
+++++++++++++++

Temp Table Name: tempTable
Input Schema: id, price, lotsize, bedrooms, bathrms, stories, driveway, recroom, fullbase, gashw, airco, garagepl, prefarea

 avg price of house
```````````````
SQL:  select avg(price) as avg_price from tempTable


 bedrooms with avg price greater than 10000
```````````````
SQL: select bedrooms, avg_price from
(select bedrooms, avg(price) as avg_price from tempTable group by bedrooms) as temp where avg_price > 10000


 house details with bedrooms avg price greater than 10000
```````````````
SQL: select tempTable.* , inner_table.avg_price from
(select bedrooms, avg_price from
(select bedrooms, avg(price) as avg_price from tempTable group by bedrooms) as temp where avg_price > 10000) as inner_table
JOIN tempTable ON(inner_table.bedrooms = tempTable.bedrooms)
