Anomaly Detection
===============

Sparkflows provides the below processors for performing Anomaly Detection using H2O.
     
H2O Isolation Forest
----------

Isolation Forest is similar in principle to Random Forest and is built on the basis of decision trees. Isolation Forest, however, identifies anomalies or outliers rather than profiling normal data points. Isolation Forest isolates observations by randomly selecting a feature and then randomly selecting a split value between the maximum and minimum values of that selected feature.

For more details, visit the H2O website at: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/glm.html

Below are the required parameters which can be specified in the H2O Isolation Forest processor:

.. list-table:: H2O Isolation
   :widths: 20 80
   :header-rows: 1

   * - Parameters
     - Description
   * - RESPONSE COLUMN
     - Select Response Column.
   * - IS RESPONSE COL CATEGORICAL
     - Choose the type of response column. It can be either numeric corresponding to Regression or categorical corresponding to Classification.
   * - OFFSET COLUMN
     - Specify a column to use as an offset, this value cannot be similar to the value of weights column.
   * - WEIGHTS COLUMN
     - Specify a column to use for the observation weights, which are used for bias correction. The specified weights column must be included in the specified training frame.  
   * - IGNORE CONST COLUMNS
     - Specify whether to ignore constant training columns.
   * - IGNORED COLUMNS
     - Specify the column or columns to be excluded from the model. 
     
.. figure:: ../../../_assets/model/h2o/5.PNG
   :alt: H2O Isolation
   :width: 90%
   
For more details on other parameters, visit: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/if.html#defining-an-isolation-forest-model

