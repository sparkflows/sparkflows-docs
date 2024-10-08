Airflow Installation
=======================

Airflow can be installed using pip.


Step 1 : Pre-requisite Check
------------------------------

Below are the pre-requisites for installing Airflow using pip.

* Python 3 environment.
* Only pip installation is currently officially supported.

The installation of Airflow is straightforward if you follow the instructions below. Airflow uses constraint files to enable reproducible installation, so using pip and constraint files is recommended.


Step 2 : Set Airflow Home (optional)
-----------------------------------

Airflow requires a home directory, and uses ~/airflow by default, but you can set a different location if you prefer. The AIRFLOW_HOME environment variable is used to inform Airflow of the desired location. This step of setting the environment variable should be done before installing Airflow so that the installation process knows where to store the necessary files.

   ::

        export AIRFLOW_HOME=~/airflow

Step 3 : Install Airflow
------------------------
Install Airflow using the constraints file, which is determined based on the URL we pass:

   ::

        AIRFLOW_VERSION=2.10.0

        # Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
        # See above for supported versions.
        PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

        CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
        # For example this would install 2.10.0 with python 3.8: 
        https://raw.githubusercontent.com/apache/airflow/constraints-2.10.0/constraints-3.8.txt

        pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

Step 4 : Run the Airflow Standalone
-----------------------------------
The airflow standalone command initializes the database, creates a user, and starts all the components.

   ::

       airflow standalone

Step 5 : Access the Airflow UI
-------------------------------
Visit localhost:8080 in your browser and log in with the **admin account** details shown in the terminal. Enable the **example_bash_operator DAG** in the home page.

   .. figure:: ../../../_assets/configuration/airflow/Airflow_v1.png
      :alt: airflow
      :width: 60%

`Click here <https://airflow.apache.org/docs/apache-airflow/stable/start.html>`_ to get the details of Airflow Installations steps.


.. note:: * Successful installation requires a Python 3 environment. Starting with Airflow 2.7.0, Airflow supports Python 3.8, 3.9, 3.10, 3.11 and 3.12.

          * Only pip installation is currently officially supported.

