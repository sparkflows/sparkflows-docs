H2O GBM
-------

Gradient Boosting Machine (for Regression and Classification) is a forward learning ensemble method. The guiding heuristic is that good predictive results can be obtained through increasingly refined approximations. H2O’s GBM sequentially builds regression trees on all the features of the dataset in a fully distributed way - each tree is built in parallel.

You can find the details at the H2O website : https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/gbm.html

Below are required parameters which can be specified in the H2O GBM processor:

.. list-table:: H2O GBM
   :widths: 20 80
   :header-rows: 1

   * - Parametrs
     - Description
   * - RESPONSE COLUMN
     - select RESPONSE COLUMN
   * - IS RESPONSE COL CATEGORICAL
     - Specify a response column type (numeric or categorical) Separates the Classification and Regression.
   * - IGNORE CONST COLUMNS
     - Specify whether to ignore constant training columns.
   * - IGNORED COLUMNS
     - Specify the column or columns to be excluded from the model. 


.. figure:: ../../../../_assets/model/h2o/3.PNG
   :alt: H2O GBM
   :width: 90%

other parameter: http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/gbm.html#defining-a-gbm-model
