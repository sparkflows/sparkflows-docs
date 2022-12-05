Git Configuration
===================

A User must input a personal access token as well as their GitHub Username and Password in order to push workflows and pipelines. The document below describes the process to enable Git integration in Sparkfows and configure it.

Enable Git Repository
----------------------

- Click Administration.
- Select Configurations. 
- Click on ``GIT`` tab
- Make ``git.enable`` true.
- Provide the git repository link in ``git.url`` value field.
- Provide the git root folder in ``git.rootFolder`` value field, it's default value is ``/ProjectsWorkflow``.
- Save the configuration.
- Refresh the browser to enable git-configuration.

.. figure:: ../../_assets/git/git_configurations.PNG
   :alt: GitEnable
   :width: 60%


Configure Git Credentials
--------------------------------------------

- On the right corner, click on the nine squares.
- Select ``Git Configuration``.
- Git preferences dialog will appear.
- Provide User Name for Github account. 
- Provide the Token/Password for github account. 

.. figure:: ../../_assets/git/git-cred-token.png
   :alt: GitCredentials
   :width: 60%


Clicking ``Test Credential`` will give the following result:

.. figure:: ../../_assets/git/git-cred-success.png
   :alt: Success
   :width: 60%

.. note:: Make sure that Git repository url should be accessible from Fire Insights machine
