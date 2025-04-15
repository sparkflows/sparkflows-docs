Importing Variables with INI or JSON file
===============

Global level variables are displayed on the **Administration** page within the **Variables** card.

.. figure:: ../../../_assets/user-guide/variables/Variable_Card.PNG
      :alt: variables_userguide
      :width: 65%

This card is accessible only to **superusers**. The Variables card can be shown or hidden based on the configuration value **module.enableVariables**, which defaults to **false**.


.. figure:: ../../../_assets/user-guide/variables/variables_config.png
      :alt: variables_config
      :width: 65%

Here variables can be imported at both **Global** & **Group** level.

**Pre-Requisites**
++++++++++++++++

#. Creation of INI file for import

   A few rules while adding the keys and values for .INI file and .INI Parsing Convention -

   * Lines before any [section] are considered global (no section prefix).
   * Once a [section] is defined, all subsequent keys belong to that section until a new section is defined.
   * There's no concept of "exiting" a section — you can only move into a new one.

   In this approach the non sectioned variables will be created directly with **key = value** but the sectioned variable’s key will be set as **sectionName.key =     value** once the .ini file is imported. Create a valid .ini file that contains key-value data in it and the file can also contain sectioned data in it using a     format similar to below image.

      .. figure:: ../../../_assets/user-guide/variables/import-variables/sample-ini-file.png
          :alt: variables_userguide
          :width: 35%

   For Example: From the above image of an .ini file the key **timeout** will directly store the value as **30** when imported as a variable but the sectioned        key like **host** will have the key set as **database.host** whose value will be set as **localhost** when imported as a variable.

#. Creation of JSON file for import

   Create a valid .json file that contains key-value data in flat or nested structure to import variables using JSON file like the image below:

     .. figure:: ../../../_assets/user-guide/variables/import-variables/sample-json-file.png
        :alt: variables_userguide
        :width: 35%

   In this approach:

   * Top-level keys will be directly used as variables with their key = value 
     For Example: "timeout": "30" will be stored as a variable with key **timeout** and value **30**.

   * Nested keys (i.e., objects within objects) will be flattened into a dot notation using their hierarchy.
     For example: "app": { "name": "MyApp" } will create a variable with key **app.name** and value **MyApp**.

.. Note:: * The length of keys and values is limited to 255 characters hence while adding the keys or values to the .JSON or .INI file limit the characters to 255.
          * Avoid adding trailing and leading spaces to the keys and values in the JSON or INI file.
          * The Variable Key can only contain letters, numbers, dots, or underscores.
          * The Variable Value can contain anything after the first non-whitespace character


The steps to import variables are as follows:

Step 1: Navigate to Variables Page
--------------------------------

Global level variables are displayed on the **Administration** page within the **Variables** card.

.. figure:: ../../../_assets/user-guide/variables/Variable_Card.PNG
      :alt: variables_userguide
      :width: 65%

Step 2: Import Variables for All Groups
--------------------------

