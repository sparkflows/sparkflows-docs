H2O Neural-Networks
-------------------

H2O’s Deep Learning is based on a multi-layer feedforward artificial neural network that is trained with stochastic gradient descent using back-propagation. The network can contain a large number of hidden layers consisting of neurons with tanh, rectifier, and maxout activation functions. Advanced features such as adaptive learning rate, rate annealing, momentum training, dropout, L1 or L2 regularization, checkpointing, and grid search enable high predictive accuracy. 

For more details, visit the H2O website at: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/deep-learning.html

Below are the required parameters which can be specified in the H2O Neural-Networks processor:

.. list-table:: H2O Neural-Networks
   :widths: 20 80
   :header-rows: 1

   * - Parameters
     - Description
   * - RESPONSE COLUMN
     - Select Response Column.
   * - IS RESPONSE COL CATEGORICAL
     - Choose the type of response column. It can be either numeric corresponding to Regression or categorical corresponding to Classification.
   * - FEATURE COLUMNS
     - Specify the column or columns to be included for feature.
   * - FOLD COLUMN
     - Specify a column to use as the fold.
   * - WEIGHTS COLUMN
     - Specify a column to use for the observation weights, which are used for bias correction.
     
.. figure:: ../../../../_assets/model/h2o/6.PNG
   :alt: H2O Neural-Networks
   :width: 90%   
   
For more details on other parameters, visit: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/deep-learning.html#defining-a-deep-learning-model

