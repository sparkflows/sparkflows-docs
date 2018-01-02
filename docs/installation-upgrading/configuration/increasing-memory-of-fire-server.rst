Increasing Memory of Fire Server
================================

By default, when the Sparkflows web server is started with ``run-fire-server.sh``, it is given ``1.5 GB of memory``.

Below is from run-fire-server.sh::

    nohup ${JAVA} -server -Djava.ext.dirs=./user-lib/ -Xmx1548m -Xms1356m -XX:+CMSClassUnloadingEnabled -XX:PermSize=512m -XX:MaxPermSize=512m -jar ./app/fire-ui-1.3.0.war --spring.config.name=application,db,log4j --spring.config.location=file:./conf/ &

* In order to increase the amount of memory for the Sparkflows web server, ``increase the value of -Xmx`` based on the amount of memory available on your server.

* For example, you could raise it to 5 GB or 10 GB or more up to 25 GB.
  * -Xmx5g
  * -Xmx10g
  * -Xmx25g
  
* The increased memory size, if available, allows Sparkflows to handle more requests and return results faster. Of course, when connected to a Spark cluster, the full jobs are submitted to the Spark cluster through spark-submit, allowing it to be very scalable and not dependent on the Sparkflows web server.

* The interactive execution of the workflows in the workflow editor, is run within Sparkflows on a small subset of the data. These interactive executions would benefit from increased memory.
