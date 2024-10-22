
Installation
==================


Installation Steps of Fire with H2 Database
--------------------------

To get started quickly with minimal install and configuration of Sparkflows, please use the steps given below. If you want a production ready environment, please follow the steps in the next section.

* Download the fire ``TGZ`` file from: https://www.sparkflows.io/download

* Or, download the file using the ``wget`` command in Linux :
     
   .. code-block:: bash

        wget https://sparkflows-release.s3.amazonaws.com/fire/rel-3.1.0/3/fire-3.x.y_spark_3.2.1.tgz


 .. Note:: 
	For **CentOS**, install `wget` command using :
	
	   .. code-block:: bash
	
		sudo yum -y install wget
	
	For **Ubuntu**, install `wget` command using :
	     
	   .. code-block:: bash
	
		sudo apt-get install wget 
  
* Unpack it::

    tar xvf fire-3.x.y_spark_3.2.1.tgz

* Sparkflows can be configured to store its metadata into H2 Database, MySQL, Microsoft SQL Server or Aurora MySQL database. For production grade install, one can use any of the above except for H2 Database. More details can be found here: https://docs.sparkflows.io/en/latest/installation/configuration/database/index.html

* For quick installation, create H2 Database::

      cd <fire install_dir>

  ::

      ./create-h2-db.sh

   .. Note:: For detailed information on connecting to RDS, `click here. <https://docs.sparkflows.io/en/latest/installation/configuration/database/mysql-db.html#>`_
    
* Launch Fire Server::

    cd <fire install_dir>

  ::

    ./run-fire-server.sh start

* Open your web browser and navigate to:: 
  
    http://localhost:8080 OR http://<machine_name>:8080 (Access over http)
    
    https://localhost:8443 OR https://<machine_name>:8443 (Access over https)

* Login with:: 

    admin/admin or test/test

 .. Note:: By default Sparkflows will run on 8080(http) and 8443(https). To adjust and personalize the port settings :

      You can modify the configurations in the **application.properties** file located within **fire-3.x.y_spark_3.2.1/conf**.


Installing and starting the Python engine
-------------------------------------------

Sparkflows comes with Java engine and Python engine. Following the above steps, we have installed Sparkflows and started it only with Java engine. If you want to leverage the capabilities of python Machine Learning libraries as well, please install the Python engine by following the below:

* On Ubuntu, the python dependencies can be installed by following the steps here: : https://docs.sparkflows.io/en/latest/installation/installation/python-install-ubuntu.html

* On RedHat and CentOS, the python dependencies can be installed by following the steps here: https://docs.sparkflows.io/en/latest/installation/installation/python-install-redhat-centos.html

  
Helpful Commands
---------------------

* Stopping the Fire Server::
   
  ./run-fire-server.sh stop


* Creating a new Linux user::

   sudo useradd -p password sparkflows


* Changing the password of a user::

   sudo passwd sparkflows


* Forwarding traffic to a port::
  
   sudo firewall-cmd --add-forward-port=port=443:proto=tcp:toport=8443 --permanent

  ::

   sudo firewall-cmd --reload


Upgrading Steps
---------------------

To upgrade Sparkflows, one needs to follow the steps given below:

* Download the new Fire TGZ file from::

    https://www.sparkflows.io/download  
  
  
* Stop Fire Server using the below command from Fire home directory using the command::

      run-fire-server.sh stop
  
* Unpack the TGZ file using the command::

      tar xvf fire-x.y.z.tgz

* Upgrade the H2 database or MySQL database:

   * If you have updated the ``conf/db.properties`` file, copy it from your old location to the new directory.
   * Backup your existing H2 database files. By default they are in your home directory as ``firedb.mv.db``.
   * If you are using MySQL, backup the fire database in MySQL.
   * Execute the following commands to create and upgrade the Fire database schema::

        cd <install_dir>/fire-x.y.z
    
        Run this create and upgrade database script if using H2 database: ./create-h2-db.sh           OR      
        Run this create and upgrade database script if using MySQL database: ./create-mysql-db.sh
    

* If PySpark engine is installed, upgrade python dependencies.

  * Activate the python environment by running from Fire home directory::

       source env/bin/activate 
    
  * Upgrade the dependencies in the environment via::
    
       pip install -r fire-x.y.x/dist/fire/requirements.txt

* Restart Fire Server.

   Restart the Fire server using the below command from Fire home directory using the command::

      run-fire-server.sh start

