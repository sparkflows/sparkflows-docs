Regression
==========

Apache Spark provides a number of Algorithms for Regression.

https://spark.apache.org/docs/latest/ml-classification-regression.html#classification

- Linear regression
- Generalized linear regression
- Decision tree regression
- Random Forest regression
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

Contrasted with linear regression where the output is assumed to follow a Gaussian distribution, generalized linear models (GLMs) are specifications of linear models where the response variable Yi follows some distribution from the exponential family of distributions.

Spark’s GeneralizedLinearRegression interface allows for flexible specification of GLMs which can be used for various types of prediction problems including linear regression, Poisson regression, logistic regression, and others. 

Decision tree regression
-------------------------

Decision trees are a popular family of classification and regression methods.

Decision tree builds regression or classification models in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes. A decision node (e.g., Outlook) has two or more branches (e.g., Sunny, Overcast and Rainy), each representing values for the attribute tested. Leaf node (e.g., Hours Played) represents a decision on the numerical target. The topmost decision node in a tree which corresponds to the best predictor called root node. Decision trees can handle both categorical and numerical data.

Random Forest Regression
-------------------------

Random forests are a popular family of classification and regression methods.

Random forests or random decision forests are an ensemble learning method for classification, regression and other tasks that operate by constructing a multitude of decision trees at training time and outputting the class that is the mode of the classes (classification) or mean prediction (regression) of the individual trees. Random decision forests correct for decision trees' habit of overfitting to their training set.


Gradient - boosted Tree Regression
-----------------------------------
Gradient-boosted trees (GBTs) are a popular regression method using ensembles of decision trees.

Gradient boosting is a machine learning technique for regression and classification problems, which produces a prediction model in the form of an ensemble of weak prediction models, typically decision trees. It builds the model in a stage-wise fashion like other boosting methods do, and it generalizes them by allowing optimization of an arbitrary differentiable loss function.




