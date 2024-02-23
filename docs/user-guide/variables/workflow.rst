Workflow 
=============

In Sparkflows, variables are used for a variety of reasons that enhance the software's ability to handle, analyze, and manipulate data effectively. Here’s why variables are significant in Sparkflows:

* **Dynamic Data Processing:** Variables in Sparkflows allow users to dynamically alter workflows based on varying data inputs or user-defined criteria. This makes it possible to create more flexible and adaptable workflows that can handle different datasets or parameters without needing manual adjustment each time.
* **Parameterization:** Variables can be used to parameterize inputs, formulas, and other elements within a workflow. This means that values or conditions can be changed at a single point (the variable), and those changes will propagate throughout the workflow where the variable is referenced. This is particularly useful for scenarios where workflows need to be run multiple times with different parameters.
* **Conditional Logic Implementation:** In Sparkflows, variables can be used to implement conditional logic within workflows, such as in Filter tools or within the Formula tool. This allows the workflow to dynamically adapt its processing based on the data it encounters or based on external inputs.

Below are the steps for creating and using variables:

Step 1: Creating Variables in Sparkflows
--------------------------------
#. Click on **Plus Button** placed on the top right corner of the workflow editor.

   .. figure:: ../../_assets/user-guide/variables/plus-button.png
      :alt: readwrite_userguide
      :width: 65%

#. In the dialog box, add parameters by name and value:
   
   For String Data pass value in single quotes (') or double quotes (").

   For multiple value in same parameter separated by comma.

   .. figure:: ../../_assets/user-guide/variables/dialog-box.png
      :alt: readwrite_userguide
      :width: 65%

Step 2: Using Variables in Workflows
--------------------------
#. Pass defined parameters in row filter to filter data as per requirement in the following format: 
   
   **${Name_variable}** 

   .. figure:: ../../_assets/user-guide/variables/conditional-expression.png
      :alt: readwrite_userguide
      :width: 65%

Step 3 : Changing Variable Values on Workflow Execution Page (Optional)
-------------------------------------------

* This is an optional step where variable values can be changed on workflow execution page also as shown below:

  .. figure:: ../../_assets/user-guide/variables/execution-page.png
     :alt: readwrite_userguide
     :width: 65%


* Below image shows data before using variables:

  .. figure:: ../../_assets/user-guide/variables/original-data.png
     :alt: readwrite_userguide
     :width: 65%

* Below image shows data after using variables:

  .. figure:: ../../_assets/user-guide/variables/changed-data.png
     :alt: readwrite_userguide
     :width: 65%


