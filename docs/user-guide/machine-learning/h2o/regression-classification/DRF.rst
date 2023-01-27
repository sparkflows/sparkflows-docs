H2O DRF
-------

Distributed Random Forest (DRF) is a powerful classification and regression tool. When given a set of data, DRF generates a forest of classification or regression trees, rather than a single classification or regression tree. Each of these trees is a weak learner built on a subset of rows and columns. More trees will reduce the variance. Both classification and regression take the average prediction over all of their trees to make a final prediction, whether predicting for a class or numeric value. (Note: For a categorical response column, DRF maps factors (e.g. ‘dog’, ‘cat’, ‘mouse) in lexicographic order to a name lookup array with integer indices (e.g. ‘cat -> 0, ‘dog’ -> 1, ‘mouse’ -> 2.).

For more details, visit the H2O website at: http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/drf.html

Below are the required parameters which can be specified in the H2O DRF processor:

.. list-table:: H2O DRF
   :widths: 20 80
   :header-rows: 1

   * - Parameters
     - Description
   * - RESPONSE COLUMN
     - Select Response Column.
   * - IS RESPONSE COL CATEGORICAL
     - Choose the type of response column. It can be either numeric corresponding to Regression or categorical corresponding to Classification.
   * - IGNORE CONST COLUMNS
     - Specify whether to ignore constant training columns.
   * - IGNORED COLUMNS
     - Specify the column or columns to be excluded from the model.
     
.. figure:: ../../../../_assets/model/h2o/1.PNG
   :alt: H2O DRF
   :width: 90%

For more details on other parameters, visit: http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/drf.html#defining-a-drf-model  
