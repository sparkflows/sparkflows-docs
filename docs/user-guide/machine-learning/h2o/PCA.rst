PCA
====
Principal Components Analysis (PCA) is closely related to Principal Components Regression. The algorithm is carried out on a set of possibly collinear features and performs a transformation to produce a new set of uncorrelated features.

You can find the details at the H2O website : https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/pca.html

Below are details which can be needed on H2O PCA processor:

.. list-table:: H2o PCA
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - K
     - Specify the number of clusters (group of data) in a dataset that are similar to each other.
   * - IGNORED COLUMNS
     - Specify the column or columns to be excluded from the model. 
   * - IGNORE CONST COLUMNS
     - Specify whether to ignore constant training columns.
     
.. figure:: ../../../_assets/model/h2o/2.PNG
   :alt: H2O PCA
   :width: 90%
   
other parameters: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/pca.html#defining-a-pca-model
