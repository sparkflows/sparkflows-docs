Regression
===========


.. list-table:: Scikit Learn based Regression Processors in Fire Insights
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Ridge regression
     -  Ridge regression addresses some of the problems of Ordinary Least Squares by imposing a penalty on the size of the coefficients. The ridge coefficients minimize a penalized residual sum of squares
     
   * - Lasso regression
     - The Lasso is a linear model that estimates sparse coefficients. It is useful in some contexts due to its tendency to prefer solutions with fewer non-zero coefficients, effectively reducing the number of features upon which the given solution is dependent.

   * - Gradient Boosting regression
     - GB builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage a regression tree is fit on the negative gradient of the given loss function
     
   * - Random forest regression
     - A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement if bootstrap=True (default). 

Ridge regression
----------------

Ridge regression is an extension of linear regression where the loss function is modified to minimize the complexity of the model. This modification is done by adding a penalty parameter that is equivalent to the square of the magnitude of the coefficients.

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html

Lasso Regression
-----------------

Lasso regression or the Least Absolute Shrinkage and Selection Operator, is also a modification of linear regression. In Lasso, the loss function is modified to minimize the complexity of the model by limiting the sum of the absolute values of the model coefficients (also called the l1-norm).

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html

Gradient Boosting regression
--------------------------

Gradient Boosting builds an additive model in a forward stage-wise fashion; it allows for the optimization of arbitrary differentiable loss functions. In each stage a regression tree is fit on the negative gradient of the given loss function.

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/auto_examples/ensemble/plot_gradient_boosting_regression.html

Random forest regression
--------------------------

A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is controlled with the max_samples parameter if bootstrap=True (default), otherwise the whole dataset is used to build each tree.

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html
