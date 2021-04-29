Joins and Unions
==========

Fire Insights provide processors for performing Joins and Unions


Join/Union Processors in Fire Insights
----------------------------------------


.. list-table:: Join/Union Processors
   :widths: 50 50
   :header-rows: 1

   * - Title
     - Description
   * - UnionAll
     - This node creates a new DataFrame by merging all the rows without removing the duplicates
   * - Union Distinct
     - This node creates a new DataFrame by performing a DISTINCT on the result set, eliminating any duplicate rows
   * - Join Using SQL
     - This node registers the incoming DataFrames as temporary tables and executes the SQL provided
   * - Geo Join
     - This node joins the incoming dataframes
   * - Join On Columns
     - This node joins the incoming dataframes on a column
   * - Join On Common Column
     - This node joins the incoming dataframes on a join Column
   * - Join On Common Columns
     - This node joins the incoming dataframes on 1 or more columns  
