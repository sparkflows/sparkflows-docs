Shapley
=======
Shapley values are one of the standard techquie used for Machine Learning Interpretability.The Shapley Feature importance is the contribution of teh featue to the payout, weighted and summed over all possible feature value combinations.The Shapley value might be the only method to deliver a full explanation. In situations where the law requires explainability – the Shapley value might be the only legally compliant method, because it is based on a solid theory and distributes the effects fairly.

More on Shapley values can be found here - https://christophm.github.io/interpretable-ml-book/shapley.html#the-shapley-value-in-detail
More on SHAP can be found here - https://christophm.github.io/interpretable-ml-book/shap.html

Sparkflows supports SHAP value computations for Tree based h2o algorithms for regression and binomial classification usecases. The below nodes can be leveraged to get Shapley contributions:
  - H2O Distributed Random forest
  - H2O Gradient Boosted machine
  - H2O XGBoost
  - H2O AutoML

Below are the details of how the SHAP values can be computed:
  - In the above mentioned nodes, one can set the field `WITH CONTRIBUTIONS` to `True` during training the model and then during scoring to ask the model to compute the SHAP Summary plot. Screenshot below
  - When scoring on a dataset trained with the above field set, one can see the average SHAP Summary plot.
 
  
.. figure:: ../../../_assets/user-guide/machine-learning/h2o/shapley_contribution.png
   :alt: Shapley value computation field
   :width: 90%


The SHAP Feature Importance plot looks like below:

.. figure:: ../../../_assets/user-guide/machine-learning/h2o/feature_importance_shap.png
   :alt: Feature importance SHAP plot
   :width: 90%
   
   
The SHAP Summary plot looks like below:

.. figure:: ../../../_assets/user-guide/machine-learning/h2o/shap.png
   :alt: Summary SHAP plot
   :width: 90%
   


