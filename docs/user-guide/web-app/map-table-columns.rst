Map Table Columns
=======================

Designing
------------------

- Add select component to load database list in selected databricks connection. Set its property name as `fld_db`. 

   .. figure:: ../../_assets/web-app/map-table-columns/select-db.PNG
        :alt: web-app
        :width: 80%

- Add select component to load tables list in selected database. Set its property name as `fld_table`. 

   .. figure:: ../../_assets/web-app/map-table-columns/select-tbl.PNG
        :alt: web-app
        :width: 80%

- Add textarea component to run added query. Set its label and make this component hidden by selecting the ``hidden`` checkbox.

   .. figure:: ../../_assets/web-app/map-table-columns/query-hidden.PNG
        :alt: web-app
        :width: 80%

- Add default value of query. Query can be parameterised or can't be ex: `select * from $fld_db.$fld_table limit 10;`. Don't select this value ``CLEAR VALUE WHEN HIDDEN`` because we want the default value when the component is hidden. Set its property name as `query`. 

   .. figure:: ../../_assets/web-app/map-table-columns/query-default-value.PNG
        :alt: web-app
        :width: 80%

  .. figure:: ../../_assets/web-app/map-table-columns/query-key.PNG
          :alt: web-app
          :width: 80%

- Add Match fields button and set the action to ``event``. Set the button event name to ``matchFields``.

   .. figure:: ../../_assets/web-app/map-table-columns/matchFields-btn.PNG
           :alt: web-app
           :width: 80%

- If we want the user to map the columns after running query below are steps : 

- Add select boxes component to add the available column names. Set its label as ``Columns`` and make this component hidden by selecting the ``hidden`` checkbox.

   .. figure:: ../../_assets/web-app/match-api-display.PNG
      :alt: web-app
      :width: 80%

- Added default values where ``LABEL`` is ``DISPLAY NAME``, ``VALUE`` is ``ACTUAL COLUMN NAME`` and select that field which should be considered as a required field. And don't select this value ``CLEAR VALUE WHEN HIDDEN`` because we want the default value when the component is hidden.

   .. figure:: ../../_assets/web-app/match-api-data.PNG
      :alt: web-app
      :width: 80%

   .. figure:: ../../_assets/web-app/match-api.PNG
      :alt: web-app
      :width: 80%

- Add upload button and set the action to ``event``. Set the button event name to ``upload``.

   .. figure:: ../../_assets/web-app/add-stage-uplaod-button1.PNG
      :alt: web-app
      :width: 80%


   .. figure:: ../../_assets/web-app/add-stage-uplaod-button2.PNG
      :alt: web-app
      :width: 80%
   

- Also, add the next button to go to the next stage and perform actions depending upon the event. Set the event name as ``next`` for the next button.

   .. figure:: ../../_assets/web-app/add-stage-next-button1.PNG
      :alt: web-app
      :width: 80%
   

   .. figure:: ../../_assets/web-app/add-stage-next-button2.PNG
      :alt: web-app
      :width: 80%


Running app
------------------

- If any stage has databricks database component added the it will load database list present in slected connection.
- On selecting database , tables list will load for selected db and connection.

   .. figure:: ../../_assets/web-app/map-table-columns/run-app1.PNG
      :alt: web-app
      :width: 80%

- On clicking `Match fields` button dialog shows up data after running the added query while designing app.

   .. figure:: ../../_assets/web-app/map-table-columns/run-app2.PNG
      :alt: web-app
      :width: 80%
