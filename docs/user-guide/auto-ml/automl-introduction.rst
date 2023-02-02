AutoML-Introduction
=====================

AutoML (Automated Machine Learning) is a process of automating the entire machine learning pipeline, from data preparation and feature engineering to model selection and hyperparameter tuning. The goal of AutoML is to make the process of building and deploying machine learning models faster, easier, and more accessible, particularly for people with less experience in machine learning. 

AutoML systems automate the entire machine learning pipeline by using a combination of techniques such as evolutionary algorithms, Bayesian optimization, and gradient-based optimization. They also provide an interface to interact with the system, like providing feedback on results, choosing model and stopping the pipeline.

The main advantage of AutoML is that it allows users to build machine learning models without having to have a deep understanding of the underlying algorithms or the technical details of the process. This can make it faster, easier and more accessible to create high-performing models, especially for people with less experience in machine learning. Additionally, since AutoML uses many different algorithms and parameters, it can be more robust to different types of data and problems, making it a more general-purpose solution

Fire provides the option to create the AutoML experiments by selecting the data and type of package. Each experiment will provide the leaderboard with different models & the hyperparameters used in the experiments. All experiments can be compared to decide the best fit for that particular use case.

.. figure:: ../../_assets/auto-ml/automl-steps.png
      :alt: auto-ml
      :width: 90%
      


In Fire, AutoML function is disabled by default. But, once it is enabled in the Fire configuration, user's can see the option to create the AutoML experiments on project page.

.. figure:: ../../_assets/auto-ml/automl-exp-page.png
      :alt: auto-ml
      :width: 90%
      

Currently Fire supports H2O and PyCaret AutoML packages.
--------------------------------------------

More details on H2O can be found at: https://docs.sparkflows.io/en/latest/user-guide/auto-ml/h2o.html

More details on PyCaret can be found at: https://docs.sparkflows.io/en/latest/user-guide/auto-ml/pycaret.html
   



Model Comparison
------------------

* Select any 2 AutoML experiments to compare across models and then click on the ``COMPARE`` button to execute and view the comparison result.

.. figure:: ../../_assets/auto-ml/ml-compare-1.PNG
      :alt: auto-ml
      :width: 90%
      
      

      
* The camparison results will be displayed as shown below.

.. figure:: ../../_assets/auto-ml/ml-compare-2.PNG
      :alt: auto-ml
      :width: 90%
      
      
.. figure:: ../../_assets/auto-ml/ml-compare-3.PNG
      :alt: auto-ml
      :width: 90%
      
* Click on the model name to view the model details.

.. figure:: ../../_assets/auto-ml/ml-compare-4.PNG
      :alt: auto-ml
      :width: 90%      

