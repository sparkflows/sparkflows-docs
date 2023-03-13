Multiple File Upload in Analytics App
====================================

Fire Insights enables you to upload multiple file in Analytics App.

- Add a file component to choose files to upload to databricks. In this component, in the File tab in ``STORAGE`` select ``Base64``. Set it's property name as ``file1`` , ``file2``, if wanted to upload more than 1 file.  

      .. figure:: ../../_assets/web-app/upload-1.png
            :alt: web-app
            :width: 80%

- Add one text field to add ``DESTINATION PATH`` where the browse file should get uploaded. Set its label as ``Destination Path``. Add key and its value in "CUSTOM PROPERTIES" where key as ``for`` and value as property name of file component e.g. ``file1``.

      .. figure:: ../../_assets/web-app/destination-path-1.png
            :alt: web-app
            :width: 80%

- Add upload button and set the action to ``event``. Set the button event name to ``upload``. Add key and its value in "CUSTOM PROPERTIES" where key as ``for`` and value as property name of file component e.g. ``file1``.

      .. figure:: ../../_assets/web-app/upload-2.png
            :alt: web-app
            :width: 80%

- If we want the user to map the columns of the file uploaded, below are the steps for it

 * Add select boxes component to add the available column names. Set its label as ``Columns`` and make this component hidden by selecting the ``hidden`` checkbox. 

 * Added default values where ``LABEL`` is ``DISPLAY NAME``, ``VALUE`` is ``ACTUAL COLUMN NAME`` and select that field which should be considered as a required field.    
   And don't select this value ``CLEAR VALUE WHEN HIDDEN`` because we want the default value when the component is hidden.
 
 * Add key and its value in "CUSTOM PROPERTIES" where key as ``for`` and value as property name of file component e.g. ``file1``.

      .. figure:: ../../_assets/web-app/map-1.png
            :alt: web-app
            :width: 80%
