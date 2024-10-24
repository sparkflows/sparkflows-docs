Project Variable 
===============

Project-level variables are displayed under the **Project Overview** page, within the **Settings** tab under the Variable section. Only users with **variable.modify** permission can access this tab.
Variables created at the project level will be shown in their respective project's overview page.

These variables have the highest priority, meaning it will first check for the variable at the project level. If it is available, the value will be fetched from here. If not, it will fall back to the group or global level.

Variable Permission
--------------------------------
Variable permissions can be found on the **Administration** page, under the **User Management** card in the **Role** tab and Click on **edit icon**.
Here user can get access for 
Add Variable - User must have **variables.add** permission
Edit Variable - User must have **variables.modify** permission to view variable tab inside project
View Variable - User must have **variables.view** permission
Delete Variable - User must have **variables.delete** permission

 .. figure:: ../../_assets/user-guide/variables/Variable_permission.png
      :alt: variables_userguide
      :width: 65%

Below are the steps for creating variables:

Add Variable 
--------------------------------
#. Click the **Add Variable** button located at the top right corner of the page.

   .. figure:: ../../_assets/user-guide/variables/Project_Variable_list.png
      :alt: variables_userguide
      :width: 65%

#. In the dialog box, add parameters by key, value  and description and click on **save** button :
   For Key alphanumeric value can be added including '_'

  .. figure:: ../../_assets/user-guide/variables/Add_Variable.png
        :alt: variables_userguide
        :width: 65%

**Editing, viewing, and deleting variables are the same as at the global or group level. The only difference is that these actions must be performed from the project list page**
