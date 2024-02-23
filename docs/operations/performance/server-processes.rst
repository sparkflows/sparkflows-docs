Server Processes
=====

Fire Insights has a server process on each VM and also helper processes running on the machine.

Fire Server
++++

By default the fire server maximum and minimum memory allocated is ``-Xmx2548m -Xms1356m``

you can increase maximum to ``-Xmx8192m``

above parameter can be updated in ``run-fire-server.sh`` and restart the Fire server

::

    nohup ${JAVA} -Dloader.path="fire-server-lib/"  -Dloader.debug=true -Dcom.amazonaws.sdk.disableCertChecking=true -Dlogging.config=file:./conf/logback-spring.xml -Xmx2548m -Xms1356m -XX:+CMSClassUnloadingEnabled -jar ./app/fire-ui.jar   --spring.config.name=application,db,sso.saml,keystore,ldap --spring.config.location=file:./conf/  > /dev/null &

Helper Processes 
++++

The Fire Server spawns helper processes. These can be Java/Scala processes or Pythong processes.

By default fire maximum and minimum memory allocated is ``-Xmx2548m -Xms1356m``

you can increase maximum to ``-Xmx4096m``

above parameter can be updated in ``run-fire.sh`` and restrt the Fire server

::

    nohup java -Xmx2548m -Xms1356m -XX:+CMSClassUnloadingEnabled -Dlog4j.configuration=file:conf/log4j-fire.properties -cp app/fire-spark_3.2.1-server-3.1.0-jar-with-dependencies.jar:fire-user-lib/* fire.httpserver.Fire $port > /dev/null &


