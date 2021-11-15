Mapping Table Columns
=======================

Fire Insights enables to map the columns of a Table to updated names. This mapping is then sent over as parameters to the Notebook or Workflow during execution.

Adding Database Dropdown
------------------

- Add select component to load data depending upon added query and selected databricks connection. Add sql query in CUSTOM PROPERTIES where KEY will be `query` and VALUE would be an sql query. For example to load databases the query can be `show databases;`.

   .. figure:: ../../_assets/web-app/map-table-columns/select-db.PNG
        :alt: web-app
        :width: 80%

Adding Tables Dropdown
---------------------

- Load tables list data in select component by adding sql query in CUSTOM PROPERTIES where KEY will be `query` and VALUE can be `show tables in $database;`. Here, `database` in `$database` is property name of some other component. When user selects the database then this select option gets loaded.

   .. figure:: ../../_assets/web-app/map-table-columns/select-tbl.PNG
        :alt: web-app
        :width: 80%

Adding dropdown with values
-------------------------

- Add select component to load values in dropdown by adding CUSTOM PROPERTIES where KEY will be `query` and VALUE can be `select * from $database.$table limit 10;`. Here, `database` and `table` in `$database$.$table$` is property name of some other component. When database and table is selected then, this select component gets loaded where, first column is treated as the value to be returned and Second column is the display name if the second column is present. If limit is not added in select query by default it will fetch 50 rows data. 
- Query example : 
                   1. select * from development.housing_csv limit 10;
                   2. select distinct(price) as price1 from development.housing_csv limit 10;

   .. figure:: ../../_assets/web-app/map-table-columns/select.PNG
        :alt: web-app
        :width: 80%

Adding Map Fields Button
-----------------------

The Map Fields Button enables the user to map the fields of the table to new names.

- Add Map fields button and set the action to ``event``. Set the button event name to ``mapFields``.

   .. figure:: ../../_assets/web-app/map-table-columns/mapFields-btn1.PNG
           :alt: web-app
           :width: 80%
           
- Set its property name as `mapFields`. Add sql query in CUSTOM PROPERTIES where KEY will be `query` and VALUE as sql query ex: `select * from $database.$table limit 10;`. If limit is not added in select query by default it will fetch 50 rows data.   

   .. figure:: ../../_assets/web-app/map-table-columns/mapFields-btn2.PNG
        :alt: web-app
        :width: 80%


In order to map the columns to the new names, add select boxes component to provide the mapping names for the user to choose from.

- Add select boxes component to add the available column names. Set its label as ``Columns`` and make this component hidden by selecting the ``hidden`` checkbox.

   .. figure:: ../../_assets/web-app/match-api-display.PNG
      :alt: web-app
      :width: 80%

- Add default values where ``LABEL`` is ``DISPLAY NAME``, ``VALUE`` is ``ACTUAL COLUMN NAME`` and select that field which should be considered as a required field. And don't select this value ``CLEAR VALUE WHEN HIDDEN`` because we want the default value when the component is hidden.

   .. figure:: ../../_assets/web-app/match-api-data.PNG
      :alt: web-app
      :width: 80%

Adding Next Button
------------------

- Add the next button and make this component disabled by selecting the ``disabled`` checkbox.

   .. figure:: ../../_assets/web-app/map-table-columns/next-disable.PNG
        :alt: web-app
        :width: 80%
        


Running app
------------------

- If any stage has the databricks database component added then it will load the database list present in the selected connection.
- On selecting the database, tables list will get loaded for selected database and connection.

   .. figure:: ../../_assets/web-app/map-table-columns/run-app1.PNG
      :alt: web-app
      :width: 80%

- On clicking `Map fields` button the dialog shows up with data after running the query associated with the button.

   .. figure:: ../../_assets/web-app/map-table-columns/run-app2.PNG
      :alt: web-app
      :width: 80%
