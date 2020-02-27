Model Evaluation
==========

Model evaluation aims to estimate the generalization accuracy of a model on future (unseen/out-of-sample) data.

- https://heartbeat.fritz.ai/introduction-to-machine-learning-model-evaluation-fa859e1b2d7f


Evaluation Processors in Fire Insights
----------------------------------------


.. list-table:: Apache Spark based Evaluation Processors in Fire Insights
   :widths: 50 50
   :header-rows: 1

   * - Title
     - Description
   * - NodeRegressionEvaluator
     - Evaluator for regression, which expects two input columns: prediction and label.  Regression analysis is used when predicting a continuous output variable from a number of independent variables.

   * -NodeBinaryClassificationEvaluator
     - Evaluator for binary classification, which expects two input columns: rawPrediction and label.  Binary classifiers are used to separate the elements of a given dataset into one of two possible groups (e.g. fraud or not fraud) and is a special case of multiclass classification. 

   * - NodeMulticlassClassificationEvaluator
     - Evaluator for multiclass classification, which expects two input columns: score and label. A multiclass classification describes a classification problem where there are M>2 possible labels for each data point (the case where M=2 is the binary classification problem)
     

Machine learning continues to be an increasingly integral component of our lives, whether we’re applying the techniques to research or business problems. Machine learning models ought to be able to give accurate predictions in order to create real value for a given organization.

While training a model is a key step, how the model generalizes on unseen data is an equally important aspect that should be considered in every machine learning pipeline. We need to know whether it actually works and, consequently, if we can trust its predictions. Could the model be merely memorizing the data it is fed with, and therefore unable to make good predictions on future samples, or samples that it hasn’t seen before?

In this article, we explain the techniques used in evaluating how well a machine learning model generalizes to new, previously unseen data. We’ll also illustrate how common model evaluation metrics are implemented for classification and regression problems using Python.

Model Evaluation Techniques
---------------------------

The above issues can be handled by evaluating the performance of a machine learning model, which is an integral component of any data science project.

Methods for evaluating a model’s performance are divided into 2 categories: namely, holdout and Cross-validation. Both methods use a test set (i.e data not seen by the model) to evaluate model performance. It’s not recommended to use the data we used to build the model to evaluate it. This is because our model will simply remember the whole training set, and will therefore always predict the correct label for any point in the training set. This is known as overfitting.

Holdout
-------
The purpose of holdout evaluation is to test a model on different data than it was trained on. This provides an unbiased estimate of learning performance.

In this method, the dataset is randomly divided into three subsets:

1)Training set is a subset of the dataset used to build predictive models.

2)Validation set is a subset of the dataset used to assess the performance of the model built in the training phase. It provides a test platform for fine-tuning a model’s parameters and selecting the best performing model. Not all modeling algorithms need a validation set.

3)Test set, or unseen data, is a subset of the dataset used to assess the likely future performance of a model. If a model fits to the training set much better than it fits the test set, overfitting is probably the cause.

The holdout approach is useful because of its speed, simplicity, and flexibility. However, this technique is often associated with high variability since differences in the training and test dataset can result in meaningful differences in the estimate of accuracy.

Cross-Validation
-----------------
Cross-validation is a technique that involves partitioning the original observation dataset into a training set, used to train the model, and an independent set used to evaluate the analysis.

The most common cross-validation technique is k-fold cross-validation, where the original dataset is partitioned into k equal size subsamples, called folds. The k is a user-specified number, usually with 5 or 10 as its preferred value. This is repeated k times, such that each time, one of the k subsets is used as the test set/validation set and the other k-1 subsets are put together to form a training set. The error estimation is averaged over all k trials to get the total effectiveness of our model.

For instance, when performing five-fold cross-validation, the data is first partitioned into 5 parts of (approximately) equal size. A sequence of models is trained. The first model is trained using the first fold as the test set, and the remaining folds are used as the training set. This is repeated for each of these 5 splits of the data and the estimation of accuracy is averaged over all 5 trials to get the total effectiveness of our model.
As can be seen, every data point gets to be in a test set exactly once and gets to be in a training set k-1 times. This significantly reduces bias, as we’re using most of the data for fitting, and it also significantly reduces variance, as most of the data is also being used in the test set. Interchanging the training and test sets also adds to the effectiveness of this method.



- https://towardsdatascience.com/metrics-to-evaluate-your-machine-learning-algorithm-f10ba6e38234


Model Evaluation in Fire Insights
---------------------------------
