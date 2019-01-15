Configuring Pipelines
======================

Fire uses Apache Airflow for executing Pipelines. Hence Airflow has to be installed on the same machine as Fire.

Below are the configurations needed in Fire.

.. figure:: ../_assets/user-guide/pipelines-configuration.PNG
   :alt: Pipelines Configuration
   :align: center
   
Airflow Installation
--------------------

It explain the steps involved in installing airflow on Centos and RHEL.

- Login to machine
 - ssh -i xyz.pem sparkflows@x.y.z.w

- Before installing airflow we need to update installed package:
 - yum -y update
 
- let’s install python-pip and any required packages: 
 - sudo yum install epel-release
 - sudo yum install python-pip
 
- Check the version of Pip that is installed and if reqd upgrade:
 - pip -V
 - pip install --upgrade setuptools
 
- Note that for 1.10 you now need to preface install commands or export this env var:
 - export SLUGIFY_USES_TEXT_UNIDECODE=yes
 
- Install gcc , gcc-c++ and dependencies for python 2.7 
 - sudo yum -y install gcc gcc-c++ kernel-devel
 - sudo yum -y install python-devel libxslt-devel libffi-devel openssl-devel
  
- airflow needs a home, ~/airflow is the default,so we can export it
 - export AIRFLOW_HOME=~/airflow  
 
- Install from pypi using pip
 - pip install apache-airflow 
  
- To check airflow version
 - airflow version


.. figure:: ../_assets/user-guide/airflow-version.PNG
   :alt: airflow
   :align: center
  
- Generate a Fernet key for Airflow(optional)
 - python -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
 - fgrc0MPUG1n3Q352Fp705A-bysNHX6EFRr7nYFTmXXA=
 - update in airflow.cfa
 - fernet key: fgrc0MPUG1n3Q352Fp705A-bysNHX6EFRr7nYFTmXXA=
 
- Initialize the database
 - airflow initdb 
 
- start the web server, its default port is 8080, If anyother application is running on 8080, we can update other port for airflow 
 - airflow webserver -p 8090

.. figure:: ../_assets/user-guide/airflow-webserver-running-url.PNG
   :alt: airflow
   :align: center
 
- start the scheduler
 - airflow scheduler

.. figure:: ../_assets/user-guide/airflow-scheduler.PNG
   :alt: airflow
   :align: center
   
- login in browser
 - http://x.y.z.w:8090   

.. figure:: ../_assets/user-guide/airflow-web-url.PNG
   :alt: airflow
   :align: center
   
