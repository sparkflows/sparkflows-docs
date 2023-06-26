Run Stage
=======

The run stage is a critical component of Analytical App, allowing you to execute your workflows or notebook with all the necessary parameters seamlessly. 

This document provides a step-by-step guide on how to add a title to a page, create a column component for the back and run buttons, customize their events and appearance, and save the components for the run stage.


Below are the steps required to add a Run Stage.

Step 1 : Add Run Stage
-------

#. Go to Edit Analytics App Page.
#. Click the **Plus Icon** to add the stage.

   .. figure:: ../../../_assets/web-app/run-stage/add-stage.png
      :alt: web-app
      :width: 65%
    
#. In the **Add Stage dialog box**:
    
   Select the **stage type** as **Run** from the drop-down list.
   
   Enter the desired **name**.
   
   .. figure:: ../../../_assets/web-app/run-stage/stage-type.png
      :alt: web-app
      :width: 50% 

   Click **Add** to add the stage.

   .. figure:: ../../../_assets/web-app/run-stage/save-stage.png
      :alt: web-app
      :width: 65% 


Step 2 : Go to Edit Stage Page
---------

#. Click the **pencil icon** located next to stage name.

   .. figure:: ../../../_assets/web-app/run-stage/edit-stage.png
      :alt: web-app
      :width: 65% 

Step 3 : Add HTML Element
------------

HTML Element is needed to add **title** on the page. 

**Note:** You can choose to skip adding title as it is not mandatory.

To add the element :

#. Expand **General** tab on the Edit Stage Page.
#. Drag and drop the **HTML Element** on the RHS.

   .. figure:: ../../../_assets/web-app/run-stage/drag-html.png
      :alt: web-app
      :width: 65% 

#. Enter the required fields on the HTML component window as below :

   Set the **HTML TAG** to **h3**. 
   
   Set the **CSS CLASS** to **page-ltitle mb3**.

   Enter the **title text** in **CONTENT** field e.g. Execute & Result.

   
   .. figure:: ../../../_assets/web-app/run-stage/html-fields.png
      :alt: web-app
      :width: 65% 

#. Click **Save** to save the HTML component settings.

   .. figure:: ../../../_assets/web-app/run-stage/save-html.png
      :alt: web-app
      :width: 65% 



Step 4 : Add Column Component
------------

#. Expand **Layout** tab on the Edit Stage page.
#. Drag and Drop the **Columns** component at the bottom.

   .. figure:: ../../../_assets/web-app/run-stage/drag-column.png
      :alt: web-app
      :width: 65% 

#. Click **Save** on the Columns Component window to save the settings.
  
   .. figure:: ../../../_assets/web-app/run-stage/save-column.png
      :alt: web-app
      :width: 65% 


Step 5 : Add Back Button Component
----------

The Back button component is essential for navigating to the previous stage and executing actions based on the event.

To add the component :

#. Expand the **General** tab on the Edit Stage Page.
#. Drag and drop the **Button** component in the left column created in step 4.

   .. figure:: ../../../_assets/web-app/run-stage/drag-back-button.png
      :alt: web-app
      :width: 65% 

#. On the Button Component window, set the required fields as below :

   Enter the **label** name as **Back**. 
   
   Set the **action** to **Event**.
  
   Enter the **button event** as **back**.

   .. figure:: ../../../_assets/web-app/run-stage/back-component.png
      :alt: web-app
      :width: 65% 

#. Click **Save** to save the component settings.

   .. figure:: ../../../_assets/web-app/run-stage/save-back.png
      :alt: web-app
      :width: 65% 

Step 6 : Add Run Button Component
----------

The Run button is necessary for advancing to the next stage and performing actions based on the event.

To add the component :

#. Expand the **General** tab on the Edit Stage Page.
#. Drag and drop the **Button** component in the right column created in step 4.

   .. figure:: ../../../_assets/web-app/run-stage/drag-run-button.png
      :alt: web-app
      :width: 65% 

#. On the Button Component window, set the required fields as below :

   Enter the **label** name as **Run**. 
   
   Set the **action** to **Event**.
  
   Enter the **button event** as **run**.
   
   Enter the **Custom CSS Class** as **float-right** to display it on the RHS.

   .. figure:: ../../../_assets/web-app/run-stage/run-component.png
      :alt: web-app
      :width: 65% 

   .. figure:: ../../../_assets/web-app/run-stage/run-css.png
      :alt: web-app
      :width: 65% 

#. Click **Save** to save the component settings.

   .. figure:: ../../../_assets/web-app/run-stage/save-run.png
      :alt: web-app
      :width: 65% 

Step 7 : Save the Stage 
----------

#. Click **Save** on the Edit Stage Page to save the stage settings.

   
