H2O GBM
========

This workflow performs H2O’s GBM sequentially builds regression trees on all the features of the Bike Sharing Dataset in a fully distributed way - each tree is built in parallel.
   
Workflow
-------

The below workflow:

* Read the Bike Sharing Dataset.
* Split the dataset for training and test.
* Perform sequentially builds regression trees using H2O GBM.
* Score the test dataset using the model created.
* Print the results.

.. figure:: ../../../_assets/tutorials/machine-learning/h2o-gbm/1.PNG
   :alt: H2O GBM
   :width: 90%

H2O GBM Configuration
---------------------

* select RESPONSE COLUMN
* select RESPONSE COL CATEGORICAL : it specifies a response column type (numeric or categorical) Separates the Classification and Regression.
* select IGNORE CONST COLUMNS : Specify whether to ignore constant training columns.
* select IGNORED COLUMNS : Specify the column or columns to be excluded from the model.

.. figure:: ../../../_assets/tutorials/machine-learning/h2o-gbm/2.PNG
   :alt: H2O GBM
   :width: 90%

Results
---------------------

Once the above workflow is getting Executed, Below details can be seen on Execution page.

.. figure:: ../../../_assets/tutorials/machine-learning/h2o-gbm/3.PNG
   :alt: H2O GBM
   :width: 90%
   
.. figure:: ../../../_assets/tutorials/machine-learning/h2o-gbm/4.PNG
   :alt: H2O GBM
   :width: 90%   
   
.. figure:: ../../../_assets/tutorials/machine-learning/h2o-gbm/5.PNG
   :alt: H2O GBM
   :width: 90%   
