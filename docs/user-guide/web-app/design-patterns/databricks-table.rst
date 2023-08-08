Create a Dropdown with Databricks Tables
================

Fire Insights allows you to populate a dropdown menu with databricks tables in an Analytical App. 

This document explains in detail the steps required to map table columns in Analytical Apps.

Step 1: Add Tables Dropdown
---------------------

To load a list of tables in the select component, use the following steps:

#. Add a **select** component.
#. Add a **SQL query** in **Custom Properties** under **API** tab. 

   Set the **Key** as **query** and the **Value** as **show tables in $database;**. 

   Here, *database* in *$database* refers to the property name of another component. 

   When the user selects a database, this select option will be populated.

   .. figure:: ../../../_assets/web-app/map-table-columns/SelectTB1.png
      :alt: web-app
      :width: 70%

`Click here <https://docs.sparkflows.io/en/latest/user-guide/web-app/map-table-columns.html>`_ for more detailed information.
