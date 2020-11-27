Installing Superset and Connecting with Databricks
==================================================

Superset enables powerful Visualizations.


Installing Superset
-------------------

Just ensure that superset machine should have python with version 3.6.0+

Steps involved in installing apache superset (centos7)
-------------

Install superset

 * ``pip install apache-superset``
 
 .. figure:: ..//_assets/configuration/superset_apache.PNG
   :alt: superset
   :align: center
   :width: 60%
 
 Initialize the database
 
 * ``superset db upgrade``

 .. figure:: ..//_assets/configuration/db_upgarde.PNG
   :alt: superset
   :align: center
   :width: 60%

Create an admin user (you will be prompted to set a username, first and last name before setting a password)

 * ``export FLASK_APP=superset``
 * ``superset fab create-admin``
 
 .. figure:: ..//_assets/configuration/admin_user.PNG
   :alt: superset
   :align: center
   :width: 60%
 
 Load some data to play with
 
 * ``superset load_examples``
 
 Create default roles and permissions

  * ``superset init``
 
 To start a development web server on port 8088, using Gunicorn use below command
 
 * ``gunicorn -b 0.0.0.0:8088 --limit-request-line 0 --limit-request-field_size 0 "superset.app:create_app()"``
 
 once above command run successfully, just ensure that port 8088, which used by superset is accessible from browser
 
 open browser and login with public ip and port
 
 * ``http://public-ip:8088/login``
 
 .. figure:: ..//_assets/configuration/loginpage.PNG
   :alt: superset
   :align: center
   :width: 60%
   
 Use your created credentials to login
 
 .. figure:: ..//_assets/configuration/homepage.PNG
   :alt: superset
   :align: center
   :width: 60%
 
Connecting Superset with Databricks
-----------------------------------

Now once Superset is running in UI, you can databricks database to it.

Steps involved in Connecting databricks to superset
----------------

Install Needed python dependency for databricks on superset VM

* ``pip install databricks-dbapi``
* ``pip install databricks-dbapi[sqlalchemy]``

Once the above two python databricks dependency installed successfully, you can  restart superset server again & LOgin to superset UI & Click on database

.. figure:: ..//_assets/configuration/superset_database.PNG
   :alt: superset
   :align: center
   :width: 60%

Now you can add databricks database by Clicking on NEW Tab & add databricks `Database name & SQLAlchemy URI`

* ``databricks+pyhive://token:<token>@<companyname>.cloud.databricks.com:443/<database>?cluster=<cluster_id>]``

Just Click on TEST CONNECTION, it should not throw any error and SAVE it

Now You can start using databricks database table for charts and visualizations







