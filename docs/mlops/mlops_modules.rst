MLOps Modules
==========

Model Management Dashboard
-----
It provides a centralized interface to manage the lifecycle of all machine learning models across projects and workflows.

* **Explore and Search Models :** Locate models across different projects and workflows.
* **View Metadata and Metrics :** Access detailed information about each model including training metrics, metadata, input/output schema, tags, etc.
* **Compare Models :** Side-by-side comparison of multiple models based on performance, version, and other metadata.
* **Model Lifecycle Actions :** Register models, Promote to production, Undeploy or re-register, Archive or delete models. 
* **Trigger Lifecycle Operations :** Actions executed via the Sparkflows MLOps server directly from the dashboard.
* **Champion–Challenger Support :** Compare challenger models with current production (champion) models to determine promotion readiness.
* **A/B Testing Support**

  * Configure parallel model inference pipelines
  * Evaluate outputs via dashboards and statistical analysis
  * Promote based on comparative performance
* **Model Registry & Integration**

  * Native Model Registry with full versioning and lineage tracking
  * Integrated with MLflow to log Experiments, Metrics, Artifacts, Model versions

`Learn More <https://docs.sparkflows.io/en/latest/mlops/user-guide/model_management_dashboard.html>`_

Model Deployment and Serving
----
It enables scalable deployment and inference of models in both batch and real-time environments, including cloud-native infrastructure.

Model Deployment Options
+++++
Sparkflows offers a unified interface for managing deployments across environments and  support for various deployment targets.

- Single Pane-of-Glass for deployment, monitoring and management.
- Support for various deployment targets.

`Learn More <https://docs.sparkflows.io/en/latest/mlops/user-guide/model_deployment.html>`_

* **Unified Deployment Interface :** Deploy models built inside or outside Sparkflows from a centralized UI.
* **ETL Pipeline Integration :** 450+ pre-built processors for Data preparation, Feature engineering, Model inference. Inference embedded directly within Spark-based ETL workflows and leverages Apache Spark for distributed execution.

Model Serving
+++++
The models in Sparkflows can be served as one of the two options:

**1. Offline Model Serving**

* MLOps offline serving is primarily employed for batch scoring, allowing machine learning models to process large volumes of data in a non-real-time, batch fashion.
* It is utilized for bulk prediction tasks, enabling the efficient processing of extensive datasets with machine learning models in scheduled or periodic operations.
* Offline model serving typically exhibits high throughput, making it well-suited for scenarios where data processing efficiency and scalability are paramount.

`User Guide <https://docs.sparkflows.io/en/latest/mlops/user-guide/offline-model-serving.html>`_

**2. Online Model Serving**

* MLOps online serving is primarily employed for scoring streaming data, ensuring that machine learning models can make predictions in real-time as new data arrives.
* It offers low latency, enabling immediate model predictions, which is crucial for applications requiring rapid responses to incoming data.
* Online model serving facilitates real-time model deployment, allowing predictions to be served as soon as new data becomes available.
* It is typically used on a relatively smaller number of rows of data at a time, making it suitable for applications where low latency is essential but data volumes are modest.

  .. figure:: ../_assets/mlops/8_Model_Serving.png
         :alt: Model Serving
         :width: 70%

`User Guide <https://docs.sparkflows.io/en/latest/mlops/user-guide/online-model-serving.html>`_

Model Monitoring and Observability
-----
It supports real-time observability of model behavior, performance, and reliability in production, ensuring that deployed models remain effective.
      
* **Dashboards :** Visualize accuracy, latency, throughput, and model health and Built-in dashboards for tracking inference outcomes.
* **Inference Logging :** Logs stored in time-series databases and Enables historic trend analysis and drift detection
* **Anomaly & Drift Detection :** Automatic detection of concept/data drift  and Triggers alerts for model performance degradation. Here the user needs to specify the drift threshold of PSI (default is 0.3) and the count of rows drifted, after which retraining should get triggered.

  `Learn More <https://docs.sparkflows.io/en/latest/mlops/user-guide/model_observability_retraining.html>`_

* **Alerting Mechanism :** Configurable alerts for Performance drops, Unexpected outputs, Data quality issues.

`Learn More <https://docs.sparkflows.io/en/latest/mlops/user-guide/model_monitoring.html>`_


Model Security & Governance
-----
It enforces enterprise-grade governance, access control, transparency, and compliance with regulatory and organizational standards.

* SSO (Single Sign-On) and Role-Based Access Control (RBAC) for secure, personalized access
* **Secure Hosting & API Exposure :** Models hosted securely with restricted access and proper authentication

* **Model Explainability :** Built-in features to understand and audit model decisions (important for regulated industries)
* **Audit Trails :** Maintain logs for every model action—registration, deployment, updates, and undeployment
* **Compliance Enablement**

  * Track metadata, lineage, usage
  * Transparent documentation of model behavior and changes
* **Permission Management**

  * Fine-grained access for teams, roles, and projects
  * Secure sharing of model endpoints and results





