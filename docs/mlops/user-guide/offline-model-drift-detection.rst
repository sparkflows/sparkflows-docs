Offline Model Drift Detection
====
Sparkflows provides comprehensive offline model and feature drift detection capabilities, enabling users to monitor data and model behavior over time, detect distribution shifts, and maintain model reliability in production.

Feature Drift Detection with Sparkflows
----
As machine learning models move from training to production, the data they encounter can evolve over time. When the distributions of individual features change significantly compared to the original training data, it is known as **feature drift**.

Feature drift can reduce model accuracy and reliability if left unchecked. Sparkflows provides a simple yet powerful way to **detect**, **measure**, and **visualize** feature drift so you can stay ahead of potential issues.

How Sparkflows Enables Feature Drift Detection
++++

**1. Collecting Feature Statistics**
****

Sparkflows automatically computes detailed statistics for both numeric and categorical features in your dataset:

  - **Numeric Features:** Mean, range, standard deviation, and more.
  - **Categorical Features:** Frequency and proportion of each category.

This ensures a clear baseline understanding of your data.

.. figure:: ../_assets/mlops/ml-data-metrics/node-ml-data-metrics.png
     :alt: Model Metrics
     :width: 70%

For more details on ML Data Metrics node, refer below document:

https://docs.sparkflows.io/en/latest/mlops/user-guide/model-monitoring/node-ml-data-metrics.html

**2. Baseline vs. Batch Comparison**
****
When a training dataset is available, Sparkflows establishes it as the **baseline** for comparison. Any new dataset (batch) can then be evaluated against this baseline to detect shifts in feature distributions.

.. figure:: ../_assets/mlops/ml-data-metrics/baseline-feature-statistics.png
     :alt: Model Metrics
     :width: 70%


**3. Measuring Feature Drift**
****

To quantify drift, Sparkflows uses metrics such as the **Population Stability Index (PSI)**, which measures how much feature distributions deviate over time.

  - High PSI values indicate significant drift.
  - Low PSI values mean the feature remains stable.

This makes it easy to pinpoint which features require attention.

.. figure:: ../_assets/mlops/ml-data-metrics/numeric-feature-drift-metrics.png
     :alt: Model Metrics
     :width: 70%


.. figure:: ../_assets/mlops/ml-data-metrics/categorical-feature-drift-metric.PNG
     :alt: Model Metrics
     :width: 70%


**4. Visual Reports and Metrics Tables**
****

Sparkflows generates interactive reports to help you analyze drift effectively:

- **Feature Drift Over Time:** Graphs showing changes for individual features across multiple batches.


 .. figure:: ../_assets/mlops/ml-data-metrics/drift-over-time.png
     :alt: Model Metrics
     :width: 70%

- **Average Feature Drift Over Time:** Aggregate drift score combining all features into a single view.

 .. figure:: ../_assets/mlops/ml-data-metrics/average-drift-over-time.png
     :alt: Model Metrics
     :width: 70%


With these visualizations, you can quickly understand where and when drift is occurring.

Model Drift Detection with Sparkflows
----

Sparkflows enables continuous monitoring of model performance by tracking test and evaluation metrics over time, helping identify potential model drift with ease.

Model Metrics over Time
++++
To track how a model’s performance evolves over time, Sparkflows provides a feature that continuously updates and displays key performance metrics.

**Initial Test Metrics**
****
When a model is trained, Sparkflows helps computes the test metrics at the time of training, (via Evaluator nodes or Score node in case of H2O). These metrics are displayed on the model’s page under the **Test Metrics** section.

  - These initial metrics form the **first data point** in the **Model Metrics over Time** graph.
  - This helps establish a baseline for evaluating future performance changes.

**Updating Metrics with Evaluator Nodes**
****
After deployment, users often have new data with labels and predictions. To keep the performance graph updated:

1. Use the **Evaluator Nodes** to compute metrics from the new label and prediction columns.

2. Each Evaluator Node provides an option to enter the **model UUID**.


 .. figure:: ../_assets/mlops/ml-data-metrics/node-regression-evaluator.png
     :alt: Model Metrics
     :width: 70%

3. When the model UUID is provided, the system updates the **Model Metrics over Time** graph for that specific model. Users can view the graph for individual metrics by selecting the desired metric from the dropdown menu.


 .. figure:: ../_assets/mlops/ml-data-metrics/metrics-over-time-graph.png
     :alt: Model Metrics
     :width: 70%




















