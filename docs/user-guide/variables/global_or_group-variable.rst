Global and Group Variables 
===============

Global level variables will be displayed under the **Administration** page within the **Variables** card. This card can be acess by superuser only. 
Variables Card can be hide/show depending upon value given in configuration `module.enableVariables`, whose defualt value is false.

.. figure:: ../../_assets/user-guide/variables/variables_config.PNG
      :alt: variables_config
      :width: 65%

Here variable can be defined at both Global & Group level.

These variables have the lowest precedence, meaning they are only used if a corresponding variable is not defined at the project or group level.

.. figure:: ../../_assets/user-guide/variables/Variable_Card.PNG
      :alt: variables_userguide
      :width: 65%


Below are the steps for creating variables:

Step 1: Creating Variables at global level in Sparkflows
--------------------------------
#. Click the **Add Variable** button located at the top right corner of the page. From the dropdown that appears, select the **Add Variable for All** option.

   .. figure:: ../../_assets/user-guide/variables/Variable_List.PNG
      :alt: variables_userguide
      :width: 65%

#. In the dialog box, add parameters by key, value  and description and click on **save** button :

   .. figure:: ../../_assets/user-guide/variables/Add_Variable.PNG
      :alt: variables_userguide
      :width: 65%

Step 2:Creating Variables at Group level in Sparkflows
--------------------------
#. Click the **Add Variable** button located at the top right corner of the page. From the dropdown that appears, select the **Add Variable for Group** option.

   .. figure:: ../../_assets/user-guide/variables/Variable_List.PNG
      :alt: variables_userguide
      :width: 65%

#. In the dialog box, add parameters by key, value description and select the group from dropdown.click on **save** button :

   .. figure:: ../../_assets/user-guide/variables/Add_group_var.PNG
      :alt: variables_userguide
      :width: 65%

Edit Variable
-------------------------------------------

#. Click the **edit icon** displayed in front of the variable you want to modify

   .. figure:: ../../_assets/user-guide/variables/Variable_List.PNG
     :alt: variables_userguide
     :width: 65%


#. In the dialog box, modify the field and click on **update** button
    Here modified the key as **Default_var_Val**

   .. figure:: ../../_assets/user-guide/variables/Edit_Variable.PNG
     :alt: variables_userguide
     :width: 65%

   *The image below shows data after updating the variables:

    .. figure:: ../../_assets/user-guide/variables/After_Edit_Variable.PNG
      :alt: variables_userguide
      :width: 65%

View Variable
-------------------------------------------

#. Click the **view icon** displayed in front of the variable you want to view

   .. figure:: ../../_assets/user-guide/variables/Variable_List.PNG
     :alt: variables_userguide
     :width: 65%

#. In the dialog box, it will display all fields & their value 

   .. figure:: ../../_assets/user-guide/variables/View_Variable.PNG
     :alt: variables_userguide
     :width: 65%

Delete Variable
-------------------------------------------

#. Click the **delete icon** displayed in front of the variable you want to delete

   .. figure:: ../../_assets/user-guide/variables/Variable_List.PNG
     :alt: variables_userguide
     :width: 65%

#. In the dialog box will open with message
   **Are you sure you want to delete this variable? Deleting it will break any functionality or references that depend on it**
   and click on Ok button to delete the variable

   .. figure:: ../../_assets/user-guide/variables/View_Variable.PNG
     :alt: variables_userguide
     :width: 65%

  *The image below shows data after deleting the variables:

   .. figure:: ../../_assets/user-guide/variables/After_Delete_Variable.PNG
     :alt: variables_userguide
     :width: 65%
