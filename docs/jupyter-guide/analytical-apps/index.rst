Analytical Apps
=================

Analytical Apps can be built on top of Jupyter Notebooks. These apps provide a web interface for business and power users to seamlessly interact with Jupyter Notebooks and view the output results.

In order to output text, tables, charts from Jupyter Notebook to Analytical App a Fire Insights, an SDK is used. It communicates back with the Fire Insights Server to which the user is logged in.

The Jupyter Notebook can be wrapped in a Docker Container and executed by Fire Insights on a Kubernetes Cluster.

.. panels::
    :container: container-lg pb-3
    :column: text-center col-lg-6 col-md-6 col-sm-6 col-xs-12 p-2
    
    :doc:`/jupyter-guide/analytical-apps/pre-requisites`

    Pre-requisites requirements

    ---

    :doc:`/jupyter-guide/analytical-apps/create-notebook`

    Steps for creating Jupyter Notebook 

    ---

    :doc:`/jupyter-guide/analytical-apps/output-to-analytical-app`

    Steps to output results to Analytical App

    ---

    :doc:`/jupyter-guide/analytical-apps/create-docker-image`

    Steps for creating Docker image

    ---


    :doc:`/jupyter-guide/analytical-apps/creating-jupyter-notebook-connection`

    Steps for creating Jupyter Notebook connection

    ---


    :doc:`/jupyter-guide/analytical-apps/creating-analytical-app`

    Steps for creating Analytical App
    

.. toctree::
   :hidden:
 
   pre-requisites.rst
   create-notebook.rst
   output-to-analytical-app.rst
   create-docker-image.rst
   creating-jupyter-notebook-connection.rst
   creating-analytical-app.rst
   
   
