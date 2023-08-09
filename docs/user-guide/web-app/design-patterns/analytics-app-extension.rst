Nested Notebooks Execution
=======================

Overview
--------

In the Analytical App there are various stages. There can be multiple Run stages. Each Run stage can be utilized to execute a different or the same Notebook. Also, the output of the execution of one Notebook, can go as input to the next Notebook execution.

This document explains in detail the steps required to execute nested notebooks or workflows.

Steps
-----

Users can set Notebook or workflow at the stage label. The run stage has the option to set workflow or notebook. 

Users can choose a specific workflow or notebook here for execution. To choose follow the below steps :

**Step 1 : Go to Change Workflow/Notebook Dialog**
++++++++

#. Go to **edit analytics app page**.
#. Click on the **Change workflow/Notebook** option on the Run Stage Label.

   .. figure:: ../../_assets/web-app/nested-notebook/change-wf.png
      :alt: web-app
      :width: 70%

**Step 2 : Select the Workflow/Notebook**
++++++

#. On the Dialog, select the notebook or workflow from the dropdown list.

   .. figure:: ../../_assets/web-app/nested-notebook/change-wf-dialog.png
      :alt: web-app
      :width: 70%

**Step 3 : Execute the App**
++++++++

#. On the **edit analytics app page**, click on the **Run** button.
   
   This will take you to the first stage. Fill in all the details here.

   .. figure:: ../../_assets/web-app/nested-notebook/first-stage.png
      :alt: web-app
      :width: 70%

#. Now, click on the **Next** button. The next stage is the first run stage.

   .. figure:: ../../_assets/web-app/nested-notebook/run-1.png
      :alt: web-app
      :width: 70%

    
   **Note 1 :** 
    
   The next button is disabled in the Run stage. To keep it diasbled we have set the fields as below :
    
   API property name is set as **afterRun**. 
     
   Also in the Display tab, it is set to be **disabled**.

   .. figure:: ../../_assets/web-app/nested-notebook/run-button.png
      :alt: web-app
      :width: 70%

   **Note 2 :** 

   When the workflow or the notebook is executed as part of first stage, it may output some parameters.
   
   These parameters get displayed on the Execution page. But on this page they are disabled and the users can only view them.

   .. figure:: ../../_assets/web-app/nested-notebook/execute-parameter.png
      :alt: web-app
      :width: 70%


#. Click on the **Run** button to reach the second parameters stage.
   
   The result parameters would get displayed here. Users can update the values for the parameters.

   .. figure:: ../../_assets/web-app/nested-notebook/execute-parameter-2.png
      :alt: web-app
      :width: 70%

   **Note :** 
   
   In order to capture the result parameters there is a **fieldset** in the page or stage.

   .. figure:: ../../_assets/web-app/nested-notebook/parameter-component.png
      :alt: web-app
      :width: 70%

   The name of the **Fieldset property** in the **API tab** should be set as **parameters**.

   .. figure:: ../../_assets/web-app/nested-notebook/api-setting.png
      :alt: web-app
      :width: 70%

#. On the second parameters page, click on the **Run** button to execute this stage.

   The result parameters would also be passed as inputs to notebook or workflow execution in this stage.

   .. figure:: ../../_assets/web-app/nested-notebook/final-execution.png
      :alt: web-app
      :width: 70%
      
      
.. note::  

   1. The Fieldset for displaying the parameters to the user can be in a separate Parameters Stage, or it can also be in the next Run Stage.
   2. The Fieldset has to be in the page immediately after the first Run Stage.
   3. There can be any number of Run Stages.
   
   
   
   
   
   

      
