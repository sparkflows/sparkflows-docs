Push Pipeline
================

Sparkflows allows to directly push changes made to new or existing pipelines onto Git. The steps to push changes to git are detailed below. 

Commit and push Pipeline to the remote Git repository
-------------------------------------------------------


- Go to create/Edit ``Pipeline`` page.
- Select the ``Pipeline`` you wish to save and push to git.
- Click on the ``Save and push to git`` button.


.. figure:: ../../_assets/git/git_pipeline.PNG
   :alt: PushWf
   :width: 60%
   
   *Save and push to git*
   
   
- Write the ``Commit message`` on the modal textarea.


 
 
.. figure:: ../../_assets/git/git_commitmsg.PNG
   :alt: PushWf
   :width: 60%
   
   *Commit Messsage*

- Click on the ``Push`` button


.. figure:: ../../_assets/git/git_pipeline_savemsg.PNG
   :alt: PushWf
   :width: 60% 

   *On Success*
   


Workflow json file get pushed in path : rootFolderPath/Projects/pipelines/test.json
