Mapping Table Columns
=======================

Adding Database Dropdown
------------------

- Add select component to load data depending upon added query and selected databricks connection. Add sql query in CUSTOM PROPERTIES where KEY will be `query` and VALUE as sql query ex: To load databases add query as `show databases;`.

   .. figure:: ../../_assets/web-app/map-table-columns/select-db.PNG
        :alt: web-app
        :width: 80%

Adding Tables Dropdown
---------------------

- Load tables list data in select component by adding sql query in CUSTOM PROPERTIES where KEY will be `query` and VALUE as `show tables in $database$;`. Here, `database` in `$database` is property name of some other component. When user select database then, this select option gets load.

   .. figure:: ../../_assets/web-app/map-table-columns/select-tbl.PNG
        :alt: web-app
        :width: 80%

Adding dropdown with values
-------------------------

- Add select component to load values in dropdown by adding CUSTOM PROPERTIES where KEY will be `query` and VALUE as `select * from $database$.$table$ limit 10;`. Here, `database` and `table` in `$database$.$table$` is property name of some other component. When database and table is selected then, this select component gets loaded where, first column is treated as the value to be returned and Second column is the display name if the second column is present.

   .. figure:: ../../_assets/web-app/map-table-columns/select.PNG
        :alt: web-app
        :width: 80%

Adding Map Fields Button
-----------------------

- Add Map fields button and set the action to ``event``. Set the button event name to ``mapFields``.

   .. figure:: ../../_assets/web-app/map-table-columns/mapFields-btn1.PNG
           :alt: web-app
           :width: 80%
           
- Set its property name as `mapFields`. Add sql query in CUSTOM PROPERTIES where KEY will be `query` and VALUE as sql query ex: `select * from $database$.$table$ limit 10;`.   

   .. figure:: ../../_assets/web-app/map-table-columns/mapFields-btn2.PNG
        :alt: web-app
        :width: 80%


- To map the columns after running map fields button query below are steps : 

- Add select boxes component to add the available column names. Set its label as ``Columns`` and make this component hidden by selecting the ``hidden`` checkbox.

   .. figure:: ../../_assets/web-app/match-api-display.PNG
      :alt: web-app
      :width: 80%

- Added default values where ``LABEL`` is ``DISPLAY NAME``, ``VALUE`` is ``ACTUAL COLUMN NAME`` and select that field which should be considered as a required field. And don't select this value ``CLEAR VALUE WHEN HIDDEN`` because we want the default value when the component is hidden.

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

- If any stage has databricks database component added the it will load database list present in slected connection.
- On selecting database , tables list will load for selected database and connection.

   .. figure:: ../../_assets/web-app/map-table-columns/run-app1.PNG
      :alt: web-app
      :width: 80%

- On clicking `Map fields` button dialog shows up data after running the added query while designing app.

   .. figure:: ../../_assets/web-app/map-table-columns/run-app2.PNG
      :alt: web-app
      :width: 80%
