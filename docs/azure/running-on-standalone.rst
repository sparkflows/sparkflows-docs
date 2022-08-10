Deployment Guide
=======================

Fire Insights can be easily installed on an Azure Standalone VM. 

Prerequisite
-------------

* java 8 should be installed 
* if you do not already have it, Need to install
- Download it from below link::

   https://www.oracle.com/in/java/technologies/javase/javase-jdk8-downloads.html
  
- Install using below command (Centos):: 
   
   yum localinstall jdk-8uxxx-linux-x64.rpm
 
- Set the below in .bash_profile::

   export JAVA_HOME=/usr/java/jdk1.8.0_xxx-amd64/

Below are the overall steps for installing Fire Insights on VM.

- *ssh into the Azure VM*
- *Download Fire Insights* from https://www.sparkflows.io/download
- *Unzip it*
- *Create H2 Database*
- *Start Fire*

Steps
------

* Create a VM on Azure::

    Create a vm if you do not already have it running.

* Update the inbound rule ::

    - ssh port ie 22 should be accessible to ssh to Azure VM.
    - We would have Fire listening on ports 8080, so just ensure its opened.
    

* ssh into the VM::

    ssh -i my.pem userp@public ip.
    
* Confirm that java 8 is already installed, if not follow above steps to install it::

    java -version

* Download the fire tgz file by one of the following options:

  * https://www.sparkflows.io/download    
       OR   
  * https://www.sparkflows.io/archives
       OR
  * wget https://s3.amazonaws.com/sparkflows-release/fire/rel-x.y.z/2/fire-x.y.z.tgz
  
  
* Unpack it::

    tar xvf fire-x.y.z.tgz


* Create H2 DB::

    Fire stores its metadata into the embedded H2 database. You can also connect it to an external MySQL database.

      cd <fire install_dir>
      ./create-h2-db.sh
    
* Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    <machine_ip>:8080

* Login with the following default username and password. Fire Insights by default comes with 2 users:: 

    username : admin password : admin
    username : test password : test
   
   
Loading Example Workflows
-------------------------

* From the home page of Fire Insights, click on ***Load Example Applications***

* Upload the Fire examples data with default or if data is available at anyother location, point to that location::

       
Install and Start Running Example Workflows
------------------------

* Start off with executing the example workflows::

    - Fire comes pre-packaged with a number of example workflows, you can start executing.
    
    

