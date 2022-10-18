Push Workflow
================

Sparkflow allows for changes to workflows to be pushed onto a configured git repo. Progress made on workflows can also be saved to be pushed onto Git at
a later time. All previously saved workflows can be accessed via revision history. This document provides information on how to push workflows onto remote
git repos, save workflows to be pushed at a later day, and view the previous saved versions of a workflow. 

Commit and Push Workflows to Remote Git Repos
-------------------------------------------------------

When you have added new workflow or made changes to existing workflows, you can directly push the changes to Git.

- Go to create/ Edit workflow page.
- Create or edit your workflow.
- Click on the ``SAVE AND PUSH TO GIT`` button.
- Write the ``Commit message`` on the modal textarea.
- Click on the ``PUSH`` button

*SAVE AND PUSH TO GIT*


.. figure:: ../../_assets/git/save_push.PNG
   :alt: PushWf
   :width: 60%
  
*Commit Messsage*
 
 
.. figure:: ../../_assets/git/commit-msg.png
   :alt: PushWf
   :width: 60%
   

*On Success*


.. figure:: ../../_assets/git/success-commit.png
   :alt: PushWf
   :width: 60% 

On success, you will get success message.

Saving Workflows Outside of Git
---------------

- Click on the ``SAVE NEW VERSION`` button.
- Add comment.
- Click ``OK`` to save the new version of workflow.

.. figure:: ../../_assets/git/save-newVersion-comment.png
   :alt: PushWf
   :width: 60% 

Viewing All Workflow Saves and Pushing a Particular Save to Git
---------------
- Click the ``three vertical dots`` at the right corner
- Select ``Revision History`` to get a list of the previous saves
- Click on the ``Git-icon`` to push the selected version of workflow.
- Write the ``Commit message`` on the modal textarea.
- Click on the ``PUSH`` button

*Workflows History*

.. figure:: ../../_assets/git/git-history.PNG
   :alt: PushWf
   :width: 60% 

*Saved Workflow Versions*

.. figure:: ../../_assets/git/savedwfVersions.png
   :alt: PushWf
   :width: 60% 
  
*Commit message*
  
.. figure:: ../../_assets/git/commit-msg.png
   :alt: PushWf
   :width: 60% 
   

*On Success*

.. figure:: ../../_assets/git/success-commit.png
   :alt: PushWf
   :width: 60% 

On success, you will get success message.

Workflow json file get pushed in path : rootFolderPath/Projects/pipelines/test.json
