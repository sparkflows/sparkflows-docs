Analytics App Reference Guide
=======================

.. list-table:: Upload Stage
   :widths: 25 25 25 25
   :header-rows: 1

   * - Title
     - Component Type
     - Property Name 
     - Description
   * - File
     - file
     - file
     - Component is added to choose files to upload to databricks
   * - Destination Path
     - text field
     - TRAIN_DATA
     - Component is added to get destination path where the browse file should get uploaded.
   * - Columns
     - select boxes
     - any 
     - Component is added if user want to map the columns of the file uploaded.

.. list-table:: Buttons
   :widths: 25 25 25 25
   :header-rows: 1

   * - Title
     - Component Type
     - Event Name
     - Property Name 
   * - Back
     - Button
     - back
     - back
   * - Next
     - Button
     - next
     - next     
   * - Run
     - Button
     - execute
     - run
   * - Upload
     - Button
     - upload 
     - upload
   * - Map Fields
     - Button
     - mapFields 
     - mapFields
     
     
.. list-table:: Map Table Columns
   :widths: 30 30 40
   :header-rows: 1

   * - Title
     - Component Type
     - Property Name 
   * - Database Dropdown
     - select
     - fld_db
   * - Table Dropdown
     - select
     - fld_table            
