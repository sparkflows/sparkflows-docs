ModelDoc Guide
=================

ModelDoc Overview
----------------

The ModelDoc feature is designed to automatically create machine learning documentation for individual models trained in Sparkflows. This editable document provides an overview of the experiment and includes important details such as dataset information, final model performance metrics, lineage, and the nodes used. 

To download and view a sample experiment report in Word format, `click here <https://drive.google.com/uc?export=download&id=1ihIlIMV6IAm_eJY3myLMHmYaQXDie5ga>`_.


Generating a ModelDoc
---------------------

There are two ways to generate ModelDoc:

* By choosing the ModelDoc option corresponding to a model from the Model Repo page under the Actions menu.

    .. figure:: ../_assets/modeldoc-guide/2.png
       :alt: ModelDoc
       :width: 60%
* By opening the model details of a particular model and then clicking on the ModelDoc option in the Model Information section on the left.
  
    .. figure:: ../_assets/modeldoc-guide/1.png
       :alt: ModelDoc
       :width: 60%

ModelDoc Structure and Template
-------------------------------
Model Details 
+++++++++
This section captures the final details of the model trained on the dataset.

System Specifications
++++++++++
This section details the Sparkflows VM specification on which the model was built and trained on.

Description
++++++++++++
This section captures the description of the workflow used to train the model

Workflow Nodes
++++++++++++++++
This section shows the details of the nodes which are used in the workflow along with a brief detail of each of the nodes.

Dataset Overview
++++++++++++++++
This section lists the datasets which were used to build the workflow and train the model.

Model Path
+++++++++++
This shows the path on the disk or on cloud storage where the model was persisted to.

Model Summary
+++++++++++++++
This shows the hyperparameters of the trained models. These are the parameters from the final epoch of training.

Features
+++++++++
Below is the list of features which was used to train the model. These can be either raw features or features created by the data scientist and subsequently fed into the model. These features would have been created either in this training workflow or in the previous workflow if multiple workflows are chained together to build the usecase.

Train Metrics
+++++++++++++
This section shows the training metrics of the final epoch of training. There are different metrics captured for models.

Feature Importance
++++++++++++++++++
This section shows the feature importance of all the features which were used for training the model in tabular format.

Test Metrics
+++++++++++++
This section shows the test metrics on the validation dataset. There are different metrics captured for models.
