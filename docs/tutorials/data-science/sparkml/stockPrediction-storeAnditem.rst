Stock Prediction For Each Store & Item
======================================

This workflow to predict the stock for each store & iteam by using linear regression & loop nodes.
Loop nodes takes in store & item fields and pass the data to liner regression model in a loop.

Workflow
--------

The below workflow:

* Reads data from a given path.
* Extracts day, month & year from date.
* Assembles features for modelling.
* Selects the store & item field in loop node to filter the data for each store & item and pass the data to model node.
* Splits the dataset.
* Uses LinearRegression Node to create the ML model.
* Makes prediction on future data.
* Uses RegressionEvaluator Node to evaluate the predictions.
* ModelSummary for each combination of store & item.


   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/WF.png
      :alt: Stock Prediction
      :width: 75%

Reading from Dataset
---------------------

It reads the sample Dataset File.

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/read-config.png
      :alt: Stock Prediction
      :width: 75%
   
Processor Output
^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/read-output.png
      :alt: Stock Prediction
      :width: 75%
  
  
Date and Time Field Extract
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/date-time-config.png
      :alt: Stock Prediction
      :width: 75%

VectorAssembler
^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/vector-assembler-config.png
      :alt: Stock Prediction
      :width: 75%


LoopDistinctValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Node to loop through the data for distinct values in the selected columns.

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/execute-in-loop-config.png
      :alt: Stock Prediction
      :width: 75%
   
LinearRegression
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Fitting the line with Regression model.

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/linear-regression-config.png
      :alt: Stock Prediction
      :width: 75%
   
ModelSummary
^^^^^^^^^^^^^
ModelSummary for each combination of values in the selected fields.
Summary can be saved and analyzed.


   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/model-summary.png
      :alt: Stock Prediction
      :width: 75%


ModelPrediction and Evalaution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Predict on test data & evaluate.

   .. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/regression-evaluator-config.png
      :alt: Stock Prediction
      :width: 75%