#. Now to import variables for **All Groups** click on the **Import** button and then on **Import Variables for All** button in the dropdown options.

   .. figure:: ../../../_assets/user-guide/variables/import-variables/import-variables-for-all.png
      :alt: variables_userguide
      :width: 65%

   * Now on selection of the option **Skip Variable key if it exists with the same name** :

     To import variables, select a valid **.INI** or **.JSON** file formatted as outlined in the Prerequisites section above. If the **Skip Variable Key if it           Exists with same name** option is selected, any variables from the file that already exist under All Groups will be skipped, and only those with unique keys        will be imported.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/import-variables-for-all-skip-ini.png
        :alt: variables_userguide
        :width: 65%

     On click of **Import** button it will show the information popup regarding the count of imported variables and the count of skipped variables along with the        reason for why specific keys from the file were skipped in a tabular format.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/skip-option-variable-import-ini-file.png
        :alt: variables_userguide
        :width: 65%

     Another Scenario is that if **Skip Variable Key if it Exists with same name** option was selected. If we select a .ini or .json file that has all the same         keys present in it that exist under All Groups, then those keys will be skipped during import. The skipped keys, along with the corresponding reasons, are         displayed in the import summary like the image below :

     .. figure:: ../../../_assets/user-guide/variables/import-variables/skip-option-variable-import-error-reason.png
        :alt: variables_userguide
        :width: 65%

   * Now on selection of the option **Overwrite Variable value if key is present with same name** :

     To import variables, select a valid **.INI** or **.JSON** file formatted as described in the Prerequisites section above. If the option "Overwrite Variable value if key is present with same name" is selected, any variables from the file that match existing keys under All Groups will have their values overwritten with the new values from the imported file. Variables with unique keys will be imported as new entries.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/import-variables-for-all-overwrite-json.png
        :alt: variables_userguide
        :width: 65%

     On click of **Import** button it will show the information popup regarding the count of imported variables and the count of skipped variables along with the reason for why specific keys from the file were skipped in a tabular format. In the example image below, we can see that the imported JSON file contained keys that already existed, so all corresponding values were successfully overwritten to the value set from the imported file.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/overwrite-option-variable-import-json-file.png
        :alt: variables_userguide
        :width: 65%

Step 3: Import Variables for a Group
--------------------------

#. Now to import variables for a specific **Group** click on the **Import** button and then on **Import Variables for Group** button in the dropdown options.

   .. figure:: ../../../_assets/user-guide/variables/import-variables/import-variables-for-group.png
      :alt: variables_userguide
      :width: 65%

   * Now on selection of the option **Skip Variable key if it exists with the same name** with a group selected :

     To import variables, select a valid **.INI** or **.JSON** file formatted as outlined in the Prerequisites section above. Now select the **Group** to which the variables are to be imported. If the "Skip Variable Key if it Exists with Same Name" option is selected, any variables from the file that already exist under the selected group will be skipped, and only those with unique keys will be imported for the selected group as new entries.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/import-variables-for-group-skip-ini.png
       :alt: variables_userguide
       :width: 65%

     On click of the **Import** button it will show the information popup regarding the count of imported variables for the selected group and the count of skipped variables for the selected group along with the reason for why specific keys from the file were skipped in a tabular format.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/skip-option-variable-group-import-ini-file.png
       :alt: variables_userguide
       :width: 65%

     Another Scenario is that if **Skip Variable Key if it Exists with same name** option was selected and a **Group** was selected. If we select a .ini or .json file that has all the same keys present in it that exist under the selected group, then those keys will be skipped during import. The skipped keys for the selected group, along with the corresponding reasons, are displayed in the import summary like the image below :

     .. figure:: ../../../_assets/user-guide/variables/import-variables/skip-option-variable-import-error-reason.png
       :alt: variables_userguide
       :width: 65%

   * Now on selection of the option **Overwrite Variable value if key is present with same name** with a group selected :

     To import variables, select a valid **.INI** or **.JSON** file formatted as described in the Prerequisites section above. Now select the **Group** to which the variables are to be imported. If the option **Overwrite Variable value if key is present with same name** is selected, any variables from the file that match existing keys under the selected **Group** will have their values overwritten with the new values from the imported file. Variables with unique keys will be imported as new entries for the selected group.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/import-variables-for-group-overwrite-json.png
       :alt: variables_userguide
       :width: 65%

     On click of **Import** button it will show the information popup regarding the count of imported variables for the selected **Group** and the count of skipped variables for the selected **Group** along with the reason for why specific keys from the file were skipped in a tabular format. In the example image below, we can see that the imported JSON file contained keys that already existed, so all corresponding values were successfully overwritten for the selected group.

     .. figure:: ../../../_assets/user-guide/variables/import-variables/overwrite-option-variable-group-import-json-file.png
       :alt: variables_userguide
       :width: 65%

















 
   
