Introduction
======

Sparkflows saves all the models trained in its model repository by default. It also captures all the training and validation metrics. The model artifacts are saved on disk or in blob storage by Sparkflows.

These models can be served as one of the two options:

#. **Offline Model Serving**

    * MLOps offline serving is primarily employed for batch scoring, allowing machine learning models to process large volumes of data in a non-real-time, batch fashion.
    * It is utilized for bulk prediction tasks, enabling the efficient processing of extensive datasets with machine learning models in scheduled or periodic operations.
    * Offline model serving typically exhibits high throughput, making it well-suited for scenarios where data processing efficiency and scalability are paramount.

#. **Online model serving**
   
    * MLOps online serving is primarily employed for scoring streaming data, ensuring that machine learning models can make predictions in real-time as new data arrives.
    * It offers low latency, enabling immediate model predictions, which is crucial for applications requiring rapid responses to incoming data.
    * Online model serving facilitates real-time model deployment, allowing predictions to be served as soon as new data becomes available.
    * It is typically used on a relatively smaller number of rows of data at a time, making it suitable for applications where low latency is essential but data volumes are modest.
