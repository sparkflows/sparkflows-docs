H2OWord2Vec
=========== 

H2O Word2Vec

Input
--------------
It takes in a DataFrame as input

Type
--------- 

transform

Class
--------- 

fire.nodes.h2o.NodeH2OWord2vec

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - min_word_freq
        - Min Word Freq
        - Specify an integer for the minimum word frequency. Word2vec will discard words that appear less than this number of times.
      * - vec_size
        - Vec Size
        - Specify the size of word vectors.
      * - window_size
        - Window Size
        - This specifies the size of the context window around a given word.
      * - epochs
        - Epochs
        - Specify the number of training iterations to run.
      * - init_learning_rate
        - Init Learning Rate
        - Set the starting learning rate.
      * - sent_sample_rate
        - Sent Sample Rate
        - Set the threshold for the occurrence of words. Those words that appear with higher frequency in the training data will be randomly down-sampled. An ideal range for this option 0, 1e-5.
      * - aggregateMethod
        - AggregateMethod
        - Specifies how to aggregate sequences of words.


Details
-------


The Word2vec algorithm takes a text corpus as an input and produces the word vectors as output. The algorithm first creates a vocabulary from the training text data and then learns vector representations of the words.

More details are available at : http://docs.h2o.ai/h2o/latest-stable/h2o-docs/data-science/word2vec.html#


