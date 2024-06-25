Fire Insights Architecture
-----------------

Fire Insights consists of three core components:

  * **Web Browser** for defining end-to-end workflows for building data products and applications:

    * Users interact with the web-based drag and drop user interface for creating datasets and workflows.
    * Workflows leverage the exhaustive set of functional and operational nodes such as Data Profiling, Data Cleaning, ETL, NLP, OCR, Machine Learning etc. displayed in the user interface.

  * **Web Server** running on a standalone machine, VM or Kubernetes cluster:

    * For running the workflows, they are submitted to the web server. The web server submits the workflow to the Apache Spark cluster. The results of the workflow execution are streamed back and displayed in the browser.
    * Web server provides a host of other features like interactive execution, schema inference and propagation, user permissions and roles, LDP integration etc.


  * **Apache Spark** cluster on which the workflows are executed as Spark jobs:

    * Workflows are submitted by the Fire Insights cluster to execute on the Apache Spark cluster.
