Regression
==========

Apache Spark provides a number of Algorithms for Regression.

https://spark.apache.org/docs/latest/ml-classification-regression.html#classification

- Linear regression
- Generalized linear regression
- Decision tree regression
- Random forest regression
- Gradient-boosted tree regression
- Survival regression
- Isotonic regression

Fire Insights provides processors for the above Algorithms.

Linear Regression
------------------

The interface for working with linear regression models and model summaries is similar to the logistic regression case.

When fitting LinearRegressionModel without intercept on dataset with constant nonzero column by “l-bfgs” solver, Spark MLlib outputs zero coefficients for constant nonzero columns. This behavior is the same as R glmnet but different from LIBSVM.

Generalized linear regression
-----------------------------
