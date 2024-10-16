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
      :alt: workflow execution cleanup
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
      :alt: workflow execution cleanup
      :width: 60%


