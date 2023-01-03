Logs in Fire Insights
=====================

Below is the list of 3 processes that run in Fire Insights :

* Fire server
* Fire engine
* Fire PySpark engine (If PySpark is configured.)

Logs for Fire Web Server
------------------------

The logs for Fire web server go into "fireserver.log". The logging level is determined by the properties file "conf/logback-spring.xml".

As an administrator, the logs can be viewed from UI. Once you login with Fire Insights application, you need to go inside ``ADMINISTRATION >> View Server Logs``. 


.. figure:: ../_assets/operating/operations/fire-server-logs.PNG
   :alt: connection
   :width: 60%


Changing the Various Logging Levels
++++++++++++++++++++++++++++++++++++++++

You can change the logging levels to ``debug`` mode by updating "conf/logback-spring.xml" file using the below and restart the Fire server:

::

    <!-- LOG "org.springframework.web" at ERROR level -->
    <logger name="org.springframework.web" level="DEBUG"
        additivity="false">
    <appender-ref ref="RollingFile" />
    <appender-ref ref="Console" />
    <appender-ref ref="SevereRollingFile" />
    </logger>

Logs for Fire Engine
--------------------

The logs for Fire engine go into "fire.log". 


As an administrator, the logs can be viewed from UI. Once you login using Fire Insights application, you need to go inside ``ADMINISTRATION >> View Server Logs``. 


.. figure:: ../_assets/operating/operations/fire-logs.PNG
   :alt: connection
   :width: 60%

Logs for Fire PySpark Engine
--------------------

The logs for Fire PySpark engine go into "pyspark.log".

As an Administrator, the logs can be viewed from UI. Once you login with Fire Insights application, you need to go inside ``ADMINISTRATION >> View Server Logs``. 


.. figure:: ../_assets/operating/operations/fire-pyspark-logs.PNG
   :alt: connection
   :width: 60%

.. note:: You can view the logs by login to Fire Insights server as well.


Logs for Job Submitted on the Cluster
--------------------

Fire enables you to view the logs for job submitted on the cluster from UI. As an user, you can view the logs while running any workflow as below. You can go to "executions page" and click on ''three dots'' and logs option will be available.


.. figure:: ../_assets/operating/operations/logs_wf.PNG
   :alt: operations
   :width: 80%
   
.. figure:: ../_assets/operating/operations/databricks-logs.PNG
   :alt: operations
   :width: 60%   
   
.. figure:: ../_assets/operating/operations/databricks_logs.PNG
   :alt: operations
   :width: 60%   
   
.. note:: Above example is shown for the job submitted on databricks cluster.
