Git Status
==========

Sparkflows can show the changes yet to be pushed to git via the ``Git Status`` Button. 

To access ``Git status``, open a project and select ``Workflows``. You would see a page similar to below.

.. figure:: ../../_assets/git/git_wf_status.PNG
   :alt: git-status
   :width: 60%

When ``Git Status`` is clicked you would be redirected to another page where you can see the list of workflows that have not been pushed to git. You would see a page similar as below

.. figure:: ../../_assets/git/git-status-list.png
   :alt: git-status
   :width: 60%

Upon clicking the workflow name you would see Workflow json differences between the current state and last workflow json pushed to git similar to below. If the workflow has not been pushed to git before, a pop up would show up stating ``There is no previous version available to show the diff``.

.. figure:: ../../_assets/git/git-status-json-differences.png
   :alt: git-status
   :width: 60%

- To see the differences in workflow form click the ``Workflow`` tab. 

.. figure:: ../../_assets/git/git-status-wf-differences.PNG
   :alt: git-status
   :width: 60%

- If there are no differences to show the  message ``No diff to show!`` is shown.

.. figure:: ../../_assets/git/git-status-no-differences.png
   :alt: git-status
   :width: 60%
