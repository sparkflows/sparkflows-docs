Running on EMR
=======================

Fire can be easily installed on an AWS EMR Cluster.

Below are the steps for installing Fire on EMR.

- *ssh into the Master node*
- *Download Fire*
- *Unzip it*
- *Create H2 Database*
- *Start Fire*

Steps
------

* ssh into the Master EMR node


* Download the fire tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unpack it::

    tar xvf fire-2.1.0.tgz


* Create H2 DB::

      cd <fire install_dir>
      ./create-h2-db.sh

* Launch Fire::

    cd <fire install_dir>
    ./run-fire.sh start
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    <machine_name>:8080/index.html

* Login with:: 

    admin/admin or test/test

