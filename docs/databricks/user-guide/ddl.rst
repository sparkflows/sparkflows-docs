Running DDL Commands
===========================

Fire Insights allows you to run DDL commands on Databricks.

With this one can:

  - Create New Databases
  - Create New Tables
  - View the schema of the tables
  - And many more

Go to DATABROWSERS/Databricks DB. Then click on DDL.

Databricks has a good page on Creating New Tables:

https://docs.databricks.com/spark/latest/spark-sql/language-manual/create-table.html

Below are example of running DDL
--------------------------------

Creating Table
++++++++++++++

statement: 

``` 
CREATE TABLE `employee` (`id` INT, `name` STRING) USING com.databricks.spark.csv OPTIONS ( `multiLine` 'false', `escape` '"', `header` 'true', `delimiter` ',', path 'dbfs:/FileStore/tables/employee.csv' ); 

```

Location of the data could be changed to S3 location.

.. figure:: ../../_assets/configuration/databricks-create-table.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   


Running SQL
+++++++++++

statement: ``` select count(*) as cunt  from employee; ```

.. figure:: ../../_assets/configuration/sql-statement1.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   


Sample Data:
++++++++++++

statement: ``` select * from employee;```
By default first 100 rows of data is displayed.

.. figure:: ../../_assets/configuration/sql-statement2.PNG
   :alt: Databricks
   :align: center
   :width: 60%
   
 
 
Drop Table
++++++++++

statement: ``` drop table employee;```

.. figure:: ../../_assets/configuration/sql-statement3.PNG
   :alt: Databricks
   :align: center
   :width: 60%

