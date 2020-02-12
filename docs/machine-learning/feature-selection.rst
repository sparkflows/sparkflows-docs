Feature Selection
=================

Apache Spark has the following Feature Selectors. Fire Insights provides them as Processors to be easily used:

More details regarding these Feature Selectors can be found at:

https://spark.apache.org/docs/2.2.0/ml-features.html#feature-selectors

- VectorSlicer
- RFormula
- ChiSqSelector

VectorSlicer
------------

VectorSlicer is a transformer that takes a feature vector and outputs a new feature vector with a sub-array of the original features. It is useful for extracting features from a vector column.

RFormula
--------

RFormula selects columns specified by an R model formula. Currently Spark supports a limited subset of the R operators, including ‘~’, ‘.’, ‘:’, ‘+’, and ‘-‘. The basic operators are:

..* ~ separate target and terms
+ concat terms, “+ 0” means removing intercept
- remove a term, “- 1” means removing intercept
: interaction (multiplication for numeric values, or binarized categorical values)
. all columns except target

ChiSqSelector
--------------

ChiSqSelector stands for Chi-Squared feature selection. It operates on labeled data with categorical features. ChiSqSelector uses the Chi-Squared test of independence to decide which features to choose. It supports five selection methods: numTopFeatures, percentile, fpr, fdr, fwe.
