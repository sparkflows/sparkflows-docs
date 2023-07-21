Analytics App Reference Guide
=======================

Upload Stage
--------

.. list-table:: 
   :widths: 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Property Name 
     - Description
   * - File
     - File
     - file
     - Component is added to choose files to upload to databricks.
   * - Destination Path
     - Text Field
     - any
     - Component is added to get destination path where the browse file should get uploaded.
   * - Columns
     - Select Boxes
     - any 
     - Component is added if user want to map the columns of the file uploaded.


Buttons
---------
.. list-table::
   :widths: 15 15 18 18 28
   :header-rows: 1

   * - Title
     - Component Type
     - Event Name
     - Property Name
     - Description
   * - Back
     - Button
     - back
     - back
     - Component is added to go to the previous stage.
   * - Next
     - Button
     - next
     - next
     - Component is added to go to the next stage.
   * - Run
     - Button
     - execute
     - run
     - Component is added to run app with selected parameters.
   * - Upload
     - Button
     - upload 
     - upload
     - Component is added to upload choose file to databricks in specified destination path otherwise by default it will store inside FileStore folder.
   * - Map Fields
     - Button
     - mapFields 
     - mapFields
     - Component is added to map fields.
   * - Next Tab
     - Button
     - nextTab
     - any
     - Component is added to go to the next tab.
   * - Back Tab
     - Button
     - backTab
     - any
     - Component is added to go to the previous tab.
   * - Browse
     - Button
     - browse
     - any
     - Component is added to browse to the HDFS file system.
   * - Upload Data
     - Button
     - uploadData
     - uploadData
     - Component is added to upload table data to the HDFS file system.
     
Mapping Table Columns
----------
.. list-table:: 
   :widths: 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Custom Properties
     - Description
   * - Database Dropdown
     - Select
     - KEY : query , VALUE : show databases;
     - Component is added to load database list in selected databricks connection.
   * - Table Dropdown
     - Select
     - KEY : query , VALUE : show tables in $database; (Database value is taken from other component having key database.)
     - Component is added to load tables list in selected database and databricks connection.
   * - Map Fields
     - Button
     - KEY : query , VALUE : select * from $database.$table limit 10; (Database and table value is taken from other component having key database and table.)
     - Component is added for mapping table columns.
     

Multiple File Upload
-------------
.. list-table:: 
   :widths: 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Custom Properties
     - Description
   * - Destination Path
     - Textfield
     - KEY : for , VALUE : file1(property name of file component);
     - Component is added to get destination path where the browse file should get uploaded.
   * - Upload
     - Button
     - KEY : for , VALUE : file1(property name of file component);
     - Component is added to upload choose file to databricks in specified destination path otherwise by default it will store inside FileStore folder.
   * - Columns
     -  Select Boxes
     - KEY : for , VALUE : file1(property name of file component);
     - Component is added to map fields.
