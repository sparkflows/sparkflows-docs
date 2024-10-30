Code Library
=====================
The Code Library in Sparkflows allows users to store and manage reusable code snippets for use in workflows. This document provides step-by-step instructions to enable, access, and create a Code Library within Sparkflows.

Step 1 : Enable the Code Library
--------------------------

#. Go to the **Sparkflows application** and **log in** with your credentials.
#. Navigate to **Administration -> Configurations -> Module**.
#. Find the setting **module.enableCodeLibrary** and set it to **true**.

Step 2 : Access the Code Library
-------------------------------

#. Go to the **Administration** Page.
#. Navigate to the **Operations** section. Once enabled, the **Code Library** option will be visible under the **Operations** section as shown below:

   .. figure:: ../../_assets/code-library/admin-code-library.png
      :alt: code library
      :width: 60%

#. Click on the **Code Library** card to be redirected to the **Code Libraries List page**.

   .. figure:: ../../_assets/code-library/code-library-list.png
      :alt: code-library-list
      :width: 60%



Step 3 : Create the Code Library
-------------------------

#. Navigate to the **Code Libraries List page** as described above.
#. Click the **Add Code Library** button located in the top-right corner.
#. Fill in the Required Details. A pop-up will appear prompting you to provide the following information:
    
    * **Library Name:** Enter the code to be used in the workflow node.
    * **Description:** Provide a name or brief description of the code library.
    * **Engine:** Specify the type of code written in the library (e.g., Scala, SQL).
    * **Group:** Specify the group if the code library is being created for a specific group.

   .. figure:: ../../_assets/code-library/create-code-library.png
      :alt: code-library-create
      :width: 60%

Step 4 : Execute Code Library
-------------------------
#. On the Workflow Editor page, the user will be able to see the Code Library node as illustrated below.

   .. figure:: ../../_assets/code-library/code-library-node.png
      :alt: code-library-node
      :width: 60%

#. By clicking the Execute button, the user can run the workflow, which will execute the code from the selected code library.

    .. figure:: ../../_assets/code-library/code-library-scala-execution.png
      :alt: code-library-scala-execution
      :width: 60%

    .. figure:: ../../_assets/code-library/code-library-sql-execution.png
         :alt: code-library-sql-execution
         :width: 60%


#. Code library node can be executed in interactive mode aswell.

   .. figure:: ../../_assets/code-library/code-library-interactive-execution.png
            :alt: code-library-sql-execution
            :width: 60%

Export and Import of code library
----------------------------------

Sparkflows supports user to export and import of a code library

#. On clicking the **Export** button in the code library list table, a JSON file will be downloaded to the system

   .. figure:: ../../_assets/code-library/code-library-export.png
               :alt: code-library-export
               :width: 60%

   .. figure:: ../../_assets/code-library/code-library-exported.png
                  :alt: code-library-exported
                  :width: 60%
#. Once the code library is exported, users can import it by clicking the **Import** button and selecting the exported JSON file. They can then execute the code library.

   .. figure:: ../../_assets/code-library/code-library-import-button.png
                  :alt: code-library-import-button
                  :width: 60%

   .. figure:: ../../_assets/code-library/code-library-import.png
                  :alt: code-library-import
                  :width: 60%
