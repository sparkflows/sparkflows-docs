Adding Stages
=============

Click on the ``Add stages`` button to add a new stage. Select stage type, enter the stage name and condition(optional).

  .. figure:: ../../../_assets/web-app/AddStage.png
      :alt: web-app
      :width: 80%


- You can rearrange the stages by using drag & drop. 
- You can EDIT, VIEW, and REMOVE stages.
- Can also RENAME the stage name and update condition.
- Conditions are added to show particular stage on run analytics app page when added condition for that stage is fulfilled.
- Conditions Example are :
 
  1. educationLevel = 'masters'
  2. educationLevel = 'masters' && gender = 'female'
  3. educationLevel = 'masters' || gender = 'female'
  4. Leave it empty to show particular stage to be displayed always.

Below are the examples for adding various Stages:

.. toctree::
   :maxdepth: 2

   upload.rst
   parameters.rst
   advanceLogic.rst
   run.rst
