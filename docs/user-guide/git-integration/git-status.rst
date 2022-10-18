Git Status
==========

Sparkflows can show the changes yet to be pushed to git via the ``Git Status`` Button. 

To access ``Git status``, open a project and select ``Workflows``. You should see a page similar to below.

.. figure:: ../../_assets/git/git_wf_status.PNG
   :alt: git-status
   :width: 60%

When ``Git Status`` is clicked you should be redirected to another page where we can see the list of workflows that have not been pushed to linked git configuration. You should see a page similar to below

.. figure:: ../../_assets/git/git-status-list.png
   :alt: git-status
   :width: 60%

Upon clicking the workflow name you should see Workflow json differences of existing workflow changes which has not been pushed to git and last workflow json changes whcih has been pushed to configured git, similar to below.

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
