Installation
------------

Fire is built to be lightweight, secure and powerful. It can be setup to run:

* In standalone mode on a MacOS, Linux or Windows machine
* On an edge node of an Apache Spark cluster. In this case the jobs would be submitted and run on the Apache Spark Cluster.

Fire stores its metadata in a Relational Store. It can be H2 or MySQL.

Installing Fire

.. toctree::
   :maxdepth: 2

   mac-install
   windows-install

Install on Windows OS

Connecting Fire to a Spark Cluster


Database

Fire runs with H2 database by default but can easily be set up to run with MySQL as well. Below are the steps to install H2 and MySQL Databases. Fire stores the users, workflows, dataset definitions, dashboard definition and history of workflow executions into the database.

H2 Database Install
MySQL Database Install

Configuring Fire
​
More details on configuring Fire is available at : Configuring Fire
