Creating Analytics App
======================

Fire Insights enables you to create Analytics Apps.

Below is the process for creating a new Analytics App.

- *Go to APPLICATIONS / ANALYTICS APPS*
- *Click on "Create Analytics App"*
- *Add mandatory fields i.e. "Name", "select notebook"*
- *Click on add stage button to add different stages*
- *Click "Save" Or "Publish"*

Go to Analytics Apps
--------------------

When you go to ANALYTICS APPS under APPLICATIONS all existing analytics app are displayed. Where you can EDIT, VIEW and DELETE existing analytics app.

   .. figure:: ../_assets/web-app/list.PNG
      :alt: web-app
      :width: 60%


Click on Create Analytics App
-------------------------

Fill in the required fields as below.

- *Name* : Name of the new analytics app 
- *category* : Category of the new analytics app
- *Description* : Description of the new analytics app
- *Execution Type:* : Select execution type i.e notebook and select notebook from the available notebook list

   .. figure:: ../_assets/web-app/create.PNG
      :alt: web-app
      :width: 60%


"Save" or "Publish" the analytics app before adding stages.

Now, click on "Add stages" button to add different stages. Select stage type and add stage name.

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


- In other column We will add one textfield to add "DESTINATION PATH" where the browse file should get uploaded whose property name will be "destinationPath".

   .. figure:: ../_assets/web-app/add-stage-uplaod-textfield.PNG
      :alt: web-app
      :width: 60%


- And add upload button and perform actions depending upon event, where we will add event name as upload.

   .. figure:: ../_assets/web-app/add-stage-uplaod-button1.PNG
      :alt: web-app
      :width: 60%


   .. figure:: ../_assets/web-app/add-stage-uplaod-button2.PNG
      :alt: web-app
      :width: 60%
   

- And also can add next button to go to next stage and perform actions depending upon event, where we will add event name as "next".

   .. figure:: ../_assets/web-app/add-stage-next-button1.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../_assets/web-app/add-stage-next-button2.PNG
      :alt: web-app
      :width: 60%
   

Click on "Done" or "Save" to save added components for that stage

2 : Parameters Stage
++++++++++++++++

- In parameters stage we can add select,text-field,select boxes,buttons , etc components

For example: 
- First we will add column component and divide in two columns  

- Then, let's add select boxes example in first column by adding select boxes component. In this component in Data tab add all possible values you want to add.

   .. figure:: ../_assets/web-app/add-stage-parameters-selectboxes.PNG
      :alt: web-app
      :width: 60%
   

-  Then, let's add select example with in second column by adding select component. In this component in Data tab add all possible values you want to add. 

   .. figure:: ../_assets/web-app/add-stage-parameters-select.PNG
     :alt: web-app
     :width: 60%
  

-  Then, let's add column component in the bottom and divide in two columns for adding back and next button.

-  Add back button in first column to go to back stage and perform actions depending upon event, where we will add event name as "back".

   .. figure:: ../_assets/web-app/add-stage-parameters-back.PNG
      :alt: web-app
      :width: 60%
   

-  Add next button in second column to go to next stage and perform actions depending upon event, where we will add event name as "next". Also can add CUSTOM CSS CLASS like          float-right, float-left etc

   .. figure:: ../_assets/web-app/add-stage-parameters-next.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../_assets/web-app/add-stage-parameters-buttons.PNG
      :alt: web-app
      :width: 60%
   

Click on "Done" or "Save" to save added components for that stage

3 : Run Stage
++++++++++++++++

- In run stage we will execute the notebook with all parameters added in app

- Let's first add title in page if needed with "html element" component like below

   .. figure:: ../_assets/web-app/add-stage-run-title.PNG
      :alt: web-app
      :width: 60%
   

-  Then, let's add column component in the bottom and divide in two columns for adding back and run button.

-  Add back button in first column to go to back stage and perform actions depending upon event, where we will add event name as "back".

-  Add next button in second column to go to next stage and perform actions depending upon event, where we will add event name as "execute". Also can add CUSTOM CSS CLASS like          float-right, float-left etc

   .. figure:: ../_assets/web-app/add-stage-run-runbtn.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../_assets/web-app/add-stage-run-buttons.PNG
      :alt: web-app
      :width: 60%
   

Click on "Done" or "Save" to save added components for that stage

