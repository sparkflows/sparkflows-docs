Performance
=====

Fire Insights performance can be increase if the machine memory is high and not being used:

Fire UI
++++

By default fire-ui maximum and minimum memory allocated is ``-Xmx2548m -Xms1356m``

you can increase maximum to ``-Xmx8192m``

above parameter can be updated in ``run-fire-server.sh`` and restrt the Fire server

::

    nohup ${JAVA} -Dloader.path="fire-server-lib/"  -Dloader.debug=true -Dcom.amazonaws.sdk.disableCertChecking=true -Dlogging.config=file:./conf/logback-spring.xml -Xmx2548m -Xms1356m -XX:+CMSClassUnloadingEnabled -jar ./app/fire-ui.jar   --spring.config.name=application,db,sso.saml,keystore,ldap --spring.config.location=file:./conf/  > /dev/null &

Fire 
++++

By default fire maximum and minimum memory allocated is ``-Xmx2548m -Xms1356m``

you can increase maximum to ``-Xmx4096m``

above parameter can be updated in ``run-fire.sh`` and restrt the Fire server

::

    nohup java -Xmx2548m -Xms1356m -XX:+CMSClassUnloadingEnabled -Dlog4j.configuration=file:conf/log4j-fire.properties -cp app/fire-spark_3.2.1-server-3.1.0-jar-with-dependencies.jar:fire-user-lib/* fire.httpserver.Fire $port > /dev/null &
