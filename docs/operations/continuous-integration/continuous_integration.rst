Job Configuration
------------

1. Create and Configure a Jenkins Job to listen to the Workflows Development Git branch.

2. Configure the Jenkins Job to run a deployment script to copy the Workflows to a target QA Environment

3. Configure the Jenkins Job  to execute the workflow against the target QA Environment

4. Schedule the Jenkins Job to run at a specific time


Job Trigger and Execution
--------------

1. Push a Workflow from a Sparkflows Editor to the Git branch

2. Jenkins Job should be executed both bt Git Commit trigger and the scheduled trigger.

3. The deployment script should be executed to copy the workflow into the target QA

4. The workflow test script should be executed to run the corresponding jobs in the target QA.


CI/CD Process Flow
--------------



.. figure:: ../../_assets/operationalization/sparkflows_ci_cd_process.png
   :alt: Continuous Integration
   :width: 60%
