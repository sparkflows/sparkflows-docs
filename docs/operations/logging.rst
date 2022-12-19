Logs in Fire Insights
=====================

In Fire Insights there are 2 processes which run:

* fire server
* fire engine
* fire pyspark engine (If Pyspark is Configured)

Logs for Fire Web Server
------------------------

The logs for Fire Web Server go into fireserver.log. The logging level is determined by the properties file conf/logback-spring.xml.

As an Administrator, the Logs can be viewed from UI, once you login with Fire Insights application, you need to go inside ''ADMINISTRATION >> View Server Logs'' 


.. figure:: ../../_assets/operating/operations/fire-server-logs.PNG
         :alt: operations
         :width: 50%

Example log4j.properties
++++++++++++++++++++++++


How to change the various logging levels
++++++++++++++++++++++++++++++++++++++++



Logs for Fire Engine
--------------------

The logs for Fire Engine go into fire.log. 


As an Administrator, the Logs can be viewed from UI, once you login with Fire Insights application, you need to go inside ''ADMINISTRATION >> View Server Logs'' 


.. figure:: ../../_assets/operating/operations/fire-logs.PNG
         :alt: operations
         :width: 50%

Logs for Fire Pyspark Engine
--------------------

The logs for Fire Pyspark Engine go into pyspark.log.

As an Administrator, the Logs can be viewed from UI, once you login with Fire Insights application, you need to go inside ''ADMINISTRATION >> View Server Logs'' 


.. figure:: ../../_assets/operating/operations/fire-pyspark-logs.PNG
         :alt: operations
         :width: 50%
