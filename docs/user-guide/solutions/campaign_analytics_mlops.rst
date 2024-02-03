
Model Dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sparkflows Model Dashboard allows users to 
- explore and search models created by different workflows in different projects by different users.
- view model details
- check performance metrics
- compare multiple models
- perform various actions like register with MLOps server, deploy into endpoint, track model serving, monitor model and data drifts and define retraining policy.

View Model Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Sparkflows allows users to drill down into a specific Model Run and view the Model Summary, Feature Importance, Training Metrics, Test Metrics, Confusion Matrix, ROC curve and other info.

Perform MLOps Actions
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Users can trigger the actions to register, deploy, promote, undeploy and re-register models from the Model Management Dashboard. 
The actions are executed in Sparkflows MLOps server

Model Serving
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Scripts for Online Scoring and Batch Scoring can be viewed in the Model Management Dashboard. 

Model Monitoring 
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Once the model is deployed, Sparkflows monitoring module, keeps a check on different metrics over a period of time.

Model Observability & Retraining 
^^^^^^^^^^^^^^^^^^^^^^^^^^^
A policy can be attached to the model to trigger auto-retraining. This policy can be of types:
- time based: The auto-retraining will kick in at a particular time of day/month etc.
- model drift-based: Here the user needs to specify the drift threshold of PSI (default is 0.3) and the count of rows drifted, after which retraining should get triggered.

