Introduction
======

MLOps, is a set of practices and tools that aims to streamline and automate the end-to-end machine learning lifecycle. It bridges the gap between data science and IT operations, ensuring the efficient deployment, monitoring, and maintenance of machine learning models in production. MLOps involves version control for models and data, continuous integration and continuous delivery (CI/CD) pipelines, automated testing, and monitoring for model performance and drift. By implementing MLOps, organizations can accelerate their machine learning development, reduce errors, and ensure models remain effective and reliable over time.

Sparkflows MLOps allows you to deploy Machine Learning models. These models can be either built in Sparkflows or models built outside of Sparkflows can also be onboarded and served.

The models in Sparkflows can be served as one of the two options:

#. **Offline Model Serving**

    * MLOps offline serving is primarily employed for batch scoring, allowing machine learning models to process large volumes of data in a non-real-time, batch fashion.
    * It is utilized for bulk prediction tasks, enabling the efficient processing of extensive datasets with machine learning models in scheduled or periodic operations.
    * Offline model serving typically exhibits high throughput, making it well-suited for scenarios where data processing efficiency and scalability are paramount.

#. **Online model serving**
   
    * MLOps online serving is primarily employed for scoring streaming data, ensuring that machine learning models can make predictions in real-time as new data arrives.
    * It offers low latency, enabling immediate model predictions, which is crucial for applications requiring rapid responses to incoming data.
    * Online model serving facilitates real-time model deployment, allowing predictions to be served as soon as new data becomes available.
    * It is typically used on a relatively smaller number of rows of data at a time, making it suitable for applications where low latency is essential but data volumes are modest.

