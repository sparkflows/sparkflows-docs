Analytical App Reference Guide
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
   * - Summarize/Translate
     - Button
     - gen-ai
     - any
     - Component is added to call open ai rest API.
   * - Read File
     - Button
     - read-file
     - any
     - Component is added to read the local file and update content in any components.
   * - Download
     - Button
     - export-text
     - any
     - Component is added to download the content of any components as a txt file.
   * - Show Difference
     - Button
     - text-diff
     - any
     - Component is added to show the difference between two component content.
   * - Translate
     - Button
     - execute-node
     - any
     - Component is added to execute a single node and perform certain tasks based on the execution result.
     
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
     - Component is added to get the destination path where the browse file should get uploaded.
   * - Upload
     - Button
     - KEY : for , VALUE : file1(property name of file component);
     - Component is added to upload the chosen file to databricks in a specified destination path otherwise by default it will be stored inside the FileStore folder.
   * - Columns
     -  Select Boxes
     - KEY : for , VALUE : file1(property name of file component);
     - Component is added to map fields.

Upload File with Read Content and Execute App Options
-------------
.. list-table:: 
   :widths: 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Custom Properties 
     - Description
   * - File
     - File
     - file
     - Component is added to browse and select files.
   * - Destination Path
     - Text Field
     - any
     - Component is added to set destination path where the selected file should get uploaded.
   * - Upload
     - Button
     - KEY: readFile, VALUE: true(It will keep content after upload file); KEY: updateTo, VALUE: component property name(It will update given component with uploaded file content); KEY: execute, VALUE: true (It will allow to execute relevant workflow after upload file).
     - Component is added to upload the selected file to hdfs/dbfs in the specified destination path otherwise by default it will be stored inside the FileStore folder. We can assign custom properties to perform certain tasks after file upload.

Download Text Area or Text Field Content as Text File
-------------
.. list-table:: 
   :widths: 15 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Event Name
     - Custom Properties 
     - Description
   * - Download
     - Button
     - export-text
     - KEY: exportFrom, VALUE: component property name (It will save given component content into a text file).
     - Component is added to download the content of any components as a txt file.
