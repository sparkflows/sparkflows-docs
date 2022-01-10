Running ML Workflows
=================


Getting Exception : 'Caused by: java.lang.ArrayIndexOutOfBoundsException: 5' during Prediction
--------------------------------------------------------------------------

When loading a Spark ML model and doing the prediction, running into an error like below:

* Suppressed: java.lang.NullPointerException
* Caused by: java.lang.ArrayIndexOutOfBoundsException: 5

This error is caused when the number of features used in the VectorAssembler during scoring/prediction is fewer than the number of features used when building the model.

