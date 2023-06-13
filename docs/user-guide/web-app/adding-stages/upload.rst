Upload Stage
========

Below are the steps required to add, edit or create an upload stage.


Step 1 : Open Edit Stage Page
---------

#. Click on the edit icon located next to the stage name.

   .. figure:: ../../../_assets/web-app/stage-upload/edit-stage.png
      :alt: web-app
      :width: 60%


Step 2 : Add Column Component
------------

#. On the Edit Analytics App page, expand the **Layout** tab.

#. Place the cusror on the **Columns** option and click to **drag and drop** it on the RHS.
   
   **Note:** Make sure to Drop the component right over the text in purple text box.
   
   .. figure:: ../../../_assets/web-app/stage-upload/drag-column.png
      :alt: web-app
      :width: 60%

#. On the columns component window, set the label and other settings as per your requirement.

   .. figure:: ../../../_assets/web-app/stage-upload/add-column.png
      :alt: web-app
      :width: 60%

   Click **Save** to save the layout.

   .. figure:: ../../../_assets/web-app/stage-upload/save-column.png
      :alt: web-app
      :width: 60%

Step 3 : Add File Component
-----------

Add file component to enable uploading of files. To add :

#. Expand the **General** tab.
#. Place the cursor on **File** option and click to drag and drop it in the first column.

   **Note:** Make sure to drop the component right over the purple-colored box in the first column.

   .. figure:: ../../../_assets/web-app/stage-upload/drag-file.png
      :alt: web-app
      :width: 60%

#. In the file component window, click **File** tab and :

   Select **Storage** as **Base64** from the drop-down menu.
   
   Enter the **File Name Template** as **file**.
   
   .. figure:: ../../../_assets/web-app/stage-upload/file-component.png
      :alt: web-app
      :width: 60%

   Click **Save** to save the component.

   .. figure:: ../../../_assets/web-app/stage-upload/save-file.png
      :alt: web-app
      :width: 60%

Step 4 : Add Text Field Component
---------

Add text field component in the **second column** to set the **destination path** where uploaded files will reside. To add :

#. Expand **General** tab.
#. Place the cursor on **Text Field** and click to drag and drop the component in the second column.

   **Note:** Make sure to drop the component right over the purple box in the second column.

   .. figure:: ../../../_assets/web-app/stage-upload/drag-text-field.png
      :alt: web-app
      :width: 60%

#. In the Text Field Component Window, Set the **Label** as **Destination Path**.

   .. figure:: ../../../_assets/web-app/stage-upload/text-field-label.png
      :alt: web-app
      :width: 60%
   
   Click **Save** to save the component.

   .. figure:: ../../../_assets/web-app/stage-upload/save-text-field.png
      :alt: web-app
      :width: 60%

Step 5 : Add Select Boxes Component
---------

If you want to map columns of the uploaded files, add select boxes. To add:

#. Expand the **General** tab.
#. Place the cursor on **Select Boxes** option and drag and drop it in the first column.

   **Note:** Make sure to drop the component right below the upload file component box and not inside the box.

   .. figure:: ../../../_assets/web-app/stage-upload/drag-select-boxes.png
      :alt: web-app
      :width: 60%

#. In the Select Boxes Component Window :

   In the **Display** tab, set the **Label** name as **Columns** and

   Check the **Hidden** box to make this component hidden.

   Also, check the **Inline Layout** Box.

   .. figure:: ../../../_assets/web-app/stage-upload/select-box-label.png
      :alt: web-app
      :width: 60%

   In the **Data** tab, add the default values where :
      
   **Label** is the display name and **Value** is the actual column name.

   Check the columns that should be considered as required fields.
       
   **Note:** Do not select the **CLEAR VALUE WHEN HIDDEN** checkbox as only the default values are needed when the component is chosen to be hidden.

   .. figure:: ../../../_assets/web-app/stage-upload/select-box-component.png
      :alt: web-app
      :width: 60%
   
   Click **Save** to save the settings and component.

   .. figure:: ../../../_assets/web-app/stage-upload/save-select-box.png
      :alt: web-app
      :width: 60%

Step 6 : Add Another Column Component
---------

#. Drag and drop the column right below the Select boxes as done in the previous steps

   .. figure:: ../../../_assets/web-app/stage-upload/drag-column2.png
      :alt: web-app
      :width: 60%
    
#. On the Column Component window, set the required fields as per choice and click **Save** to save the component.

   .. figure:: ../../../_assets/web-app/stage-upload/save-column2.png
      :alt: web-app
      :width: 60%


Step 7 : Add Upload Button Component
---------

To add upload button:

#. Expand the **General** Tab.
#. Place the cursor on **Buttons** option and drag and drop it in the left column created in step 6.

   .. figure:: ../../../_assets/web-app/stage-upload/add-upload-button.png
      :alt: web-app
      :width: 60%

#. In the Button Component window:

   Set the **label** as **upload**.
   
   Set the **Action** as **Event**.
   
   Enter the Button Event as **Upload**.
   
   Set the rest of the settings as per your choice.


   .. figure:: ../../../_assets/web-app/stage-upload/upload-button-component.png
      :alt: web-app
      :width: 60%
   
   Click **Save** to save the component settings.

   .. figure:: ../../../_assets/web-app/stage-upload/save-button-component.png
      :alt: web-app
      :width: 60%



Step 8 : Add Next Button Component
------

To go to the next stage and perform actions depending upon the event, Next button is needed. 

To add the Next button :

#. Expand the **General** Tab.
#. Place the cursor on **Buttons** option and drag and drop it in the right column created in step 6.

   .. figure:: ../../../_assets/web-app/stage-upload/add-next-button.png
      :alt: web-app
      :width: 60%

#. In the Button Component window:

   Set the **label** as **next**.
   
   Set the **Action** as **Event**.
   
   Enter the Button Event as **next**.
   
   Set the rest of the settings as per your choice.
   
   .. figure:: ../../../_assets/web-app/stage-upload/upload-next-button.png
      :alt: web-app
      :width: 60%

   .. figure:: ../../../_assets/web-app/stage-upload/custom-class.png
      :alt: web-app
      :width: 60%

   **Note:** 

      * By default, the button will get displayed on the LHS.
      * To display the button on the RHS, enter **float-right** in the **CUSTOM CSS CLASS** field.

   Click **Save** to save the component settings.

   .. figure:: ../../../_assets/web-app/stage-upload/save-next-button.png
      :alt: web-app
      :width: 60%


#. Again, on the edit stage page click **Save** to save the above-added components of the Stage.






































































































