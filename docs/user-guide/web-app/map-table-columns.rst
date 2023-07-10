Mapping Table Columns
=======================

Fire Insights allows you to map the columns of a table to updated names. This mapping is then sent as parameters to the Notebook or Workflow during execution.

This document explains in detail the steps required to map table columns in Analytical Apps.

Step 1 : Add Database Dropdown
------------------

To load data based on the added query and selected Databricks connection, follow these steps:

#. Add a **select** component.
#. Specify the **SQL query** in **Custom Properties** under **API** tab.
  
   Set the **Key** as **query** and the **Value** can be a **SQL query**. 
   
   For example, to load databases, the query can be **show databases;**.

   .. figure:: ../../_assets/web-app/map-table-columns/SelectDB.png
      :alt: web-app
      :width: 70%

Step 2 : Add Tables Dropdown
---------------------

To load a list of tables in the select component, use the following steps:

#. Add a **select** component.
#. Add a **SQL query** in **Custom Properties** under **API** tab. 

   Set the **Key** as **query** and the **Value** as **show tables in $database;**. 

   Here, *database* in *$database* refers to the property name of another component. 

   When the user selects a database, this select option will be populated.

   .. figure:: ../../_assets/web-app/map-table-columns/SelectTB1.png
      :alt: web-app
      :width: 70%

Step 3 : Add Dropdown with Values
-------------------------
To load values in the dropdown, follow these steps:

#. Add a **select** component.
#. Specify the **SQL query** in **Custom Properties** under **API** tab, where the **Key** will be **query** and the VALUE can be **select * from $database.$table limit 10;**. 

   Here, *database* and *table* in *$database.$table* refer to the property names of other components. 

   When the database and table are selected, this select component will be populated. 
   
   The first column is considered as the value to be returned, and the second column is used as the display name if present. 

   By default, it fetches 50 rows of data unless a limit is specified in the select query.
   
   **Note:** Query Examples can be :
   
   * select * from development.housing_csv limit 10;
   * select distinct(price) as price1 from development.housing_csv limit 10;

   .. figure:: ../../_assets/web-app/map-table-columns/Select.png
      :alt: web-app
      :width: 70%

Step 4 : Add Map Fields Button
-----------------------

The Map Fields Button allows users to map the fields of the table to new names. Follow these steps:

#. Add a **Map Fields button** and set its **action** to **event**.
#. Set the **button event name** as **mapFields**.
#. Set its **property name** as **mapFields**.

   .. figure:: ../../_assets/web-app/map-table-columns/MapFields1.png
      :alt: web-app
      :width: 70%

#. Add a **SQL query** in **Custom Properties** under **API** tab.
   
   Set the **Key** as **query** and the **Value** can be a SQL query such as **select * from $database.$table limit 10;**. 

   By default, it fetches 50 rows of data unless a limit is specified in the select query.

   .. figure:: ../../_assets/web-app/map-table-columns/MapFields2.png
      :alt: web-app
      :width: 70%
           
#. Add **select box** components to display the available column names.
   
   Set the **label** as **Columns** and hide this component by selecting the **hidden checkbox**.

   .. figure:: ../../_assets/web-app/map-table-columns/SelectBox1.png
      :alt: web-app
      :width: 70%

#. Add default values where the **label** is the **display name**, **value** is the **actual column name**, and select the field that should be considered as a required field. 

   **Note:** Do not select the **Clear Value When Hidden** checkbox, as we want the default value when the component is hidden.

   .. figure:: ../../_assets/web-app/map-table-columns/SelectBox2.png
      :alt: web-app
      :width: 70%


Step 5 : Add Next Button
------------------

#. Add the **next** button component and make it **disabled** by selecting the **disabled checkbox**.


   .. figure:: ../../_assets/web-app/map-table-columns/ButtonDisable.png
      :alt: web-app
      :width: 70%
        

Step 6 : Run the App
------------------

#. If any stage has the databricks database component added then it will load the database list present in the selected connection.

   On selecting the database, tables list will get loaded for selected database and connection.

   .. figure:: ../../_assets/web-app/map-table-columns/RunApp1.png
      :alt: web-app
      :width: 70%

#. On clicking **Map Fields** button the dialog shows up with data after running the query associated with the button.

   .. figure:: ../../_assets/web-app/map-table-columns/RunApp2.png
      :alt: web-app
      :width: 70%
