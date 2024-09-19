Logs for Fire Server
----------

From the VM
+++++++

You can view the logs from vm on which Fire Insights is running from below location:

Fire server Logs:

::

    cd fire-x.y.z/log/
    Search for fireserver.log, where you can view fireserver logs.
    
.. figure:: ../_assets/configuration/logs/fireserver-log.PNG
   :alt: Logs
   :width: 70%

Logs from UI
+++++

You can view the logs from UI if you have admin access.

Below are steps involved in it:

Go to Administrations page and select View Server Logs, it will open new windows which display all the Logs ie. ''Fire Server Logs, Fire Logs, Fire Exception Logs & Fire Pyspark Logs'' respectively.

.. figure:: ../_assets/configuration/logs/fireserver_log.PNG
   :alt: Logs
   :width: 70%




Logs for Fire Web Server
+++++

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

If using Fire in Docker, along with the above change to setting the level to "DEBUG", you would need to pass ``logback-spring.xml`` in ``entrypoint.sh`` instead of ``log4j.properties`` (default)::

    -Dlog4j.configuration=file:conf/logback-spring.xml
