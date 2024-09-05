Anomaly Detection
===============

Fire Insights provides the below processors for performing Anomaly Detection using Keras.
Below is an example of implementing Autoencoders for detecting anomalies in a dataset using Keras, providing a powerful approach to identify outliers and abnormal patterns in complex data.

.. figure:: ../../../docs/_assets/machinelearning/anomaly-dtection-keras.png
   :alt: Deep Learning
   :width: 90%

Tennessee Eastman Process Dataset
----------------------------------

The Tennessee Eastman Process (TEP) is a widely used chemical process simulation benchmark for testing fault detection and diagnosis algorithms. The dataset simulates various operational scenarios, including normal conditions and 21 different process faults. These faults include sensor failures, equipment malfunctions, and process disturbances.

TEP has been popular in academia and industry because it represents a real-world challenge with multivariate data and the need for accurate and robust fault detection mechanisms. It provides both training data with normal operation and test data containing different types of faults.

Autoencoders for Fault Detection
--------------------------------

Autoencoders are unsupervised neural networks used for representation learning. They are often employed in fault detection tasks. The idea is to train an autoencoder on fault-free (normal) data, allowing the network to learn how to encode and reconstruct the normal operational patterns. During inference, if the input is faulty data, the autoencoder will reconstruct the input poorly, as it has only learned normal operations, thus making it easier to detect faults.

Autoencoders are particularly useful in situations where labeled faulty data is limited or unavailable, as they can model what "normal" looks like without explicit labels.

Workflow Overview
-----------------

This workflow is designed to detect faults in the Tennessee Eastman process using a sequential deep learning model. Below is a detailed step-by-step explanation of the workflow nodes used:

Nodes Overview
--------------

1. **KerasPreprocessor (Preprocess Data)**:
    - This node preprocesses the dataset before feeding it into the model. Common preprocessing tasks include scaling, normalization, and handling missing values.
   
2. **ReadCSV (Fault-Free Training Data)**:
    - This node loads the fault-free training data from the Tennessee Eastman dataset. The model learns to recognize normal operating conditions using this data.
    - **Parameters**:
        - File Path: Path to the CSV file containing fault-free data.

3. **KerasModel Sequential**:
    - Defines a sequential neural network model, where layers are stacked one by one. This is suitable for simpler models where the output of one layer is passed as input to the next.
    - **Parameters**:
        - Input Layer: Specifies the input shape that matches the dataset.
        - Hidden Layers: Adds layers with specific activation functions (`ReLU`, `Sigmoid`, etc.).
        - Output Layer: Configured based on the classification task (e.g., `Softmax` for multi-class classification).

4. **KerasModel Compile**:
    - This node compiles the Keras model, setting up the optimizer, loss function, and evaluation metrics. Compiling is essential before training the model.
    - **Parameters**:
        - **Optimizer**: Select the optimization algorithm (e.g., `Adam`, `SGD`).
        - **Loss Function**: For classification tasks, `categorical_crossentropy` is commonly used. For regression, `mean_squared_error` is appropriate.
        - **Metrics**: Typical metrics include `accuracy` for classification problems.

5. **KerasModel Fit**:
    - This node is responsible for training the model using the fault-free data. The model will learn to predict normal operational behavior based on the provided dataset.
    - **Parameters**:
        - **Epochs**: Number of training iterations (e.g., 10).
        - **Batch Size**: Number of samples processed before the model is updated.
        - **Validation Split**: Percentage of data reserved for validation to monitor training progress.

6. **ReadCSV (Faulty Test Data)**:
    - This node reads the faulty test data from the Tennessee Eastman dataset. The test data contains various faults, and the trained model will attempt to detect them.
    - **Parameters**:
        - File Path: Path to the CSV containing test data with faults.
        - Delimiter: Specifies how the data is separated (commas, tabs, etc.).
        - Header: Indicates if the file contains column headers.
        - Infer Schema: Automatically detects data types.

7. **SQL (Data Query)**:
    - This node allows for filtering or querying the test dataset, potentially selecting specific fault scenarios or certain columns.
    - **Parameters**:
        - SQL Query: A SQL-like query to filter and prepare data (e.g., select specific rows/columns).

8. **KerasPredict**:
    - This node uses the trained Keras model to predict faults in the test dataset. Based on the input data, it generates the predicted fault labels.
    - **Parameters**:
        - Batch Size: Number of samples to process at a time.
        - Verbose: Whether to print progress information.

9. **PrintNRows**:
    - This node prints the first few rows of the output for validation. It allows you to inspect the results of the prediction step and ensures that the model is performing as expected.
    - **Parameters**:
        - N: Number of rows to print (e.g., 5).
        - Columns: Select which columns to display for a detailed view of predictions.
