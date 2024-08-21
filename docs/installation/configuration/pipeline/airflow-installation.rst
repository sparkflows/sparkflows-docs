Airflow Installations
---------------

Below are the steps for installing Airflow. 

The installation of Airflow is straightforward if you follow the instructions below. Airflow uses constraint files to enable reproducible installation, so using pip and constraint files is recommended.

#. Set Airflow Home (optional):

    Airflow requires a home directory, and uses ~/airflow by default, but you can set a different location if you prefer. The AIRFLOW_HOME environment variable is used to inform Airflow of the desired location. This step of setting the environment variable should be done before installing Airflow so that the installation process knows where to store the necessary files.

    export AIRFLOW_HOME=~/airflow

#. Install Airflow using the constraints file, which is determined based on the URL we pass:

    AIRFLOW_VERSION=2.10.0

    # Extract the version of Python you have installed. If you're currently using a Python version that is not supported by Airflow, you may want to set this manually.
    # See above for supported versions.
    PYTHON_VERSION="$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"

    CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
    # For example this would install 2.10.0 with python 3.8: https://raw.githubusercontent.com/apache/airflow/constraints-2.10.0/constraints-3.8.txt

    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

#. Run Airflow Standalone:

    The airflow standalone command initializes the database, creates a user, and starts all components.

     airflow standalone

#. Access the Airflow UI:

   Visit localhost:8080 in your browser and log in with the admin account details shown in the terminal. Enable the example_bash_operator DAG in the home page.


   `Click here <https://airflow.apache.org/docs/apache-airflow/stable/start.html>`_ to get details Airflow Installations steps.

