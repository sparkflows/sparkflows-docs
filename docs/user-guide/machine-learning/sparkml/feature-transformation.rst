Feature Transformation
======================

Feature transformation is simply a function that transforms features from one representation to another. Feature transformation techniques are used for several reasons:

   - data types are not suitable to be fed into a machine learning algorithm, e.g. text, categories
   - feature values may cause problems during the learning process, e.g. data represented in different scales
   - we want to reduce the number of features to plot and visualize data, speed up training or improve the accuracy of a specific model



Apache Spark has the following Feature Transformers. Fire Insights provides them as Processors to be easily used in the workflows:


Feature Transformer Processors in Fire Insights
----------------------------------------------

.. list-table:: Apache Spark based Feature Transformer Processors in Fire Insights
   :widths: 20 50
   :header-rows: 1

   * - Title
     - Description
   * - VectorSlicer
     - VectorSlicer is a transformer that takes a feature vector and outputs a new feature vector with a sub-array of the original features. It is useful for extracting features from a vector column. VectorSlicer accepts a vector column with specified indices, then outputs a new vector column whose values are selected via those indices.
   * - RFormula
     - RFormula selects columns specified by an R model formula. RFormula produces a vector column of features and a double or string column of labels. Like when formulas are used in R for linear regression, string input columns will be one-hot encoded, and numeric columns will be cast to doubles. If the label column is of type string, it will be first transformed to double with StringIndexer. If the label column does not exist in the DataFrame, the output label column will be created from the specified response variable in the formula.

   * - ChiSqSelector
     - ChiSqSelector stands for Chi-Squared feature selection. It operates on labeled data with categorical features. ChiSqSelector uses the Chi-Squared test of independence to decide which features to choose. It supports five selection methods: numTopFeatures, percentile, fpr, fdr, fwe

More details regarding the Feature Transformers in Spark can be found at:
https://spark.apache.org/docs/latest/ml-features#feature-transformers

Tokenizer
------------

https://spark.apache.org/docs/latest/ml-features#tokenizer

Tokenization is the process of taking text (such as a sentence) and breaking it into individual terms (usually words). A simple Tokenizer class provides this functionality. The example below shows how to split sentences into sequences of words. 

Regex Tokenizer
-----------------
RegexTokenizer allows more advanced tokenization based on regular expression (regex) matching. By default, the parameter “pattern” (regex, default: "\\s+") is used as delimiters to split the input text. Alternatively, users can set parameter “gaps” to false indicating the regex “pattern” denotes “tokens” rather than splitting gaps, and find all matching occurrences as the tokenization result. 

Stop Words Remover
--------------------

https://spark.apache.org/docs/latest/ml-features#stopwordsremover

Stop words are words which should be excluded from the input, typically because the words appear frequently and don’t carry as much meaning. 

StopWordsRemover takes as input a sequence of strings (e.g. the output of a Tokenizer) and drops all the stop words from the input sequences. The list of stopwords is specified by the stopWords parameter. Default stop words for some languages are accessible by calling StopWordsRemover.loadDefaultStopWords(language), for which available options are “danish”, “dutch”, “english”, “finnish”, “french”, “german”, “hungarian”, “italian”, “norwegian”, “portuguese”, “russian”, “spanish”, “swedish” and “turkish”. A boolean parameter caseSensitive indicates if the matches should be case sensitive (false by default). 

N Gram Transformer
--------------------
An n-gram is a sequence of n tokens (typically words) for some integer n. The NGram class can be used to transform input features into n-grams.

NGram takes as input a sequence of strings (e.g. the output of a Tokenizer). The parameter n is used to determine the number of terms in each n-gram. The output will consist of a sequence of n-grams where each n-gram is represented by a space-delimited string of n consecutive words. If the input sequence contains fewer than n strings, no output is produced.

Binarizer
-----------
Binarization is the process of thresholding numerical features to binary (0/1) features.

Binarizer takes the common parameters inputCol and outputCol, as well as the threshold for binarization. Feature values greater than the threshold are binarized to 1.0; values equal to or less than the threshold are binarized to 0.0. Both Vector and Double types are supported for inputCol.

PCA
----
PCA is a statistical procedure that uses an orthogonal transformation to convert a set of observations of possibly correlated variables into a set of values of linearly uncorrelated variables called principal components. A PCA class trains a model to project vectors to a low-dimensional space using PCA. The example below shows how to project 5-dimensional feature vectors into 3-dimensional principal components. 

Polynomial Expansion
----------------------
Polynomial expansion is the process of expanding your features into a polynomial space, which is formulated by an n-degree combination of original dimensions. A PolynomialExpansion class provides this functionality. The example below shows how to expand your features into a 3-degree polynomial space. 

String Indexer
----------------
StringIndexer encodes a string column of labels to a column of label indices. StringIndexer can encode multiple columns. The indices are in [0, numLabels), and four ordering options are supported: “frequencyDesc”: descending order by label frequency (most frequent label assigned 0), “frequencyAsc”: ascending order by label frequency (least frequent label assigned 0), “alphabetDesc”: descending alphabetical order, and “alphabetAsc”: ascending alphabetical order (default = “frequencyDesc”). Note that in case of equal frequency when under “frequencyDesc”/”frequencyAsc”, the strings are further sorted by alphabet.

