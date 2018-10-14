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

* Update the inbound rules for the Master Node::

    We would have Fire listening on ports 8085 and 8086
    Update the inbound rules for the Master Node to allow ports 8085 and 8086

* ssh into the Master EMR node as the ``hadoop`` user::

    ssh -i my.pem hadoop@ec2-xx-yyy-zz-aaa.compute-1.amazonaws.com

* Download the fire tgz file by one of the following options:

  * https://www.sparkflows.io/download    
       OR   
  * https://www.sparkflows.io/archives
       OR
  * wget https://s3.amazonaws.com/sparkflows-release/fire/rel-x.y.z/2/fire-x.y.z.tgz
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz
    
    
* Configure the port to start Fire on::

    cd <fire install_dir>
    Edit conf/application.properties
    Update the last two lines to below:
        http.port=8085
        https.port=8086

* Create H2 DB::

    Fire stores its metadata into the embedded H2 database. You can also connect it to an external MySQL database.

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

* Login with the following default username and password:: 

    admin/admin
    
* Connect Fire with the EMR Cluster::

    Go to Administration/Configuration
    Click on 'Infer Hadoop Configs'
    Save
    
    If your EMR cluster is not running HIVE, update 'spark.sql-context = SQLContext'
    
* Create the ``hadoop`` user in Fire::

    Under Administration/Users, add the 'hadoop' user
    Logout from the current session and login again with the 'hadoop' user
    
Running Example Workflows
-------------------------

* Upload the Fire examples data onto HDFS::

    cd <fire install_dir>
    hadoop fs -put data
    
    
* Start off with executing the example workflows::

    - Fire comes pre-packaged with a number of example workflows
    - You can install them by clicking on the 'Install example workflows' link in the landing page when logged in as the `admin` user.
    
    - Execute the workflows
    

