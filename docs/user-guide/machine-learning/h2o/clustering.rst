Clustering
==========

Sparkflows provides the following processors to perform Clustering using H2O.

H2O K-means
----------

K-means falls in the general category of clustering algorithms. Clustering is a form of unsupervised learning that tries to find structures in the data without using any labels or target values. Clustering partitions a set of observations into separate groupings such that an observation in a given group is more similar to another observation in the same group than to another observation in a different group.

For more details, visit the H2O website at: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/k-means.html

Below are the details needed on H2O K-means processor:

.. list-table:: H2O K-means
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
   :alt: H2O Cluster
   :width: 80%
   
For more details on other parameters, visit: https://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/k-means.html#defining-a-k-means-model   
