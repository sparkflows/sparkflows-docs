Sparkflows Reference Architecture
=================================

Overview
--------

Sparkflows provides a flexible architecture for designing, executing, and managing data engineering, analytics, and machine learning workflows.

The platform combines a web-based visual interface, an application server, and a configurable execution environment to support end-to-end data processing workflows.

Sparkflows can be deployed on standalone machines, virtual machines, or Kubernetes clusters and can leverage Apache Spark clusters for distributed data processing.

Core Architecture Components
----------------------------

The Sparkflows architecture consists of three primary components:

1. Web Browser – User Interface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sparkflows provides a web-based, drag-and-drop interface that enables users to design, configure, and execute data workflows without writing extensive code.

The interface allows users to:

* **Design Workflows:** Build end-to-end data pipelines using a visual workflow designer.
* **Access Processing Nodes:** Use built-in nodes for data ingestion, data profiling, data cleaning, ETL, natural language processing (NLP), optical character recognition (OCR), and machine learning.
* **Configure Workflows:** Define data sources, transformations, processing logic, and execution parameters.
* **Execute and Monitor Workflows:** Submit workflows for execution and view execution status, logs, and results.
* **Explore Data:** Preview datasets and inspect intermediate workflow outputs during development.

The browser serves as the primary interaction layer between users and the Sparkflows platform.

2. Sparkflows Web Server – Application and Orchestration Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Sparkflows web server serves as the central application component, managing interactions between the user interface and the underlying workflow execution environment.

The web server can be deployed on a standalone machine, virtual machine, or Kubernetes cluster, depending on the infrastructure requirements.

Its key responsibilities include:

* **Workflow Management:** Manage workflow definitions, configurations, and execution requests.
* **Execution Orchestration:** Process workflow execution requests and submit jobs to the configured execution environment.
* **Interactive Execution:** Support interactive workflow development, testing, and execution.
* **Schema Management:** Perform schema inference and propagate schema information between workflow nodes.
* **User Access Management:** Manage user permissions and role-based access to platform resources.
* **Integration Management:** Support connectivity with configured data sources and external processing services.
* **Execution Monitoring:** Collect execution information and make workflow results, status, and logs available through the user interface.

The Sparkflows web server acts as the coordination layer between workflow design and execution.

3. Apache Spark Cluster – Distributed Processing Layer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sparkflows integrates with Apache Spark to execute data processing workflows across distributed computing resources.

When configured to use an Apache Spark cluster, Sparkflows submits workflows as Spark jobs to the connected execution environment.

Apache Spark handles the distributed execution of supported data processing operations, enabling workflows to process larger datasets and utilize computing resources across multiple nodes.

Sparkflows can integrate with supported Apache Spark environments, including:

* Standalone Apache Spark clusters
* Amazon EMR
* AWS Glue
* Azure HDInsight
* Google Cloud Dataproc
* Databricks
* Apache Spark clusters running within supported Hadoop environments

The processing environment can be hosted on-premises or in the cloud, depending on the organization's infrastructure.

For smaller workloads and development environments, Sparkflows also supports local execution without requiring a separate distributed Apache Spark cluster.

Workflow Execution Architecture
-------------------------------

Sparkflows separates workflow design and management from the underlying data processing environment.

A typical workflow execution follows these steps:

#. **Workflow Design:** Users create and configure workflows through the Sparkflows web interface using the available processing nodes.

#. **Workflow Submission:** When a workflow is executed, the browser sends the execution request to the Sparkflows web server.

#. **Execution Coordination:** The web server processes the request, applies the workflow configuration, and submits the job to the configured execution environment.

#. **Workflow Processing:** The execution environment processes the workflow using local computing resources or a distributed Apache Spark cluster, depending on the deployment configuration.

#. **Execution Monitoring:** The Sparkflows web server receives execution information, including status, logs, and results, from the processing environment.

#. **Results Visualization:** Execution information and workflow results are made available through the web interface, allowing users to monitor progress and inspect outputs.

This architecture allows users to develop workflows through a consistent interface while choosing the execution environment best suited to their processing requirements.

Deployment Architecture
-----------------------

Sparkflows supports multiple deployment configurations to accommodate different development and enterprise environments.

Standalone Deployment
~~~~~~~~~~~~~~~~~~~~~

In a standalone deployment, Sparkflows is installed on a local machine or dedicated server.

Workflow execution takes place on the same machine, making this configuration suitable for development, testing, proof-of-concept implementations, and smaller data processing workloads.

Distributed Deployment
~~~~~~~~~~~~~~~~~~~~~~

In a distributed deployment, the Sparkflows web server runs independently of the Apache Spark processing cluster.

The web server manages workflow requests and submits jobs to the connected cluster, which performs the distributed data processing operations.

This configuration is suitable for organizations that require larger-scale processing capabilities or want to leverage existing cloud or on-premises Apache Spark infrastructure.

Cloud and Kubernetes Deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sparkflows can be deployed on supported cloud infrastructure or Kubernetes clusters, providing flexibility in how the application is hosted and managed.

Depending on the configuration, the Sparkflows application can connect to supported external processing environments such as Amazon EMR, Azure Databricks, or Google Cloud Dataproc.

This allows organizations to align Sparkflows deployment with their existing infrastructure and operational requirements.

Architecture Benefits
---------------------

The Sparkflows architecture provides several advantages:

* **Flexible Deployment:** Deploy Sparkflows across local, on-premises, and cloud-based infrastructure.
* **Scalable Processing:** Leverage distributed Apache Spark clusters for workloads that require additional computing resources.
* **Separation of Responsibilities:** Manage workflow design and orchestration independently from distributed data processing.
* **Interactive Development:** Design, test, and monitor workflows through a unified visual interface.
* **Integration with Existing Infrastructure:** Connect Sparkflows to supported data sources, cloud services, and Apache Spark environments.
* **Centralized Workflow Management:** Configure, execute, and monitor workflows from a common platform.

Next Steps
----------

To learn more about the available infrastructure configurations, refer to the :doc:`/installation/deployment-overview/deployment-options` guide.

For environment-specific setup instructions, refer to the relevant Sparkflows installation and configuration documentation.

See also:

* :doc:`/installation/installation/index`
* :doc:`/installation/requirements-sizing/index`
