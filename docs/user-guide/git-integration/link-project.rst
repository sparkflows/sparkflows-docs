Link project with Git
===================

Sparkflows allows for created projects to be linked with git via the ``Link With Git`` button. You must link projects with git in order to push workflows to a configured git. When this button is clicked there are two options: To link a project to an existing branch and to create a new branch. This document goes over how to link projects both ways. 

.. figure:: ../../_assets/git/link-project.png
   :alt: link-with-git
   :width: 60%

Existing Branch
----------------------

- Click on ``EXISTING BRANCH`` option.
- Select branch from list 
- Provide root folder path
   If no link is provided it will get linked with the path added in the git configurations
- Click link.

.. figure:: ../../_assets/git/git_existing_branch.PNG
   :alt: link-with-git
   :width: 60%

Create New Branch
----------------------

- Click on ``CREATE NEW BRANCH`` option.
- Add ORIGIN
- Add the NEW BRANCH NAME
- Add the root folder path
   If no link is provided it will get linked with the path added in the git configurations
- When you click on link button in this option it will first create branch with specified NEW BRANCH NAME. New branch is updated with specified ORIGIN.

.. figure:: ../../_assets/git/git_new_branch.PNG
   :alt: link-with-git
   :width: 60%

Successfully Linked Project with Git. Now, you can push workflows under Project to linked branch.
