ML Data Metrics
=====
Sparkflows provides a node to analyze and monitor datasets used in machine learning models. It focuses on understanding how data is distributed and whether the current dataset is drifting away from the original training (baseline) data.

ML Data Metrics Node
----
**Node ML Data Metrics** does the following:

- Summarizes important characteristics of the data (averages, ranges, category counts, etc.).
- Compares the day's dataset with past baseline data.
- Detects changes (drift) that might signal problems for model accuracy.
- Produces reports that are easy to visualize and interpret.


Node Configuration
++++

 .. figure:: ../../../_assets/mlops/ml-data-metrics/ml-data-metrics-node.png
     :alt: Model Metrics
     :width: 70%

* To attach this node to the **algorithm node** while training the model:

  * ``Model UUID``: Leave blank in the training workflow as this would be picked up from the passed model.
  * ``Numeric Columns``: Select the feature columns which are numeric (having discrete or continuous values) from the dropdown.
  * ``Categorical Columns``: Select the columns which have categorical data.

* To attach this node while **scoring/prediction** workflow:

  * ``Model UUID``: Enter the UUID that was generated at the time of model training.
  * ``Numeric Columns``: Select the feature columns which are numeric (having discrete or continuous values) from the dropdown.
  * ``Categorical Columns``: Select the columns which have categorical data.


Workflow
++++

* While creating the Training Workflow

 .. figure:: ../../../_assets/mlops/ml-data-metrics/model-metrics-workflow.png
     :alt: Model Metrics
     :width: 70%

* While creating the Scoring/Prediction Workflow

 .. figure:: ../../../_assets/mlops/ml-data-metrics/scoring-workflow.png
     :alt: Model Metrics
     :width: 70%

Node Output
++++

- Data Summaries → Numeric and categorical statistics of the current dataset.

 .. figure:: ../../../_assets/mlops/ml-data-metrics/baseline-feature-statistics.png
     :alt: Model Metrics
     :width: 70%

 .. figure:: ../../../_assets/mlops/ml-data-metrics/batch-feature-statistics.png
     :alt: Model Metrics
     :width: 70%

 .. figure:: ../../../_assets/mlops/ml-data-metrics/categorical-feature-drift-metrics.png
     :alt: Model Metrics
     :width: 70%

 .. figure:: ../../../_assets/mlops/ml-data-metrics/numeric-feature-drift-metrics.png
     :alt: Model Metrics
     :width: 70%

- Drift Reports → Clear indicators of which features have shifted over time.

 .. figure:: ../../../_assets/mlops/ml-data-metrics/drift-over-time.png
     :alt: Model Metrics
     :width: 70%

 .. figure:: ../../../_assets/mlops/ml-data-metrics/average-drift-over-time.png
     :alt: Model Metrics
     :width: 70%

































