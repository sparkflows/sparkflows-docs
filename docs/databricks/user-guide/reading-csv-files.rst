Read CSV Files
=================================

There are multiple ways to read and process CSV files in Fire Insights.

* Use Read CSV node in the workflow for reading the CSV file from DBFS.
* Create an unmanaged Databricks Table on the CSV file. Then, use the Read Databricks Table node in the workflow.
* Create a dataset in Fire Insights on the CSV file in DBFS. Then, use that Dataset in a workflow.


Use of Read CSV Node
-------------------

The workflow  given below has a Read CSV node which reads CSV files from DBFS and processes them.

The path of the file can either be the CSV file itself, or it can be a folder containing many CSV files of the same schema.

.. figure:: ../../_assets/databricks/csv_file.PNG
   :alt: Databricks
   :width: 60%

Create an unmanaged Databricks Table on the CSV File
---------------

The command given below shows an example of creating an unmanaged Databricks Table on the CSV file.

::

    CREATE TABLE `housing` ( `id` INT, `price` DOUBLE, `lotsize` INT, `bedrooms` INT, `bathrms` INT, `stories` INT, `driveway` STRING, `recroom` STRING, `fullbase` STRING, `gashw` STRING, `airco` STRING, `garagepl` STRING, `prefarea` STRING) USING com.databricks.spark.csv OPTIONS ( `multiLine` 'false', `escape` '"', `header` 'true', `delimiter` ',', path 'dbfs:/FileStore/sample-data/data/housing.csv' ) 

The workflow given below uses the Read Databricks Table Node to read in the data from the Databricks table created above.

.. figure:: ../../_assets/databricks/databrick_table.PNG
   :alt: Databricks
   :width: 60%


Create a Dataset in Fire Insights on the CSV File
-------------

Fire Insights supports the concept of Datasets. Dataset is the definition of the data it represents. This way the Dataset can be defined just once and used in multiple workflows.

Below is the creation of a Dataset on a CSV file.

.. figure:: ../../_assets/databricks/data.PNG
   :alt: Databricks
   :width: 60%

The workflow given below shows the usage of the Dataset created previously.

  
.. figure:: ../../_assets/databricks/dataset.PNG
   :alt: Databricks
   :width: 60%   


