Upload Stage
======================

- In upload stage we will first add column component and divide in two columns 

   .. figure:: ../../_assets/web-app/add-stage-uplaod-column.PNG
      :alt: web-app
      :width: 60%


- In first column add file component to choose files to upload to databricks. In this component in File tab in "STORAGE" select "Base64". Set its property name to ``file``.


   .. figure:: ../../_assets/web-app/add-stage-uplaod-file.PNG
      :alt: web-app
      :width: 60%


- In other column we will add one textfield to add "DESTINATION PATH" where the browse file should get uploaded. Set its label as ``Destination Path`` and property name to ``TRAIN_DATA``.

   .. figure:: ../../_assets/web-app/add-stage-uplaod-textfield.PNG
      :alt: web-app
      :width: 60%

- If we want the user to map the columns of the file uploaded, below are the steps for it

Add select boxes component to add the available column names. Set its label as ``Columns`` and make this component hidden by selecting ``hidden`` checkbox.

   .. figure:: ../../_assets/web-app/match-api-display.PNG
      :alt: web-app
      :width: 60%

Added default values where ``LABEL`` is ``DISPLAY NAME``, ``VALUE`` is ``ACTUAL COLUMN NAME`` and select that field which should be considered as required field. And don't     select this value ``CLEAR VALUE WHEN HIDDEN`` because we want default value when component is hidden.

   .. figure:: ../../_assets/web-app/match-api-data.PNG
      :alt: web-app
      :width: 60%

   .. figure:: ../../_assets/web-app/match-api.PNG
      :alt: web-app
      :width: 60%

- Add upload button and set action to ``event``. Set the button event name to ``upload``.

   .. figure:: ../../_assets/web-app/add-stage-uplaod-button1.PNG
      :alt: web-app
      :width: 60%


   .. figure:: ../../_assets/web-app/add-stage-uplaod-button2.PNG
      :alt: web-app
      :width: 60%
   

- Also add next button to go to next stage and perform actions depending upon event. Set the event name as ``next`` for the next button.

   .. figure:: ../../_assets/web-app/add-stage-next-button1.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../../_assets/web-app/add-stage-next-button2.PNG
      :alt: web-app
      :width: 60%
   

Click on "DONE" or "SAVE" to save added components for that stage
