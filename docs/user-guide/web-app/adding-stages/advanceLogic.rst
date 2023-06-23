Advance Parameters Design
=======

In the Parameters stage, components can be added by selecting text fields, select boxes, buttons, and more. 

These elements also provide options for adding conditions and logic.

This document outlines the essential steps for adding conditions and logic effectively.

Conditions and Logics
-------

Conditions
++++

Conditions are primarily used to show or hide components based on specific rules. There are two ways to apply conditions: 

* For **simple conditions**, users can choose from predefined options.
* For **advanced conditions**, users can enter custom JavaScript code. 
  
  They must assign boolean values to variable names i.e. **show** to control component visibility.

Logic
+++++++

Logic involves combining triggers and actions. Users can add multiple logics for the same component. For example:

* **Simple** triggers require selecting from available options.

* **Advanced or JavaScript** triggers involve entering custom JavaScript code that will return a result variable.

**Note :** Every logic must have at least one **action**, which will return a value variable.


Add Simple and Advanced Condition
-----------

Follow the below steps to add condtions :

**Step 1 : Add Text Field Components**
++++++

#. Expand the **General** tab.
#. Add as many text fields as are needed to apply conditions by the use of drag and drop **Text Fields**.  
  
   .. figure:: ../../../_assets/web-app/adv-parameters/add-text-field.png
      :alt: web-app
      :width: 60%

#. Set the **Labels** of each of them in the **Display** tabs. 
   
   .. figure:: ../../../_assets/web-app/adv-parameters/text-field-label.png
      :alt: web-app
      :width: 60%

#. Click **Save** to Save the the components.

   **Note :** We have added 3 components with the labels set as Country, Capital and Business City.

   .. figure:: ../../../_assets/web-app/adv-parameters/save-text-fields.png
      :alt: web-app
      :width: 60%
 
   
**Step 2 : Set the Conditions**
+++++++


**To add the simple condition :**
.......

#. Click on the **edit** button of text field component on which you want to apply condition.

   **Note :** We have selected text field component labeled as CAPITAL.

   .. figure:: ../../../_assets/web-app/adv-parameters/edit-text-field1.png
      :alt: web-app
      :width: 60%

#. On the Text Field component window, click on the **Conditional** tab.
#. Set the required fields as :

   Select **True or False** based on whether you want the component to be visible or not.

   Select the component on which you want to apply the condition e.g. Country(country)
   
   Enter the value to be checked e.g. USA.

   .. figure:: ../../../_assets/web-app/adv-parameters/add-simple-condition.png
      :alt: web-app
      :width: 60%

#. Click **Save** to save the component settings.

#. Click **Save** on the edit stage page to save the stage settings.

**To add the Advanced Condition :**
.............

#. Click on the **edit** button of text field component on which you want to apply condition.

   **Note :** We have selected text field component labeled as BUSINESS CITY.

   .. figure:: ../../../_assets/web-app/adv-parameters/edit-text-field2.png
      :alt: web-app
      :width: 60%

#. On the Text Field component window, click on the **Conditional** tab.
#. Click on the **Advanced Conditions** option.
#. Enter the **custom condition** in the **JavaScript** field.
   
   For e.g. show = data.country == 'USA' || data.country == 'India'
  
   .. figure:: ../../../_assets/web-app/adv-parameters/add-java-condition.png
      :alt: web-app
      :width: 60%

#. Click **Save** to save the condition.
#. Click **Save** or **Done** to save the stage settings.

   

Add Logics and Actions
-------

Follow the below steps to add the logics :

**Step 1 : Add Text Field Components**
+++++++++

#. Expand the **General** tab.
#. Add as many text fields as are needed to apply conditions by the use of drag and drop the **Text Fields**.  
   
   .. figure:: ../../../_assets/web-app/adv-parameters/add-text-field.png
      :alt: web-app
      :width: 60%
#. Set the **Labels** of each of them in the **Display** tabs. 

   .. figure:: ../../../_assets/web-app/adv-parameters/text-field-label.png
      :alt: web-app
      :width: 60%

#. Click **Save** to Save the the components.

   **Note :** We have added 3 components with the labels set as Country, Capital and Business City.
   
   .. figure:: ../../../_assets/web-app/adv-parameters/save-text-fields.png
      :alt: web-app
      :width: 60%
   


**Step 2 : Set the Simple Logic and Action**
+++++++++

**To add the Simple Logic :**
..........

#. Click on the **edit** button of text field component on which you want to apply condition.

   **Note :** We have selected text field component labeled as CAPITAL.

   .. figure:: ../../../_assets/web-app/adv-parameters/edit-text-field1.png
      :alt: web-app
      :width: 60%
   

#. On the Text Field component window, click on the **Logic** tab and then click on the **Add Logic** button.

   .. figure:: ../../../_assets/web-app/adv-parameters/add-logic.png
      :alt: web-app
      :width: 60%


#. Enter the required fields as below :

   Enter the desired **Logic Name** e.g. Upload Field.
   
   Set the **trigger type** as **Simple** from the drop-down list.
   
   Select the field, from the drop-down list, on which logic is to be applied e.g. Country(country).

   Enter the **Value** of the logic e.g. USA.

   .. figure:: ../../../_assets/web-app/adv-parameters/add-simple-logic.png
      :alt: web-app
      :width: 60%


**To add action, follow the below steps :**
............

#. Click on **Add Action** button on the Logic tab.

   **Note :** It is mandatory to add atleast one action for each logic.

#. Enter the required fields :

   Enter the desired **action name** e.g. Field Action

   Select the **Type** as **value** from the drop-down list.
   
   Enter the **Javascript custom code** in the **value** Column e.g. value = 'Washington'.

   .. figure:: ../../../_assets/web-app/adv-parameters/add-simple-action.png
      :alt: web-app
      :width: 60%

#. Save the logic and action :

   Click on the **Save Logic** and **Save Action** buttons

   .. figure:: ../../../_assets/web-app/adv-parameters/save-logic-action.png
      :alt: web-app
      :width: 60%

#. Save the Component settings :
   
   Click on the **Save** button to save the text field component settings.

    

Step 3 : Set Advanced Logic and Action
+++++++

**To add advanced logic, follow the below steps :**
..............

#. Click on the **edit** button of text field component on which you want to apply condition.

   **Note :** We have selected text field component labelled as BUSINESS CITY.

#. On the Text Field component window, click on the **Logic** tab and then click on the **Add Logic** button.
   
   .. figure:: ../../../_assets/web-app/adv-parameters/add-logic.png
      :alt: web-app
      :width: 60%

#. Enter the required fields as below :

   Enter the desired **Logic Name** e.g. Field Update.
   
   Set the trigger type as **JAVASCRIPT** from the drop-down list.
   
   Enter the result value custom condition in the **TEXT AREA** field.
   
   For e.g. result = (data.country == 'USA' && data.capital == 'Washington').
   
   .. figure:: ../../../_assets/web-app/adv-parameters/add-java-logic.png
      :alt: web-app
      :width: 60%

#. Add the action by following the steps mentioned above in step 2.
#. Click on **Save Logic** and **Save Action** buttons.

   .. figure:: ../../../_assets/web-app/adv-parameters/save-java-logic.png
      :alt: web-app
      :width: 60%

#. Click on **Save** to save the component settings.

#. On the edit stage page, click on **Save** or **Done** to save the new stage settings.



 
   









   


    
























      
