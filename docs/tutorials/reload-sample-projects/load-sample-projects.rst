Loading Sample Projects
=============================

This tutorial explains the process of loading sample projects.

This feature of load sample projects allows the user to load the data from any path configured by admin. It also provides the user to create projects that are private and accessible only to them."

The steps for the same are as follows:

Step 1 :  Configure the Path
----------------------------------
#. **Login** to Fire Insights.

   .. figure:: ../../_assets/tutorials/load-sample-project/Login.png
      :alt: Load Sample Projects
      :width: 65% 

Navigate to Administration->Configurations, as shown below.





Search the variable app.sampleDataPath and then enter the path of the folder where the data for sample projects has been stored.


And then click on save the configurations.






Step 2 : Now navigate to project tab and click on Reload sample project.



It will then show a pop-up where in the path configured by the admin is being displayed.



Click on submit to reload the projects.


Step 3: Now  under the project tab in projects list page , we can see a sample projects tab , which shows all the reloaded sample projects.



Step 4 : On the project list page , Click on the Load Sample Project button to load a single project.
Step 5 : If the user tries to load the project which is already present, it will show an error message below the text box.





Step 6 : To proceed further, the user can give a new project name after clicking on the sample project which already exists


And then it will show the loaded project in All tab of the Projects List page




UPDATE SAMPLE DATA PATH AND RELOAD SAMPLE PROJECTS.

Step 1 :  Navigate to the administration tab and then click on the sample projects.


The text box beside the update sample data path button will reflect the path which is being set in the configuration by admin.



Step 2 : Now to update the sample data path , update the desired path and then click on the update sample data path button .
This updated data path will also be saved in the configuration now.





Step 3: Now if we click on the Drop All Sample Projects.

All the sample projects would be deleted and the tab Sample Projects in Project List page will not be seen








Step 4 : Now if we click on the Drop And Reload All Sample Projects.

 It would drop all the current sample projects and reload all the sample projects again




Step :5 To reload only the required sample projects, we can select the sample projects to be loaded and then click on Reload Selected Sample Projects.








WHEN THE SAMPLE DATA PATH IS EMPTY

If the sample data path variable `app.sampleDataPath` is set to empty , it would take the path as /data. 




 Note : The sample data path can be set to empty only through configurations.


