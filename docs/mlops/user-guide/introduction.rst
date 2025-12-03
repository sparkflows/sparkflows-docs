Introduction
======
This guide provides an overview of how Sparkflows enables seamless **model serving—both offline (batch) and online (real-time)** along with step-by-step **instructions for accessing, managing, and deploying** machine learning models within the platform.

Model serving refers to the process of deploying a machine learning model into a production environment so it can make predictions based on real-time or batch data. This is a critical step in the lifecycle of a machine learning project because it moves the model from a development phase into a live environment where it can generate value.

Sparkflows saves all the models trained in its model repository by default. It also captures all the training and validation metrics. The model artifacts are saved on local disk or in cloud storage by Sparkflows. External models can also be imported into Sparkflows and served.

These models can be served in one of the following two ways: 

* Offline Model Serving
* Online Model Serving

Offline Model Serving
---------
**Purpose:** Offline model serving is used for batch scoring, allowing machine learning models to process large volumes of data in a non-real-time, batch-oriented fashion.

**Usage:** It is ideal for bulk prediction tasks, enabling efficient processing of extensive datasets during scheduled or periodic operations.

**Key Features:** Exhibits high throughput, making it well-suited for scenarios prioritizing data processing efficiency and scalability over immediacy.

Online model serving
--------------
**Purpose:** Online model serving is designed for scoring streaming data, enabling machine learning models to make real-time predictions as new data arrives.

**Usage:** It supports real-time model deployment, delivering predictions immediately upon receiving new data.

**Key Features:**

* Offers low latency, which is critical for applications requiring rapid responses, such as fraud detection, recommendation systems, and conversational AI.
* Processes a relatively smaller number of rows of data at a time, focusing on speed and accuracy rather than bulk processing.  

Accessing and Managing Models in Sparkflows
-----
Sparkflows provides an intuitive interface to manage all models—whether trained within Sparkflows or imported from external sources. Follow the steps below:

**Step 1 : Accessing the ML Models Page**
++++++++++++++++++++++++++++++++++++++++++++++
* Login to Sparkflows with your credentials.
* Navigate to the **Models** menu and choose **All Models** from the dropdown to view the list of available models, as shown below:

  .. figure:: ../../_assets/mlops/models-menu.png
     :alt: Model Info
     :width: 70%


**Step 2 : Viewing the List of Saved Models**
++++++++++++++++++++++++++++++++++++++++++++++++++
* After clicking on **All Models**, you will see a table listing all the trained models, as shown below: 

  .. figure:: ../../_assets/mlops/models-list-page.png
     :alt: Model Info
     :width: 70%

**Step 3 : Managing the Models**
++++++++++++++++++++++++++++++++++
* Click on the **three-dot** icon in the **Actions** column, as shown below to perform various model-related operations: 
  
  .. figure:: ../../_assets/mlops/model-options.png
     :alt: Model Info
     :width: 70%
  
  * **Deploy Model:** Push model into a production-ready state
  * **Download:** Export the model artifacts
  * **Associate Scoring Workflow:** Link model to a scoring pipeline
  * **ModelDoc:** View documentation and metadata of the model























