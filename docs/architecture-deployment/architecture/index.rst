Fire Architecture
-----------------

.. figure:: ../../_assets/architecture/sparkflows-fire-architecture.png
   :scale: 100%
   :alt: Sparkflows Fire Architecture
   :align: center

Fire consists of three core components:

  * **Web Browser** for defining end-to-end workflows for building data products and applications

    * Users interact with the web based drag and drop user interface for creating Datasets and Workflows
    * Workflows leverage the exhaustive set of functional and operational nodes such as Data Profiling, Data Cleaning, ETL, NLP, OCR, Machine Learning etc. displayed in the user interface.

  * **Web Server** running on an Edge node in a Apache Spark Cluster

    * For running the workflows, they are submitted to the web server. The web server submits the workflow to the Apache Spark cluster as a spark job using spark-submit. The results of the workflow execution are streamed back and displayed in the Browser.
    * Web Server provides a host of other features likes interactive execution, schema inference and propagation, user permissions and roles, LDP integration etc.


  * **Apache Spark** cluster on which the workflows are executed as Spark jobs

    * Workflows are saved in a JSON string.
    * Workflows can also be submitted on the spark cluster through **spark-submit** via a command line interface
