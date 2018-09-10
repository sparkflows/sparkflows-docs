LDA
=========== 

LDA is given a collection of documents as input data, via the featuresCol parameter. Each document is specified as a Vector of length vocabSize, where each entry is the count for the corresponding term (word) in the document

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ml.NodeLDA

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      * - Name
        - Title
        - Description
      * - featuresCol
        - Features Column
        - Features column of type vectorUDT for model fitting.
      * - k
        - K
        - The number of topics to create.
      * - maxIter
        - Max Iterations
        - The maximum number of iterations.
      * - optimizer
        - Optimizer
        - Optimizer or inference algorithm used to estimate the LDA model.
      * - topicDistributionCol
        - TopicDistributionColumn
        - Output column with estimates of the topic mixture distribution for each document
      * - checkpointInterval
        - checkpointInterval
        - The checkpoint interval (>= 1) or disable checkpoint (-1). E.g. 10 means that the cache will get checkpointed every 10 iterations.
      * - subsamplingRate
        - subsamplingRate
        - Fraction of the corpus to be sampled and used in each iteration of mini-batch gradient descent, in range (0, 1].
      * - seed
        - Seed
        - Random Seed.
      * - maxTermsPerTopic
        - MaxTermsPerTopic
        - Number of Terms in Topics




