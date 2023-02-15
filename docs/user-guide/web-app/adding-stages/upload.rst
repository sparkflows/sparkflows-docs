Upload Stage
======================

- In the upload stage, add a column component and then divide it into two columns.

   .. figure:: ../../../_assets/web-app/add-stage-uplaod-column.PNG
      :alt: web-app
      :width: 65%


- In the first column add a file component to choose files to upload to databricks. In this component, in the File tab in "STORAGE" select "Base64". Set its property name to ``file``.


   .. figure:: ../../../_assets/web-app/add-stage-uplaod-file.PNG
      :alt: web-app
      :width: 65%


- In the second column, add a text field to add "DESTINATION PATH" where the browse file should get uploaded. Set its label as ``Destination Path`` and property name to ``TRAIN_DATA``.

   .. figure:: ../../../_assets/web-app/add-stage-uplaod-textfield.PNG
      :alt: web-app
      :width: 65%

- Below are the steps to follow in case you want to map the columns of the file uploaded in the previous step.

Add select boxes component to add the available column names. Set its label as ``Columns`` and make this component hidden by selecting the ``HIDDEN`` checkbox.

   .. figure:: ../../../_assets/web-app/match-api-display.PNG
      :alt: web-app
      :width: 65%

Add default values where ``LABEL`` is ``DISPLAY NAME``, ``VALUE`` is ``ACTUAL COLUMN NAME`` and select the field which should be considered as a required field. Note:  don't select ``CLEAR VALUE WHEN HIDDEN`` checkbox as only the default values are needed when the component is chosen to be hidden.

.. figure:: ../../../_assets/web-app/match-api-data.PNG
   :alt: web-app
   :width: 65%

.. figure:: ../../../_assets/web-app/match-api.PNG
   :alt: web-app
   :width: 65%

- Add upload button and set the action to ``EVENT``. Set the button event name to ``UPLOAD``.

.. figure:: ../../../_assets/web-app/add-stage-uplaod-button1.PNG
   :alt: web-app
   :width: 65%


.. figure:: ../../../_assets/web-app/add-stage-uplaod-button2.PNG
   :alt: web-app
   :width: 65%
   

- Also, add the next button to go to the next stage and perform actions depending upon the event. Set the event name as ``next`` for the next button.

.. figure:: ../../../_assets/web-app/add-stage-next-button1.PNG
   :alt: web-app
   :width: 65%
   

.. figure:: ../../../_assets/web-app/add-stage-next-button2.PNG
   :alt: web-app
   :width: 65%
   

Click on ``DONE`` or ``SAVE`` to save added components for that stage.
