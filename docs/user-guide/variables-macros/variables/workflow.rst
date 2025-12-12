Variables in Workflows
=============

In Sparkflows, variables are used for a variety of reasons that enhance the software's ability to handle, analyze, and manipulate data effectively. Here’s why variables are significant in Sparkflows:

* **Dynamic Data Processing :** Variables in Sparkflows allow users to dynamically alter workflows based on varying data inputs or user-defined criteria. This makes it possible to create more flexible and adaptable workflows that can handle different datasets or parameters without needing manual adjustment each time.
* **Parameterization :** Variables can be used to parameterize inputs, formulas, and other elements within a workflow. This means that values or conditions can be changed at a single point (the variable), and those changes will propagate throughout the workflow where the variable is referenced. This is particularly useful for scenarios where workflows need to be run multiple times with different parameters.
* **Conditional Logic Implementation :** In Sparkflows, variables can be used to implement conditional logic within workflows, such as in Filter tools or within the Formula tool. This allows the workflow to dynamically adapt its processing based on the data it encounters or based on external inputs.

Below are the steps for creating and using variables:

Step 1 : Creating Variables in Sparkflows
--------------------------------
#. Click on **Plus** button placed on the top right corner of the workflow editor.

   .. figure:: ../../../_assets/user-guide/variables/plus-button.png
      :alt: variables_userguide
      :width: 65%

#. In the dialog box, add description and parameters by name and value, as shown below:

   .. figure:: ../../../_assets/user-guide/variables/dialog-box.png
      :alt: variables_userguide
      :width: 65%

 - For **String Data** pass value in **single quotes (')** or **double quotes (")**.

 - For **multiple value** in same parameter **separated by comma**.

   
   

Step 2 : Using Variables in Workflows
--------------------------
#. Pass defined parameters in row filter to filter data as per requirement in the following format: 
   
   **${Name_variable}** 

   .. figure:: ../../../_assets/user-guide/variables/conditional-expression.png
      :alt: variables_userguide
      :width: 65%

Step 3 : Changing Variable Values on Workflow Execution Page (Optional)
-------------------------------------------

* This step is optional where you can modify variable values on workflow execution page if required, as shown below:

  .. figure:: ../../../_assets/user-guide/variables/execution-page.png
     :alt: variables_userguide
     :width: 65%


* The image below shows data before using variables:

  .. figure:: ../../../_assets/user-guide/variables/original-data.png
     :alt: variables_userguide
     :width: 65%

* The image below shows data after using variables:

  .. figure:: ../../../_assets/user-guide/variables/changed-data.png
     :alt: variables_userguide
     :width: 65%

Using Macros set in Variables in Workflows
--------------------------------

Below is an example for using **Variables** in a workflow where in the Variable's value is set as a **Macro** -

* The Variables are created in the below format where in the value is set to a macro -

   .. list-table:: 
      :widths: 30 40 50
      :header-rows: 1

      * - Variable Key
        - Variable Value
        - Description
      * - HomePath
        - /home/sparkflows
        - Home Path
      * - date_year
        - ${fire.macros.ds_format(ds,y,YYYY,0)}
        - Gets the current year
      * - date_month
        - ${fire.macros.ds_format(ds,m,M,0)}
        - Gets the current month
      * - date_day
        - ${fire.macros.ds_format(ds,d,D,-1)}
        - Gets the day before the current day

* Post declaring the variables in the above way it can be used in the workflow in the following way -

   .. figure:: ../../../_assets/user-guide/variables/using-macros-in-variables.png
      :alt: Using Macros in Variables
      :width: 65%

  Here the path is set to **${HomePath}/year=${date_year}/month=${date_month}/day=${date_day}** which would be evaluated to **/home/sparkflows/year=2025/month=12/day=11** after resolving the macros that are used in the variables.

* On executing the workflow it will correctly read the path and print the data -

   .. figure:: ../../../_assets/user-guide/variables/marcos-in-variables-exe-res.png
      :alt: Using Macros in Variables Execution Result
      :width: 65%





