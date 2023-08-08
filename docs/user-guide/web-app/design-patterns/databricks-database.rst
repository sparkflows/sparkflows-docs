Create a Dropdown with Databricks Databases
===============

Fire Insights allows you to populate a dropdown menu with databases in an Anlayitical App. This document explains in detail the steps required to populate dropdown with table columns in Analytical Apps.

Step 1 : Add Database Dropdown
------------------

To load data based on the added query and selected Databricks connection, follow these steps:

#. Add a **select** component.
#. Specify the **SQL query** in **Custom Properties** under **API** tab.
  
   Set the **Key** as **query** and the **Value** can be a **SQL query**. 
   
   For example, to load databases, the query can be **show databases;**.

   .. figure:: ../../../_assets/web-app/map-table-columns/SelectDB.png
      :alt: web-app
      :width: 70%
