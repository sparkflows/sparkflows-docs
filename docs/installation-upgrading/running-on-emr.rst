Running on AWS EMR
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

* Start your EMR cluster on AWS::

    Start your EMR cluster on AWS if you do not already have it running.

* Update the inbound rules for the master node::

    We would have Fire listening on port 8085
    Update the inbound rules to allow port 8085

* ssh into the Master EMR node as the ``hadoop`` user::

    ssh -i my.pem hadoop@ec2-xx-yyy-zz-aaa.compute-1.amazonaws.com

* Download the fire tgz file from:

  * https://www.sparkflows.io/download    
       OR   
  * https://www.sparkflows.io/archives
  
  
* Unpack it::

    tar xvf fire-2.1.0.tgz
    
* Upload the Fire examples data onto HDFS::

    cd <fire install_dir>
    hadoop fs -put data
    
    
* Change the port on which to start Fire::

    cd <fire install_dir>
    Edit conf/application.properties
    Update the last two lines to below:
        http.port=8085
        https.port=8086

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
  
    <machine_name>:8085/index.html

* Login with:: 

    admin/admin or test/test

