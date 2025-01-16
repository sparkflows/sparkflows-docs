Introduction
======

Understanding MLOps and Its Purpose
********
**Definition**

* It is a set of best practices and tools designed to streamline and automate the end-to-end machine learning lifecycle.
* It Bridges the gap between data science and IT operations.

**Core Goals**

* Efficient deployment of machine learning models.
* Continuous monitoring and maintenance of models in production.

**Key Components**

* Version Control: Manages versioning for both models and data to ensure traceability.
* CI/CD Pipelines: Facilitates continuous integration and continuous delivery for rapid iteration and deployment.
* Automated Testing: Verifies the performance and functionality of models before deployment.
* Performance & Drift Monitoring: Tracks model performance and detects drift to ensure reliability over time.

**Benefits**

By implementing MLOps, organisations can get following benefits:

* Accelerates Development: Reduces time spent on manual processes.
* Minimizes Errors: Identifies and resolves issues proactively.
* Ensures Model Reliability: Keeps models effective and up-to-date with changing data trends.

**Sparkflows and MLOps Integration**

* Model Deployment using Sparkflows MLOps: Enables deployment of various machine learning models.
* Model Compatibility: Supports models either built within Sparkflows or allows onboarding and serving of models built outside Sparkflows.

**MLOps Architecture:**

.. figure:: ../_assets/mlops/1_MLOps_Arch.png
   :alt: MLOps Architecture
   :width: 70%

**MLOps Modules**
***********************

Sparkflows MLOps Offering is bundled with various built-in capabilities as explained below:

- Model Management Dashboard
- Model Deployment and Serving
- Model Security & Governance
- Model Monitoring and Observability

`Learn More <https://docs.sparkflows.io/en/latest/mlops/mlops_modules.html>`_


**Model Management Dashboard**
***********************

Sparkflows Model Management Dashboard includes following Actions:

- Explore and search models created by different workflows in different projects by different users.
- View model details.
- Check performance metrics.
- Compare multiple models.
- Perform various actions like register with MLOps server, deploy into endpoint, track model serving, monitor model and data drifts and define retraining policy.

`Learn More <https://docs.sparkflows.io/en/latest/mlops/model_management_dashboard.html>`_

**Model Lifecycle Actions**
***********************

Users can trigger the actions to register, deploy, promote, undeploy and re-register models from the Model Management Dashboard. The actions are executed in Sparkflows MLOps server. 

`Learn More <https://docs.sparkflows.io/en/latest/mlops/model_lifecycle_action.html>`_

**Model Deployment Options**
***********************

- Single Pane-of-Glass for deployment, monitoring and management.
- Support for various deployment targets.

`Learn More <https://docs.sparkflows.io/en/latest/mlops/model_deployment.html>`_

**Model Serving**
***********************

The models in Sparkflows can be served as one of the two options:

#. **Offline Model Serving**

    * MLOps offline serving is primarily employed for batch scoring, allowing machine learning models to process large volumes of data in a non-real-time, batch fashion.
    * It is utilized for bulk prediction tasks, enabling the efficient processing of extensive datasets with machine learning models in scheduled or periodic operations.
    * Offline model serving typically exhibits high throughput, making it well-suited for scenarios where data processing efficiency and scalability are paramount.

`User Guide <https://docs.sparkflows.io/en/latest/mlops/user-guide/offline-model-serving.html>`_


#. **Online Model Serving**
   
    * MLOps online serving is primarily employed for scoring streaming data, ensuring that machine learning models can make predictions in real-time as new data arrives.
    * It offers low latency, enabling immediate model predictions, which is crucial for applications requiring rapid responses to incoming data.
    * Online model serving facilitates real-time model deployment, allowing predictions to be served as soon as new data becomes available.
    * It is typically used on a relatively smaller number of rows of data at a time, making it suitable for applications where low latency is essential but data volumes are modest.

      .. figure:: ../_assets/mlops/8_Model_Serving.png
         :alt: Model Serving
         :width: 70%

`User Guide <https://docs.sparkflows.io/en/latest/mlops/user-guide/online-model-serving.html>`_



**Model Monitoring**
***********************

Once the model is deployed, Sparkflows monitoring module, provides the detailed info on environment, deployment type, deployment mode, problem type, alerts and all the metrics needed to keep a check on how model is being used and is performing over a period of time. 


`See Details <https://docs.sparkflows.io/en/latest/mlops/model_monitoring.html>`_

**Model Observability & Retraining**
***********************

A policy can be attached to the model to trigger auto-retraining. This policy can be of types:

- Time based: The auto-retraining will kick in at a particular time of day/month etc.
- Model-drift based: Here the user needs to specify the drift threshold of PSI (default is 0.3) and the count of rows drifted, after which retraining should get triggered.

`Learn More <https://docs.sparkflows.io/en/latest/mlops/model_observability_retraining.html>`_

**Model Security & Governance**
***********************

Sparkflows ensures the following security measures.

- Data Privacy & Protection
- Secure Model Hosting
- Single Sign-On( SSO )
- Transparency and Explainability
- Robustness and Reliability
- Governance and Auditing
- User Controls
- Permissions and Secure Sharing

`Learn More <https://docs.sparkflows.io/en/latest/mlops/model_security.html>`_


.. toctree::
   :hidden:

   mlops_modules.rst
   model_management_dashboard.rst
   model_lifecycle_action.rst
   model_deployment.rst
   user-guide/offline-model-serving.rst
   user-guide/online-model-serving.rst
   model_monitoring.rst
   model_observability_retraining.rst

   



