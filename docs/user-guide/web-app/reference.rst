Analytical App Reference Guide
=======================
This document outlines the components, properties, and functionalities available in the Analytical App, providing detailed reference for configuring file uploads, data mapping, navigation, and various interactive operations.

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
     - Component is added to upload chosen file to databricks in specified destination path otherwise by default it will be stored inside FileStore folder.
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
     - Component is added to download the content of any components as a .txt file.
   * - Show Difference
     - Button
     - text-diff
     - any
     - Component is added to show the difference between the contents of two components.
   * - Translate
     - Button
     - execute-node
     - any
     - Component is added to execute a single node and perform certain tasks based on the execution result.
   * - Cancel
     - Button
     - cancel
     - any
     - Component is added to cancel the current stage and go back to the previous page.
   * - Execute Query
     - Button
     - execute-query
     - any
     - Component is added to execute a database query and show result in table.
   * - Get Query Result
     - Button
     - get-query-result
     - any
     - Component is added to execute a database query and show result in table with support pagination.
   * - Save Record
     - Button
     - save-record
     - any
     - Component is added to insert or update a row in a database table from the form fields, without a workflow or custom code.
   * - Export DB Data
     - Button
     - export-db-data
     - any
     - Component is added to export database table data into an excel file. It is commonly used with `get-query-result` data.
   * - Expand
     - Button
     - expand
     - any
     - Component is added to expand a section or component.
   * - Modal Content
     - Button
     - modal-content
     - any
     - Component is added to display given component content into modal.
   * - View PDF
     - Button
     - viewPdf
     - any
     - Component is added to view selected file content. It can be text, CSV, HTML, image or PDF file.
   * - Refresh File
     - Button
     - refreshFile
     - any
     - Component is added to refresh or reload the file list.
   * - Get Dashboard
     - Button
     - get-dashboard
     - any
     - Component is added to retrieve and display a dashboard.
   * - Get Report
     - Button
     - get-report
     - any
     - Component is added to retrieve and display a report.
     
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
     - KEY: readFile, VALUE: true(It will keep content after upload file); KEY: updateTo, VALUE: component property name(It will update given component with uploaded file content); KEY: execute, VALUE: true (It will allow to execute relevant workflow after upload file);KEY: dirOverwrite, VALUE:true(It will delete all files/folders present in given destination path and then upload the file selected file).
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
     - Component is added to download the content of any components as a .txt file.

Save Form Data to Database Table
--------------------------------
.. list-table:: 
   :widths: 15 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Event Name
     - Custom Properties 
     - Description
   * - Save
     - Button
     - save-record
     - KEY: database, VALUE: database name; KEY: table, VALUE: table name; KEY: columnMap, VALUE: formKey:column pairs separated by comma (e.g. co_name:company_name,co_city:city) (Only the form fields listed here are saved and validated); KEY: mode, VALUE: insert or update (default insert); KEY: keyColumn, VALUE: column name (Row to update when mode is update, its value is taken from the mapped form field); KEY: constants, VALUE: column:value pairs (e.g. entity:LEAD) (Always saved with the row); KEY: defaults, VALUE: column:value pairs (e.g. status:Active,currency:INR) (Saved only when the mapped form field is empty); KEY: successMessage, VALUE: message shown after save; KEY: resultQuery, VALUE: select query (e.g. SELECT MAX(company_id) FROM CRM.crm_company) (First value of the result is added to the success message); KEY: clearOnSave, VALUE: true (It will reset the mapped form fields to their default values after save).
     - Component is added to save the form fields into a database table using the app's JDBC connection. Values are saved with a prepared statement, so quotes and special characters are stored as entered, and each value is converted to the column type. Empty fields are skipped on insert so the column default is used. Checkbox values are saved as true/false in text columns and 1/0 in numeric columns. Missing required fields and database errors are shown in an error dialog.

Editable Query Result Table
---------------------------
.. list-table:: 
   :widths: 15 15 15 23 30
   :header-rows: 1

   * - Title
     - Component Type
     - Event Name
     - Custom Properties 
     - Description
   * - Get Query Result
     - Button
     - get-query-result
     - KEY: selectColumns, VALUE: column names separated by comma (default all columns); KEY: columnMap, VALUE: column:Header pairs separated by comma (e.g. company_id:Company Id,company_name:Company Name) (It will set the table column headers); KEY: editable, VALUE: true (It will add edit, cancel and save icons to each row); KEY: primaryColumn, VALUE: key column name (It is read-only in the table and is used to find the row to update); KEY: idColumn, VALUE: key column name (It is used to pass the selected row to the next stage); KEY: hiddenColumns, VALUE: column names separated by comma (It will hide these columns); KEY: orderBy, VALUE: column name; KEY: orderType, VALUE: ASC or DESC (default DESC); KEY: tableTitle, VALUE: title shown above the table; KEY: tableSubtitle, VALUE: text shown below the title; KEY: recordSave, VALUE: true (It will save only the changed cells with a prepared statement and enable the save icon while the row is being edited); KEY: detailPopup, VALUE: false (It will show the primaryColumn value as plain text instead of a link to the details popup).
     - Component is added to execute a database query and show result in an editable table with pagination. The query uses the form fields with key database, table and filters (where condition). The table must be a database table (not a view) and selectColumns must be real column names to save the edited rows. Without recordSave the save icon is enabled after a cell is changed and the cell editing is completed (Enter, Tab or click on another cell).

