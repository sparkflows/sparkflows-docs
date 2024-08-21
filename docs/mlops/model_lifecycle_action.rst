Models Lifecycle Actions
===================

Users can trigger the actions to register, deploy, promote, undeploy and re-register models from the Model Management Dashboard. The actions are executed in Sparkflows MLOps server. 

**Register Model:** 

- By default, all models are registered in internal Model repository of Sparkflows. If you need a specific model to be registered to MLflow, this action can be used. This would register the model residing in Sparkflows model repo to MLflow model repository.

**Deploy Model:**

- Once the model is registered, it can be deployed by choosing the deploy model option. The whole pipeline of feature engineering and model scoring gets deployed. The model can be deployed to one of the target systems like Kubeflow, Sagemaker, MLflow among others. On deployment, user gets an end point which can be used to perform online scoring. The details of the same using python and curl command can be seen by clicking on the View icon in the Actions list.

**Undeploy Model:**

- A deployed model can be undeployed by choosing this option. This would destroy the scoring endpoint as well. But the model will continue to persist in the Sparkflows model repo and the MLflow model repository.

**Promote Model:**

- A model can be promoted and demoted among one of these stages using this option - Staging, Production, Archived, None. The default stage model is registered is “None”.

**Champion-Challenger Model:**

- Multiple Challenger models can be attached to the Champion(deployed in production) model to be evaluated over a period of time. When a scoring request comes to the Champion model, the request is serviced by the Champion model and the request is re-routed to the Challenger models as well. The Challenger models can be evaluated over a period of time and if they perform better than the Champion model, then the Challenger model can be deployed to production and the current Champion model can be Undeployed.