The unseen labels will be put at index numLabels if user chooses to keep them. If the input column is numeric, we cast it to string and index the string values. When downstream pipeline components such as Estimator or Transformer make use of this string-indexed label, you must set the input column of the component to this string-indexed column name. In many cases, you can set the input column with setInputCol.

Additionally, there are three strategies regarding how StringIndexer will handle unseen labels when you have fit a StringIndexer on one dataset and then use it to transform another:

throw an exception (which is the default)
skip the row containing the unseen label entirely
put unseen labels in a special additional bucket, at index numLabels

Index String
---------------
Symmetrically to StringIndexer, IndexToString maps a column of label indices back to a column containing the original labels as strings. A common use case is to produce indices from labels with StringIndexer, train a model with those indices and retrieve the original labels from the column of predicted indices with IndexToString. However, you are free to supply your own labels.

One Hot Encoder
-----------------
One-hot encoding maps a categorical feature, represented as a label index, to a binary vector with at most a single one-value indicating the presence of a specific feature value from among the set of all feature values. This encoding allows algorithms which expect continuous features, such as Logistic Regression, to use categorical features. For string type input data, it is common to encode categorical features using StringIndexer first.

OneHotEncoder can transform multiple columns, returning an one-hot-encoded output vector column for each input column. It is common to merge these vectors into a single feature vector using VectorAssembler.

OneHotEncoder supports the handleInvalid parameter to choose how to handle invalid input during transforming data. Available options include ‘keep’ (any invalid inputs are assigned to an extra categorical index) and ‘error’ (throw an error).

Vector Indexer
-----------------
VectorIndexer helps index categorical features in datasets of Vectors. It can both automatically decide which features are categorical and convert original values to category indices. Specifically, it does the following:

Take an input column of type Vector and a parameter maxCategories.
Decide which features should be categorical based on the number of distinct values, where features with at most maxCategories are declared categorical.
Compute 0-based category indices for each categorical feature.
Index categorical features and transform original feature values to indices.
Indexing categorical features allows algorithms such as Decision Trees and Tree Ensembles to treat categorical features appropriately, improving performance.

Normalizer
------------
Normalizer is a Transformer which transforms a dataset of Vector rows, normalizing each Vector to have unit norm. It takes parameter p, which specifies the p-norm used for normalization. (p=2 by default.) This normalization can help standardize your input data and improve the behavior of learning algorithms.

Standard Scalar
------------------
StandardScaler transforms a dataset of Vector rows, normalizing each feature to have unit standard deviation and/or zero mean. It takes parameters:

withStd: True by default. Scales the data to unit standard deviation.
withMean: False by default. Centers the data with mean before scaling. It will build a dense output, so take care when applying to sparse input.
StandardScaler is an Estimator which can be fit on a dataset to produce a StandardScalerModel; this amounts to computing summary statistics. The model can then transform a Vector column in a dataset to have unit standard deviation and/or zero mean features.

Note that if the standard deviation of a feature is zero, it will return default 0.0 value in the Vector for that feature.

Min Max Scalar
----------------
MinMaxScaler transforms a dataset of Vector rows, rescaling each feature to a specific range (often [0, 1]). It takes parameters:

min: 0.0 by default. Lower bound after transformation, shared by all features.
max: 1.0 by default. Upper bound after transformation, shared by all features.
MinMaxScaler computes summary statistics on a data set and produces a MinMaxScalerModel. The model can then transform each feature individually such that it is in the given range.

SQL Transformer
-------------------
SQLTransformer implements the transformations which are defined by SQL statement. Currently, we only support SQL syntax like "SELECT ... FROM __THIS__ ..." where "__THIS__" represents the underlying table of the input dataset. The select clause specifies the fields, constants, and expressions to display in the output, and can be any select clause that Spark SQL supports. Users can also use Spark SQL built-in function and UDFs to operate on these selected columns. For example, SQLTransformer supports statements like:

SELECT a, a + b AS a_b FROM __THIS__
SELECT a, SQRT(b) AS b_sqrt FROM __THIS__ where a > 5
SELECT a, b, SUM(c) AS c_sum FROM __THIS__ GROUP BY a, b

Vector Assembler
------------------
VectorAssembler is a transformer that combines a given list of columns into a single vector column. It is useful for combining raw features and features generated by different feature transformers into a single feature vector, in order to train ML models like logistic regression and decision trees. VectorAssembler accepts the following input column types: all numeric types, boolean type, and vector type. In each row, the values of the input columns will be concatenated into a vector in the specified order.

Quantile Discretizer
-----------------------
QuantileDiscretizer takes a column with continuous features and outputs a column with binned categorical features. The number of bins is set by the numBuckets parameter. It is possible that the number of buckets used will be smaller than this value, for example, if there are too few distinct values of the input to create enough distinct quantiles.

NaN values: NaN values will be removed from the column during QuantileDiscretizer fitting. This will produce a Bucketizer model for making predictions. During the transformation, Bucketizer will raise an error when it finds NaN values in the dataset, but the user can also choose to either keep or remove NaN values within the dataset by setting handleInvalid. If the user chooses to keep NaN values, they will be handled specially and placed into their own bucket, for example, if 4 buckets are used, then non-NaN data will be put into buckets[0-3], but NaNs will be counted in a special bucket[4].
