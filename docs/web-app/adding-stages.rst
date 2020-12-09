Adding Stages
=============

Click on "Add stages" button to add a new stage. Select stage type and enter the stage name.

  .. figure:: ../_assets/web-app/add-stage.PNG
      :alt: web-app
      :width: 60%


- You can rearrange the stages by dragging and dropping. 
- You can EDIT, VIEW and REMOVE stages.

Examples for adding various Stages
-----------------

1 : Upload Stage
++++++++++++++++

- In upload stage we will first add column component and divide in two columns 

   .. figure:: ../_assets/web-app/add-stage-uplaod-column.PNG
      :alt: web-app
      :width: 60%


- In first column add file component to choose files to upload to databricks. In this component in File tab in "STORAGE" select "Base64"

   .. figure:: ../_assets/web-app/add-stage-uplaod-file.PNG
      :alt: web-app
      :width: 60%


- In other column we will add one textfield to add "DESTINATION PATH" where the browse file should get uploaded. Set its property name to ``destinationPath``.

   .. figure:: ../_assets/web-app/add-stage-uplaod-textfield.PNG
      :alt: web-app
      :width: 60%


- Add upload button and set action to ``event``. Set the button event name to ``upload``.

   .. figure:: ../_assets/web-app/add-stage-uplaod-button1.PNG
      :alt: web-app
      :width: 60%


   .. figure:: ../_assets/web-app/add-stage-uplaod-button2.PNG
      :alt: web-app
      :width: 60%
   

- Also add next button to go to next stage and perform actions depending upon event. Set the event name as ``next`` for the next button.

   .. figure:: ../_assets/web-app/add-stage-next-button1.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../_assets/web-app/add-stage-next-button2.PNG
      :alt: web-app
      :width: 60%
   

Click on "DONE" or "SAVE" to save added components for that stage

2 : Parameters Stage
++++++++++++++++

- In parameters stage we can add ``select, text-field, select boxes, buttons`` etc components

For example: 

- First we will add column component and divide it in two columns  

- Then, lets add select boxes example in first column by adding select boxes component. In this component in Data tab add all possible values you want to add.

   .. figure:: ../_assets/web-app/add-stage-parameters-selectboxes.PNG
      :alt: web-app
      :width: 60%
   

-  Then, lets add select example in the second column by adding select component. In this component in Data tab add all possible values you want to add. 

   .. figure:: ../_assets/web-app/add-stage-parameters-select.PNG
     :alt: web-app
     :width: 60%
  

-  Now, lets add column component in the bottom and divide into two columns for adding back and next button.

-  Add back button in first column to go to back stage and perform actions depending upon event, where we will add event name as ``back``.

   .. figure:: ../_assets/web-app/add-stage-parameters-back.PNG
      :alt: web-app
      :width: 60%
   

-  Add next button in second column to go to next stage and perform actions depending upon event.  Set its event name as ``next``. We can also add CUSTOM CSS CLASS like          ``float-right, float-left`` etc

   .. figure:: ../_assets/web-app/add-stage-parameters-next.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../_assets/web-app/add-stage-parameters-buttons.PNG
      :alt: web-app
      :width: 60%
   

Click on "DONE" or "SAVE" to save the added components for that stage.


3 : Run Stage
++++++++++++++++

- In run stage we will execute the notebook with all parameters added in the App.

- Let's first add title in page if needed with "html element" component like below.

   .. figure:: ../_assets/web-app/add-stage-run-title.PNG
      :alt: web-app
      :width: 60%
   

-  Now, lets add column component in the bottom and divide it into two columns for adding the ``back`` and ``run`` buttons.

-  Add back button in first column to go to back stage and perform actions depending upon event. Set its event name as ``back``.

-  Add next button in second column to go to next stage and perform actions depending upon event. Set its add event name as ``execute``. We can also can add CUSTOM CSS CLASS like          float-right, float-left etc

   .. figure:: ../_assets/web-app/add-stage-run-runbtn.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../_assets/web-app/add-stage-run-buttons.PNG
      :alt: web-app
      :width: 60%
   

Click on "DONE" or "SAVE" to save added components for that stage

