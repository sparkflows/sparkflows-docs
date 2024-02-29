Models Lifecycle Actions
===================

Users can trigger the actions to register, deploy, promote, undeploy and re-register models from the Model Management Dashboard. The actions are executed in Sparkflows MLOps server. 

**Configure MLflow in Admin Console:**

- Users can now see the additional MLOps Actions in the model page.

**Register Model:** 

- This action will register and log the model to MLflow server. This copies the model from Sparkflows model repo to MLflow model storage which most often is a cloud store like S3.

**Deploy Model:**

- Once the model is registered with MLflow, it can be deployed by choosing the deploy model option. This action would give an end point which can be used to perform online scoring. The details of the same using python and curl command can be seen by clicking on the View icon in the Actions list.

**Undeploy Model:**

- A deployed model can be undeployed by choosing this option. This would destroy the scoring endpoint as well. But the model will continue to persist in the Sparkflows model repo and the MLflow model store.

**Promote Model:**

- A model can be promoted and demoted among one of these stages using this option - Staging, Production, Archived, None. The default stage model is registered is “None”.
