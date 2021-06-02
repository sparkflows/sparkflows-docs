Classification
==============


.. list-table:: Scikit Learn based Classification Processors in Fire Insights
   :widths: 30 70
   :header-rows: 1

   * - Title
     - Description
   * - Logistic Regression Classifier
     - In LR Classifier, probabilities describing the possible outcomes of a single trial are modeled using a logistic function. It is implemented in the linear_model library.

   * - Gradient Boosting classifier
     - The Gradient Boosting Classifier is an additive ensemble of a base model whose error is corrected in successive iterations (or stages) by the addition of Regression Trees which correct the residuals (the error of the previous stage).

   * - Random forest classifier
     - A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement if bootstrap=True (default).


Logistic Regression Classifier
-----------------------------

In LR Classifier, probabilities describing the possible outcomes of a single trial are modeled using a logistic function. It is implemented in the linear_model library.

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegressionCV.html

Gradient Boosting classifier
----------------------------

The Gradient Boosting Classifier is an additive ensemble of a base model whose error is corrected in successive iterations (or stages) by the addition of Regression Trees which correct the residuals (the error of the previous stage).

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html

Random forest classifier
-------------------------

A random forest is a meta estimator that fits a number of decision tree classifiers on various sub-samples of the dataset and use averaging to improve the predictive accuracy and control over-fitting.

More details are at the Scikit-learn page:

https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html
