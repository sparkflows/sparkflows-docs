Multiple File Upload in Analytical App
====================================

Fire Insights enables you to upload multiple files in Analytical App. 

This document explains in detail the steps required to enable multiple file upload in Analytical Apps.

Step 1 : Add File Component
-----------

To add a file component to choose files to upload to databricks : 

#. Go to **Edit Stage** Page.
#. Expand the **General** tab.
#. Drag and drop the **File** component on the RHS.
#. In the File Component Dialog Box :

   Under the  File tab, set the **Storage** as **Base64** from the dropdown list.
   
     .. figure:: ../../../_assets/web-app/MultipleFileUpload/file-storage.png
        :alt: web-app
        :width: 65%

   Under the API tab, set the **property name** as **file1**.

   **Note :** It is always recommended to use property names like file1, file2, and so forth when enabling users to upload multiple files.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/file-property-name.png
        :alt: web-app
        :width: 65%

   Click on the **Save** button to save the component settings.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/save-file.png
        :alt: web-app
        :width: 65%


Step 2 : Add Text Field Component
---------------
The Text Field component is essential for users to specify the destination path where the uploaded file will be located. To add :

#. Expand the **General** tab.
#. Drag and drop the **Text Field** component right below the File Component.
#. In the Text Field Component Dialog Box :

   Under the Display tab, set the **label** as **Destination Path**.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/text-label.png
        :alt: web-app
        :width: 65%

   Under the API tab, in the **Custom Properties** field, set the key as **for** and value as **file1**.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/text-custom.png
        :alt: web-app
        :width: 65%

   **Note :** Value will be similar to the file component property name e.g. file1, file2, etc.

   Click on the **Save** button to save the component settings.
   
     .. figure:: ../../../_assets/web-app/MultipleFileUpload/save-text.png
        :alt: web-app
        :width: 65%


Step 3 : Add Upload Button Component
------------

Upload button is essential to trigger the file upload. To add :

#. Expand the **General** tab.
#. Drag and Drop the **Button** Component right below the Text Field Component.
#. In the Button Component Dialog Box :

   Under the **Display** tab, set the following :

   * **Label** as **Upload**.
   * **Action** as **Event**.
   * **Button Event** as **upload**.
    
     .. figure:: ../../../_assets/web-app/MultipleFileUpload/button-label.png
        :alt: web-app
        :width: 65%

   Under the **API** tab, in the **Custom Properties** field, set the following :

   * **Key** as **for**.
   * **Value** as **file1**.
     
     .. figure:: ../../../_assets/web-app/MultipleFileUpload/button-custom.png
        :alt: web-app
        :width: 65% 

   Click on the **Save** button to save the component settings.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/save-button.png
        :alt: web-app
        :width: 65% 

Step 4 : Add Select Boxes Component (Optional)
---------------

To allow users to map the columns of the uploaded file, you can incorporate the Select Boxes component. To add :

#. Expand the **General** tab.
#. Drag and drop the **Select Boxes** component right below the upload button.
#. In the Select Boxes Dialog Box :

   Under the **Display** tab, set the following :

   * **Label** as **Columns**.
   * Select the **Hidden** checkbox to make the component hidden.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/selectbox-label.png
        :alt: web-app
        :width: 65% 

   Under the **Data** tab, add **values** where :

   * Label is the display name of the column.
   * Value is the actual column name of the column.
   
   Also, check the fields (columns) that should be considered as a required field.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/selectbox-data.png
        :alt: web-app
        :width: 65% 
 
   Under the **API** tab, in **Custom Properties** field set the following :

   * **Key** as **for**.
   * **Value** as **file1**.
    
     .. figure:: ../../../_assets/web-app/MultipleFileUpload/selectbox-custom.png
        :alt: web-app
        :width: 65% 
 
   Click on the **Save** button to save the component settings.

     .. figure:: ../../../_assets/web-app/MultipleFileUpload/save-selectbox.png
        :alt: web-app
        :width: 65% 

Step 5 : Save the Application Settings
-----------
#. Click on **Done** or **Save** to save the application settings.

.. note:: You can repeat the above steps to add as many file components as needed to enable multiple file uploads. Remember to modify the file component label to "file2", "files3", etc. and update the value as "file2", "file3" etc. under custom properties for each additional component added.





