H2O GLRM
--------

Generalized Low Rank Models (GLRM) is an algorithm for dimensionality reduction of a dataset. It is a general, parallelized optimization algorithm that applies to a variety of loss and regularization functions. Categorical columns are handled by expansion into 0/1 indicator columns for each level. With this approach, GLRM is useful for reconstructing missing values and identifying important features in heterogeneous data.

You can find the details at the H2O website : https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glrm.html

Below are parameters which can be specified in the H2O GLRM processor:

.. list-table:: H2O GLRM
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - K
     - Specify the rank of matrix approximation.
   * - IGNORED COLUMNS
     - Specify the column or columns to be excluded from the model: Class
   * - IGNORE CONST COLS
     - Specify whether to ignore constant training columns : true
 
.. figure:: ../../../../_assets/model/h2o/4.PNG
   :alt: H2O GLRM
   :width: 90%
