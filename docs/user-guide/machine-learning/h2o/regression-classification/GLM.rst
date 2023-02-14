H2O GLM
-------

Generalized Linear Models (GLM) estimate regression models for outcomes following exponential distributions. In addition to the Gaussian (i.e. normal) distribution, these include Poisson, binomial, and gamma distributions. Each serves a different purpose, and depending on distribution and link function choice, can be used either for prediction or classification.

For more details, visit the H2O website at: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glm.html

Below are the required parameters which can be specified in H2O GLM processor:

.. list-table:: H2O GLM
   :widths: 20 80
   :header-rows: 1

   * - Parameters
     - Description
   * - RESPONSE COLUMN
     - select Response Column.
   * - IS RESPONSE COL CATEGORICAL
     - Choose the type of response column. It can be either numeric corresponding to Regression or categorical corresponding to Classification.
   *  - OFFSET COLUMN
      - Specify a column to use as an offset, this value cannot be similar to the value of weights column.
   *  - WEIGHTS COLUMN
      - Specify a column to use for the observation weights, which are used for bias correction. The specified weights column must be included in the specified training frame.
   * - IGNORE CONST COLUMNS
     - Specify whether to ignore constant training columns.
   * - IGNORED COLUMNS
     - Specify the column or columns to be excluded from the model. 
     
.. figure:: ../../../../_assets/model/h2o/5.PNG
   :alt: H2O DRF
   :width: 75%
   
For more details on other parameters, visit: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glm.html#defining-a-glm-model
   
   
