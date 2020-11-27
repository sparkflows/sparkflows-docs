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

 .. figure:: ..//_assets/configuration/db_upgrades.PNG
   :alt: superset
   :align: center
   :width: 60%

Create an admin user (you will be prompted to set a username, first and last name before setting a password)

 * ``export FLASK_APP=superset``
 * ``superset fab create-admin``
 
 Load some data to play with
 
 * ``superset load_examples``

Create default roles and permissions

  * ``superset init``
  
Connecting Superset with Databricks
-----------------------------------


