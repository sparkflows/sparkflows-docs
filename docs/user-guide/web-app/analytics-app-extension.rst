Analytics App Extension
=======================

Users can set workflow/Notebook at stage label. The run stage has the option to set workflow or notebook. Users can choose a specific workflow or notebook here for execution.

.. figure:: ../../_assets/web-app/wae-change-notebook.png
      :alt: web-app
      :width: 90%

On Clicking on Change Workflow/Notebook icon, a pop will appear. Users can select workflow or notebook for current stage execution.

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

There is a change in the next button on the run stage. Its API property name should be **afterRun** and select disabled property.

.. figure:: ../../_assets/web-app/wae-execution-next.PNG
      :alt: web-app
      :width: 90%

After execution workflow or notebook return results with some parameters.

.. figure:: ../../_assets/web-app/wae-execution-result-parameters.png
      :alt: web-app
      :width: 90%

After clicking on the Next button, the user will go to the second parameters stage. Where result parameters will show. Users can select or deselect parameters also.

.. figure:: ../../_assets/web-app/wae-result-parameters.PNG
      :alt: web-app
      :width: 90%

To capture result parameters there is a fieldset there.

.. figure:: ../../_assets/web-app/wae-result-parameters-edit.png
      :alt: web-app
      :width: 90%

Fieldset property name should be **parameters**.

.. figure:: ../../_assets/web-app/wae-result-parameters-edit1.PNG
      :alt: web-app
      :width: 90%

The next stage is final execution. Click run to execute again with result parameters.

.. figure:: ../../_assets/web-app/wae-final-execution.PNG
      :alt: web-app
      :width: 90%
