H2O
===

.. panels::
    :container: container-lg pb-3

    :doc:`/user-guide/machine-learning/h2o/building-h20-workflows`
    
    Building H2O workflows
    
    ---

    :doc:`/user-guide/machine-learning/h2o/clustering`

    Clustering using H2O
    
    ---

    :doc:`/user-guide/machine-learning/h2o/regression-classification`

    Regression & Classification using H2O
    

   
.. list-table:: H2O Processors in Fire Insights
   :widths: 20 80
   :header-rows: 1

   * - Title
     - Description
   * - H2O DRF
     - Distributed Random Forest (DRF) is a powerful classification and regression tool. When given a set of data, DRF generates a forest of classification or regression trees, rather than a single classification or regression tree.
   * - H2O K-Means
     - K-Means falls in the general category of clustering algorithms. Clustering is a form of unsupervised learning that tries to find structures in the data without using any labels or target values. Clustering partitions a set of observations into separate groupings such that an observation in a given group is more similar to another observation in the same group than to another observation in a different group.
   * - H2O GBM
     - Gradient Boosting Machine (for Regression and Classification) is a forward learning ensemble method. The guiding heuristic is that good predictive results can be obtained through increasingly refined approximations. H2O’s GBM sequentially builds regression trees on all the features of the dataset in a fully distributed way - each tree is built in parallel.
   * - H2O GLRM
     - Generalized Low Rank Models (GLRM) is an algorithm for dimensionality reduction of a dataset. It is a general, parallelized optimization algorithm that applies to a variety of loss and regularization functions. Categorical columns are handled by expansion into 0/1 indicator columns for each level. With this approach, GLRM is useful for reconstructing missing values and identifying important features in heterogeneous data.
   * - H2O GLM
     - Generalized Linear Models (GLM) estimate regression models for outcomes following exponential distributions. In addition to the Gaussian (i.e. normal) distribution, these include Poisson, binomial, and gamma distributions. Each serves a different purpose, and depending on distribution and link function choice, can be used either for prediction or classification. 
   * - H2O XGBoost
     - XGBoost is a supervised learning algorithm that implements a process called boosting to yield accurate models. Boosting refers to the ensemble learning technique of building many models sequentially, with each new model attempting to correct for the deficiencies in the previous model. In tree boosting, each new model that is added to the ensemble is a decision tree. XGBoost provides parallel tree boosting (also known as GBDT, GBM) that solves many data science problems in a fast and accurate way. For many problems, XGBoost is one of the best gradient boosting machine (GBM) frameworks today.


   
.. toctree::
   :hidden:

   building-h20-workflows.rst
   clustering.rst
   regression-classification/index.rst
   
