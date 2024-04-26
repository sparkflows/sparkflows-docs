Models Lifecycle Actions
===================

Users can trigger the actions to register, deploy, promote, undeploy and re-register models from the Model Management Dashboard. The actions are executed in Sparkflows MLOps server. 

**Configure in Admin Console:**

- Users can now see the additional MLOps Actions in the model page. Configure the properties to leverage MLOps capabilities.

**Register Model:** 

- This action will register and log the model to MLflow server. This registers the model residing in Sparkflows model repo to MLflow model storage which most often is a cloud store like S3.

**Deploy Model:**

- Once the model is registered with MLflow, it can be deployed by choosing the deploy model option. Once the model is deployed, user gets an end point which can be used to perform online scoring. The details of the same using python and curl command can be seen by clicking on the View icon in the Actions list.

**Undeploy Model:**

- A deployed model can be undeployed by choosing this option. This would destroy the scoring endpoint as well. But the model will continue to persist in the Sparkflows model repo and the MLflow model store.

**Promote Model:**

- A model can be promoted and demoted among one of these stages using this option - Staging, Production, Archived, None. The default stage model is registered is “None”.

**Champion-Challenger Model:**

- Multiple Challenger models can be attached to the Champion(deployed in production) model to be evaluated over a period of time. When a scoring request comes to the Champion model, the request is serviced by the Champion model and the request is re-routed to the Challenger models as well. The Challenger models can be evaluated over a period of time and if they perform better than the Champion model, then the Challenger model can be deployed to production and the current Champion model can be Undeployed.
