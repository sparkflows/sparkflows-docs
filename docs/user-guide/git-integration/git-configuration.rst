Git Configuration
===================

The document below describes the process to enable and configure Git in Sparkfows. The authentication can be configured either via token or username and password.

Enable Git Repository
----------------------

- Login as ``Admin``
- Click on ``Administration`` from the top menu
- Select ``Configurations``
- Click on ``GIT`` tab
- Set the property ``git.enabled`` to true
- Provide the git repository link in ``git.url`` field. Eg: https://github.com/sparkflows/fire-tools.git
- Provide the git root folder in ``git.rootFolder`` field. Default value is ``/ProjectsWorkflow``
- Click on ``Save configurations``
- Refresh the browser for configurations to reflect

.. figure:: ../../_assets/git/git_configurations.PNG
   :alt: GitEnable
   :width: 60%


Configure Git Credentials
--------------------------------------------

- Click on the Waffle icon (nine squares) on the top right corner
- Click on ``Git Configuration``. Will take you to the ``Git Configuration`` dialogue.
- Provide ``Username`` for the Git account. 
- Provide the ``Token/Password`` for Git account. (For GitHub, one needs to enter the Token. For GitLab, one can enter either the password or token) 

.. figure:: ../../_assets/git/git-cred-token.png
   :alt: GitCredentials
   :width: 60%


Clicking ``Test Credential`` will give the following response on success. If there was a change to the exisiting credentials, one needs to click ``Update`` and then ``Close``:

.. figure:: ../../_assets/git/git-cred-success.png
   :alt: Success
   :width: 60%

.. note:: Make sure that Git repository url should be accessible from Sparkflows machine
