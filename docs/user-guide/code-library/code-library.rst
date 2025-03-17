Code Library
=============

Code Library is a centralized repository where users can write, store, and manage reusable code components. These components can be written in SQL and Scala, allowing for flexibility in how they can be applied.

Key Features
-----------

Reusable Components: 
++++++++++++

Code written in the library can be reused across different workflows, making it easy to share common logic and processes between groups and users.

Support for Multiple Languages: 
++++++++++++++++++

Users can write code in SQL for database queries and Scala for more complex logic or processing tasks, offering versatility based on the specific needs of each workflow.
Collaboration Across Groups and Users: The code library can be accessed and utilized by different groups and users, promoting collaboration and efficiency. Each group or user can leverage the pre-existing code components in their own workflows without duplicating effort.

Streamlined Workflows:
++++++++++++++++++

By using reusable code components from the library, users can simplify and speed up the creation of workflows, reducing redundancy and potential errors. 

This document provides you the step-by-step instructions to enable, access, and create a Code Library within Sparkflows.

Step 1 : Enable the Code Library
--------------------------

#. Go to the **Sparkflows application** and **log in** with your credentials.
#. Navigate to **Administration -> Configurations -> Module**.
#. Find the setting **module.enableCodeLibrary** and set it to **true**.

Step 2 : Access the Code Library
-------------------------------

#. Go to the **Administration** Page.
#. Navigate to the **Operations** section and click on **Code Library** card, as shown below. (Once enabled the setting in step 1, the **Code Library** option will be visible under the 
   **Operations** section.)

   .. figure:: ../../_assets/code-library/admin-code-library.png
      :alt: code library
      :width: 60%

#. By clicking on **Code Library** you are directed to the **Code Libraries List page**, as shown below.

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
#. On the Workflow Editor page, you will be able to see the Code Library node as illustrated below.

   .. figure:: ../../_assets/code-library/code-library-node.png
      :alt: code-library-node
      :width: 60%

#. By clicking the Execute button, you can run the workflow, which will execute the code from the selected code library.

   .. figure:: ../../_assets/code-library/code-library-scala-execution.png
      :alt: code-library-scala-execution
      :width: 60%

   .. figure:: ../../_assets/code-library/code-library-sql-execution.png
         :alt: code-library-sql-execution
         :width: 60%


#. Code library node can be executed in interactive mode as well, as shown below.

   .. figure:: ../../_assets/code-library/code-library-interactive-execution.png
            :alt: code-library-sql-execution
            :width: 60%

Export and Import of code library
----------------------------------

Sparkflows supports users in exporting and importing a code library. Follow the steps below for the process:

#. On clicking the **Export** button in the code library list table, a JSON file will be downloaded to the system, as shown below.

   .. figure:: ../../_assets/code-library/code-library-export.png
               :alt: code-library-export
               :width: 60%

   .. figure:: ../../_assets/code-library/code-library-exported.png
                  :alt: code-library-exported
                  :width: 60%
#. Once the code library is exported, you can import it by clicking the **Import** button and selecting the exported JSON file. They can then execute the code library.

   .. figure:: ../../_assets/code-library/code-library-import-button.png
                  :alt: code-library-import-button
                  :width: 60%

   .. figure:: ../../_assets/code-library/code-library-import.png
                  :alt: code-library-import
                  :width: 60%
