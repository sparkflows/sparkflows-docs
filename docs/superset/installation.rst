Installation
==============

Ensure that Superset machine has python 3.6.0+ installed on it.

Steps involved in installing apache superset (centos7)
-------------

* Install Superset::

    pip install apache-superset
    
 
 .. figure:: ..//_assets/configuration/superset_apache.PNG
   :alt: superset
   :width: 60%
 
* Initialize the database::

    superset db upgrade
   

 .. figure:: ..//_assets/configuration/db_upgarde.PNG
   :alt: superset
   :width: 60%

* Create an admin user (you will be prompted to set a username, first and last name before setting a password)::

    export FLASK_APP=superset
    superset fab create-admin
 
 .. figure:: ..//_assets/configuration/admin_user.PNG
   :alt: superset
   :width: 60%
 
* Load some data to play with::
 
    superset load_examples

 
* Create default roles and permissions::

    superset init
 
* Start a development web server on port 8088, using Gunicorn in background::
 
    nohup gunicorn -b 0.0.0.0:8088 --limit-request-line 0 --limit-request-field_size 0 "superset.app:create_app()"
 
 Once above command runs successfully, ensure that port 8088, on which Superset is running is accessible from your browser
 
* Open browser and login with public ip and port::
 
    http://public-ip:8088/login
 
 .. figure:: ..//_assets/configuration/loginpage.PNG
   :alt: superset
   :width: 60%
   
* Use your created credentials to login::
 
 .. figure:: ..//_assets/configuration/homepage.PNG
   :alt: superset
   :width: 60%
