Logs
=======

Fire Insights enable you to view the Logs for fireserver and both engine being used.

You Can view the Logs either from VM on which Fire Insights application is installed or from UI with admin access.

Logs from VM
----------

You can view the logs from vm on which Fire Insights is running from below location:

Fireserver Logs:

::

    cd fire-x.y.z/logs/
    Search for fireserver.logs, where you can view fireserver logs.
    
.. figure:: ../../_assets/configuration/logs/fireserver-log.PNG
   :alt: Logs
   :width: 70%
   
   
Fire Logs:

::

    cd cd fire-x.y.z
    Search for fire.logs
    
.. figure:: ../../_assets/configuration/logs/fire-log.PNG
   :alt: Logs
   :width: 70%
   
Pyspark Logs:

::

    cd cd fire-x.y.z
    Search for pyspark.logs

.. figure:: ../../_assets/configuration/logs/pyspark-log.PNG
   :alt: Logs
   :width: 70%
   
   
Logs from UI
----------

You can view the logs from UI if you have admin access

Below are steps involved in it:

Go to Administrations page and select View Server Logs, it will open new windows which has all the Logs ie. Fire Server Logs, Fire Logs, Fire Exception Logs & Fire Pyspark Logs respectively

.. figure:: ../../_assets/configuration/logs/fireserver_log.PNG
   :alt: Logs
   :width: 70%

.. figure:: ../../_assets/configuration/logs/fire_log.PNG
   :alt: Logs
   :width: 70%

.. figure:: ../../_assets/configuration/logs/pyspark_log.png
   :alt: Logs
   :width: 70%
