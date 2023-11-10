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
