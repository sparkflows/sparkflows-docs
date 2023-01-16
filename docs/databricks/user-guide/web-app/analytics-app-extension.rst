Nested Notebooks Execution
=======================

Overview
--------

In the Analytics App there are various stages. There can be multiple Run stages. Each Run stage can be executing a different or the same Notebook.

Also, the output of the execution of one Notebook, can go as input to the next Notebook execution.

Steps
-----

Users can set workflow/Notebook at stage label. The run stage has the option to set workflow or notebook. Users can choose a specific workflow or notebook here for execution.

.. figure:: ../../_assets/web-app/wae-change-notebook.png
      :alt: web-app
      :width: 90%

On Clicking on Change Workflow/Notebook icon, a popup dialog will appear. Users can select workflow/notebook for current stage execution.

.. figure:: ../../_assets/web-app/wae-select-notebook.PNG
      :alt: web-app
      :width: 90%

When users run Analytics App, they will land on the first stage.

.. figure:: ../../_assets/web-app/wae-first-parameters.PNG
      :alt: web-app
      :width: 90%

The next stage is the first run stage

.. figure:: ../../_assets/web-app/wae-first-execution.PNG
      :alt: web-app
      :width: 90%


There is a change in the next button on the run stage. Its API property name should be **afterRun**. Also in the Display tab, set it to ``disabled``.

.. figure:: ../../_assets/web-app/wae-execution-next.PNG
      :alt: web-app
      :width: 90%



When the workflow or the notebook is executed, it may output some parameters. These parameters get displayed in the Execution page. In this page they are disabled and the users can only view them.

.. figure:: ../../_assets/web-app/wae-execution-result-parameters.png
      :alt: web-app
      :width: 90%


After clicking on the Next button, the user will go to the second parameters stage. The result parameters would get displayed here. Users can updated the values for the parameters.

.. figure:: ../../_assets/web-app/wae-result-parameters.PNG
      :alt: web-app
      :width: 90%

In order to capture the result parameters there is a fieldset in the page/stage.

.. figure:: ../../_assets/web-app/wae-result-parameters-edit.png
      :alt: web-app
      :width: 90%

The name of the Fieldset property should be **parameters**.

.. figure:: ../../_assets/web-app/wae-result-parameters-edit1.PNG
      :alt: web-app
      :width: 90%

The next stage is final execution. Users would click Run to execute this stage. The result parameters would also be passed as inputs to notebook/workflow execution.

.. figure:: ../../_assets/web-app/wae-final-execution.PNG
      :alt: web-app
      :width: 90%
      
      
.. note::  

   1. The Fieldset for displaying the parameters to the user can be in a separate Parameters Stage, or it can also be in the next Run Stage.
   2. The Fieldset has to be in the page immediately after the first Run Stage.
   3. There can be any number of Run Stages.
   
   
   
   
   
   

      
