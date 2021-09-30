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
* select the store & item field in loop node to filter the data for each store & item and pass the data to model node.
* Splits the dataset.
* Uses LinearRegression Node.
* Makes prediction on future data.
* Uses RegressionEvaluator Node.
* ModelSummary for each combination of store & item.


.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/1.png
   :alt: Stock Prediction
   :width: 100%

Reading from Dataset
---------------------

It reads the sample Dataset File.

Processor Configuration
^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/2.png
   :alt: Stock Prediction
   :width: 100%
   
Processor Output
^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/2a.png
   :alt: Stock Prediction
   :width: 100%
  
  
Date and Time Field Extract
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/3.png
   :alt: Stock Prediction
   :width: 100%

VectorAssembler
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/4.png
   :alt: Stock Prediction
   :width: 100%


LoopDistinctValue
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Node to loop through the data for distinct values in the selected columns.

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/5.png
   :alt: Stock Prediction
   :width: 100%
   
LinearRegression
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Fitting the line with Regression model.

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/6.png
   :alt: Stock Prediction
   :width: 100%
   
ModelSummary
^^^^^^^^^^^^^
ModelSummary for each combination of values in the selected fields.
Summary can be saved and analyzed.


.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/7.png
   :alt: Stock Prediction
   :width: 100%


ModelPrediction and Evalaution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Precdcit on test data & evaluate.

.. figure:: ../../../_assets/tutorials/machine-learning/stock-prediction-store-iteam/8.png
   :alt: Stock Prediction
   :width: 100%
