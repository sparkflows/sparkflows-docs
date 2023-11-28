Run DDL Commands
===========================

Fire Insights allows you to run DDL commands on Databricks to perform various actions like:

  - Create New Databases
  - Create New Tables
  - View the schema of the tables
  - And much more

This document explains the essential steps required to run DDL Commands. 

Step 1 : Get Access to Run Commands
----------------

To be able to run DDL commands:

#. Hover the cursor over **DATA** and select **Databricks DB** from the drop-down menu. 
#. Click on **DDL**.

To get detailed information, read `Databricks Documentation. <https://docs.databricks.com/spark/latest/spark-sql/language-manual/create-table.html>`_


Step 2 : Run DDL Commands
----------------------

Below are few examples to run DDL:


Create Database
+++++++++++++++++

* DDL Statement::

    CREATE DATABASE finance; 
    
Create Table
++++++++++++++

* DDL Statement::

    CREATE TABLE `employee` (`id` INT, `name` STRING) USING com.databricks.spark.csv OPTIONS ( `multiLine` 'false', `escape` '"', `header` 'true', `delimiter` ',', path 'dbfs:/FileStore/tables/employee.csv' ); 

* DDL Statement::

    CREATE TABLE `housing` (`id` INT, `price` DOUBLE, `lotsize` INT, `bedrooms` INT, `bathrms` INT, `stories` INT, `driveway` STRING, `recroom` STRING, `fullbase` STRING, `gashw` STRING, `airco` STRING, `garagepl` STRING, `prefarea` STRING) USING com.databricks.spark.csv OPTIONS ( `multiLine` 'false', `escape` '"', `header` 'true', `delimiter` ',', path 'dbfs:/FileStore/sample-data/data/housing.csv' )

* DDL Statement::

    CREATE TABLE `bike_sharing_sample_dataset` (`datetime` STRING, `season` INT, `holiday` INT, `workingday` INT, `weather` INT, `temp` DOUBLE, `atemp` DOUBLE, `humidity` INT, `windspeed` DOUBLE, `casual` INT, `registered` INT, `count` INT) USING com.databricks.spark.csv OPTIONS ( `multiLine` 'false', `escape` '"', `header` 'true', `delimiter` ',', path 'dbfs:/FileStore/sample-data/bike_sharing_sample_dataset.csv' )

Change Data Location
+++++++++

* Location of the data could be changed to S3 location.

  .. figure:: ../../_assets/configuration/databricks-create-table.PNG
     :alt: Databricks
     :width: 60%
   
Run SQL
+++++++++++

* Select SQL Statement::

      select count(*) as count  from employee;

  .. figure:: ../../_assets/configuration/sql-statement1.PNG
     :alt: Databricks
     :width: 60%
   


Sample Data:
++++++++++++

* Select SQL Statement::

    select * from employee;
    
  By default, the first 100 rows of data are displayed.

  .. figure:: ../../_assets/configuration/sql-statement2.PNG
     :alt: Databricks
     :width: 60%
   
Drop Table
++++++++++

* Drop Statement::

    drop table employee;

  .. figure:: ../../_assets/configuration/sql-statement3.PNG
     :alt: Databricks
     :width: 80%

