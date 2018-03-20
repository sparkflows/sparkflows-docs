Running on EMR
=======================

Fire can be easily installed on an AWS EMR Cluster.

Below are the steps for installing Fire on EMR.

- *ssh into the Master node*
- *Download Fire*
- *Unzip it*
- *Create H2 Database*
- *Start Fire*

ssh into the Master Node
--------------------------



Download Fire
--------------------------

wget 

Copy it into fire-user-lib
--------------------------

Under the Fire installation directory, there is ``fire-user-lib`` directory.

Copy the downloaded JDBC jar file into it.

Start Fire
------------

Restart Fire with ``./run-fire.sh restart``

Fire Server does not need to be restarted.


