Reading from RDBMS
=======================

Fire has JDBC Processors for reading from JDBC sources or writing to JDBC sinks.

In order to connect to a JDBC source like MySQL/Oracle/DB2 etc. the JDBC driver needs to be installed in Fire.

Use the steps here for installing the corresponding JDBC driver for your RDBMS:

- https://sparkflows.readthedocs.io/en/latest/operating/installing-jdbc-drivers.html


Workflow for reading from MySQL
--------------------------------

Below is a workflow which reads data from MySQL and saves to a CSV file.

.. figure:: ../_assets/user-guide/jdbc-workflow.png
   :scale: 50%
   :alt: JDBC Workflow
   :align: center
   
JDBC Processor Configuration
----------------------------

Below are the configuration details of the JDBC Processor

.. figure:: ../_assets/user-guide/jdbc-dialog.png
   :scale: 50%
   :alt: JDBC Processor Dialog
   :align: center
   
Results of reading from MySQL table
-----------------------------------

The below screenshot displays some of the records read from the MySQL table by Fire.

.. figure:: ../_assets/user-guide/jdbc-read-results.png
   :scale: 50%
   :alt: JDBC Read Results
   :align: center

