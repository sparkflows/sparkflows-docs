H2O GBM
========

This workflow performs H2O’s GBM sequentially builds regression trees on all the features of the dataset in a fully distributed way - each tree is built in parallel
   
Workflow
-------

The below workflow:

* Read the Bike Sharing Dataset.
* Split the dataset for training and test.
* Perform clustering using H2O GBM.
* Score the test dataset using the model created.
* Print the results.
