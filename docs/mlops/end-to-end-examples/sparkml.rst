SparkML
====

This document describes how to implement end-to-end MLOps for SparkML models in Sparkflows, covering training, evaluation, champion model selection, prediction workflows, and continuous monitoring using MLflow and built-in drift metrics.

Create the Training Workflow 
---------------------------------------

#. **Start a new Workflow**: Create a new workflow in Sparkflows and give it a meaningful name (e.g., ``SparkML_Train_Churn_Model``).
#. **Read Data**: Use a Read node (e.g., ``Read CSV``, ``Read JDBC``) to ingest your training dataset.
#. **Data Preprocessing (Optional but Recommended)**: Add necessary nodes for data cleaning, feature engineering, and transformation (e.g., ``Imputer``, ``StringIndexer``, ``VectorAssembler``).
#. **Split Data**: Use the Split node to divide your data into training and testing sets (e.g., 80% for training, 20% for testing).
#. **Train Model**:

   - Add a SparkML training algorithm node (e.g., ``Random Forest Classifier``, ``Logistic Regression``).
   - Connect the training split output to this node.

#. **Evaluate Model**:

   - Add the Evaluator node.
   - Connect the model output and the testing split output to the Evaluator.

#. **Crucial Step**: Ensure the Champion Model Selection is toggled to ``False``.
#. **Crucial Step**: Enable the Prediction over time and set the model type to populate the Predictions over Time Graph under the Models Page.
#. **Predict/Score**:

   - Add the Predict/Score node.
   - Connect the model output and the testing split output to this node.

#. **Crucial Step**: Ensure the Champion Model Selection is toggled to ``False``.
#. **ML Data Metrics**:

   - Add the ML Data Metrics node.
   - Connect the output of the Predict/Score node to this node.

#. **Crucial Step**: Ensure the Champion Model Selection is toggled to ``False``.
#. **Save**: Use the Spark ML Model Save node to explicitly save the trained model. 

   .. Note:: The model gets registered with MLflow automatically, but this ensures a clean save point.)


Run the Training Workflow
----

The Training Model gets registered with MLflow automatically, as shown below.

.. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/sparkml-training-wf.png
   :alt: MLOps Examples
   :width: 70%

.. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/predict-node-config.png
   :alt: MLOps Examples
   :width: 70%

.. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/model-registration-success.png
   :alt: MLOps Examples
   :width: 70%



The trained model is visible on the models page, as shown below.


.. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/trained-model-on-models-page.png
   :alt: MLOps Examples
   :width: 70%


The training workflow's runs will be tracked in MLflow and can be found under the experiment name: **PROJECT NAME - WORKFLOW NAME**.

.. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/track-training-wf-runs.png
   :alt: MLOps Examples
   :width: 70%

To designate your champion model, use the **champion button** to toggle the selection.


.. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/champion-model-toggle.png
   :alt: MLOps Examples
   :width: 70%




Create a Prediction Workflow
----------------------------

#. **Start a new Workflow**: Create a new workflow in Sparkflows and give it a meaningful name (e.g., ``SparkML_Predict_Churn_Model``).
#. **Read Data**: Use a Read node to ingest the *unseen* data you wish to score/predict.
#. **Data Preprocessing**: Apply the exact same preprocessing and transformation steps used in the training workflow to the new, unseen data.
#. **Load Model**:

   - Add the Spark ML Model Load node.

#. **Crucial Step**: Ensure the Champion Model Selection is toggled to ``True`` to load the currently designated champion model.
#. **Predict/Score**:

   - Add the Predict/Score node.
   - Connect the output of the Load Model node and the preprocessed data to this node.

#. **Crucial Step**: Ensure the Champion Model Selection is toggled to ``True``.
#. **ML Data Metrics (Optional for real-time predictions, recommended for batch scoring)**:

   - Add the ML Data Metrics node.
   - Connect the output of the Predict/Score node to this node.

#. **Crucial Step**: Ensure the Champion Model Selection is toggled to ``True``.
#. **Write Results**: Use a Save node (e.g., ``Save CSV``, ``Save JDBC``) to save the prediction results.

   .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/prediction-wf.png
      :alt: MLOps Examples
      :width: 70%

   .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/prediction-nodes-config.png
      :alt: MLOps Examples
      :width: 70%


Associate the Prediction Workflow with the Training Workflow
----------------

By clicking **Associate Scoring Workflow**, prediction workflow can be associated with the training workflow. Follow the below steps for the same:

* First, select the desired prediction workflow and confirm your choice.
* Next, execute the selected prediction workflows using your new, unseen test data.

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/scoring-wf-association.png
     :alt: MLOps Examples
     :width: 70%


Model Monitoring and Drift
-------------------------

Sparkflows MLOPS features provide comprehensive monitoring capabilities:

#. **Performance Over Time**: The Predictions over Time Graph (enabled in the training workflow's Evaluator node) displays model performance metrics as the model scores new data over time using the associated prediction workflow.

#. **Data Drift**: The ML Data Metrics node in the prediction workflow calculates key metrics, including:

    - **Data Drift Over Time**: Compares the statistical distribution of input features in the new data against the training data.
    - **Average Drift Over Time**: Compares the distribution of predictions on the new data against the predictions made during training.
    - **Metric Thresholds**: Alerts can be configured based on defined thresholds for these drift metrics, notifying users when the model is decaying.

#. **Metrics Over Time**: Track the model's test metrics over time using unseen datasets. Additionally, monitor the volume of data utilized during batch prediction.



Finally, continuously monitor all relevant metrics over time.

* Data Drift Over Time

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/data-drift-over-time.png
     :alt: MLOps Examples
     :width: 70%

* Average Drift Over Time

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/avg-drift-over-time.png
     :alt: MLOps Examples
     :width: 70%

* Prediction Over Time - Classification

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/prediction-over-time-1.png
     :alt: MLOps Examples
     :width: 70%

* Prediction Over Time - Clustering

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/prediction-over-time-2.png
     :alt: MLOps Examples
     :width: 70%

* Prediction Over Time - Regression

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/prediction-over-time-3.png
     :alt: MLOps Examples
     :width: 70%

* Metrics Over Time 

  .. figure:: ../../_assets/mlops/end-to-end-examples/sparkml/metrics-over-time.png
     :alt: MLOps Examples
     :width: 70%






























