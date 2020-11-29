Installing Superset and Connecting with Databricks
==================================================

Superset enables powerful Visualizations. Superset can connect with Databricks clusters and display data from Tables in Databricks.


Installing Superset
-------------------

Ensure that Superset machine has python 3.6.0+ installed on it.

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
 
 To start a development web server on port 8088, using Gunicorn use the command below
 
 * ``gunicorn -b 0.0.0.0:8088 --limit-request-line 0 --limit-request-field_size 0 "superset.app:create_app()"``
 
 Once above command run successfully, ensure that port 8088, on which Superset is running is accessible from your browser
 
 Open browser and login with public ip and port
 
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

Once Superset is running, you can connect it to Databricks Tables.

NOTE * Make sure that databricks cluster is running

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

.. figure:: ..//_assets/configuration/superset-connection.PNG
   :alt: superset
   :align: center
   :width: 60%

Just Click on TEST CONNECTION, it should not throw any error and SAVE it, 
On successful save the database will be available in superset database list page.

.. figure:: ..//_assets/configuration/super-databricks-database.PNG
   :alt: superset
   :align: center
   :width: 60%

Now You can start using databricks database table for charts and visualizations

.. figure:: ..//_assets/configuration/query.PNG
   :alt: superset
   :align: center
   :width: 60%





