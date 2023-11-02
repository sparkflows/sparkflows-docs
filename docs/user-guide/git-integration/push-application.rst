Push Application
=================

Sparkflows allows for changes to application to be pushed to a configured Git repo. Progress made on application can also be saved to be pushed onto Git at any given time. All previously saved application can be accessed via revision history. 

This document provides detailed steps on how to push applications onto remote Git repos, save applications to be pushed at a later day, and view the previous saved versions of applications.


Step 1 : Check the Pre-requisites
-----------
#. **Git Configuration:** Ensure that Git is enabled and properly configured within Sparkflows. Refer to `this link <https://docs.sparkflows.io/en/latest/user-guide/git-integration/git-configuration.html>`_ for detailed instructions.

#. **Linking Projects with Git:** Before pushing your Application to a Git repository, make sure you have successfully linked the concerned project with Git. Detailed steps can be found `here. <https://docs.sparkflows.io/en/latest/user-guide/git-integration/link-project.html>`_ 

Step 2 : Login to Fire Insights
-----------------
#. Go to Fire Insights Home Page.
#. Enter your credentials.
#. Click **Sign in** to reach the Dashboard.

Step 3 : Open Concerned Project    
---------------------------
Open the project containing the Application to be pushed. Follow the below steps :

#. From the Dashboard, click **PROJECTS** located on the top navigation bar.
#. On the Projects Page, search and select the concerned project.

   Alternatively, you can search and select the project using the search panel located on top navigation bar.

Step 4 : Open Edit Analytics Application Page
---------------------
#. From the Projects Page, Click **Applications** button located on the top-middle bar.
#. Open the Application using **Edit App** option.
   
   .. figure:: ../../_assets/git/edit-app.png
      :alt: PushApplication
      :width: 60%

   
Step 5 : Push Application to Git
---------------
#. On the Edit Analytics App Page, click **Save and Push to Git** button.

   .. figure:: ../../_assets/git/git_application.png
      :alt: PushApplication
      :width: 60%

#. Write the **Commit message** in the text box provided and click the **Push** button.

   .. figure:: ../../_assets/git/git_application_commitmsg.png
      :alt: PushApplication
      :width: 60%

   A success message will be displayed as shown below:

   .. figure:: ../../_assets/git/git_application_savemsg.png
      :alt: PushApplication
      :width: 60% 

   **Note:** In our example, on success the Application JSON file gets pushed into below path:  

   rootFolderPath/Projects/analytics_app/Example_Application.json
