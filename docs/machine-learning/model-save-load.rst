Model Save/Load
================

Save/ Load Model allows you to save your model to file and load it later in order to make predictions.

Fire Insights allows you to save the ML Model created.

Spark ML models are saved into a directory with multiple files in it.

H2O Models can be saved in binary format or in MOJO format.

The ML Models can be loaded in the same or other workflows to be used for scoring. The ML Models can also be downloaded from HDFS Browse.


Finalize Your Model with pickle
--------------------------------
Pickle is the standard way of serializing objects in Python.

You can use the pickle operation to serialize your machine learning algorithms and save the serialized format to a file.

Later you can load this file to deserialize your model and use it to make new predictions.

Finalize Your Model with joblib
-------------------------------
Joblib is part of the SciPy ecosystem and provides utilities for pipelining Python jobs.

It provides utilities for saving and loading Python objects that make use of NumPy data structures, efficiently.

This can be useful for some machine learning algorithms that require a lot of parameters or store the entire dataset (like K-Nearest Neighbors).

Tips for Finalizing Your Model
---------------------------------
This section lists some important considerations when finalizing your machine learning models.

- Python Version. Take note of the python version. You almost certainly require the same major (and maybe minor) version of Python used to serialize the model when you later load it and deserialize it.

- Library Versions. The version of all major libraries used in your machine learning project almost certainly need to be the same when deserializing a saved model. This is not limited to the version of NumPy and the version of scikit-learn.

- Manual Serialization. You might like to manually output the parameters of your learned model so that you can use them directly in scikit-learn or another platform in the future. Often the algorithms used by machine learning algorithms to make predictions are a lot simpler than those used to learn the parameters can may be easy to implement in custom code that you have control over.

Take note of the version so that you can re-create the environment if for some reason you cannot reload your model on another machine or another platform at a later time.

Summary
-------
In this post you discovered how to persist your machine learning algorithms in Python with scikit-learn.

You learned two techniques that you can use:

- The pickle API for serializing standard Python objects.

- The joblib API for efficiently serializing Python objects with NumPy arrays.

