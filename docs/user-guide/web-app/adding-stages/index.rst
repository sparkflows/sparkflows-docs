Adding Stages
=============

This document explains in detail the steps required to add stages to an Anlytical App.

Step 1 : Open Add Stage Window
---------

#. Click the **Plus Icon** button on the create or edit analytical app page. 

     .. figure:: ../../../_assets/web-app/add-stages/add-stage.png
        :alt: web-app
        :width: 70%
      
Step 2 : Enter the Required Fields
---------

On the Add stage window:

#. Select the **stage type** from the drop-down list i.e. Upload, Parameter or Run.
#. Enter the desired **stage name**.
#. Enter the **condition**, if any. Note: 
   
   * Conditions are added to show particular stage on run analytics app page when the added condition for that stage is fulfilled.
   * Examples of conditions:
      
     1. educationLevel = 'masters'
     2. educationLevel = 'masters' && gender = 'female'
     3. educationLevel = 'masters' || gender = 'female'
     4. Leave it empty if you prefer the stage to always be displayed.

     .. figure:: ../../../_assets/web-app/add-stages/enter-fields.png
        :alt: web-app
        :width: 40%
      
Step 3 : Add the Stage
-----------

#. Once you enter all the field details, click on the **Add** button to add the stage.
   
   Note: 
   
   - You can rearrange the stages by using drag and drop. 
   - You can EDIT, VIEW, and REMOVE stages.
   - You can also RENAME the stage name and update condition.

  If successfully added, the stage will be displayed on the Edit Stage Page as below:
 
   .. figure:: ../../../_assets/web-app/add-stages/save-stage.png
      :alt: web-app
      :width: 70%
      

Below are the examples for adding various Stages:

.. toctree::
   :maxdepth: 2

   upload.rst
   parameters.rst
   advanceLogic.rst
   run.rst
