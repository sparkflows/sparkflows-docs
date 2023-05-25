Deployment Guide
=======================

Fire Insights can be easily installed on an Azure Standalone VM. 

Prerequisite
-------------

Before initiating the installation process, make sure to meet the following requirement:

Install Java 8
+++++

Please install Java 8 if it has not been pre-installed on your machine.

Step 1 : **Download** Java 8 from the link given below: ::

   https://www.oracle.com/in/java/technologies/javase/javase-jdk8-downloads.html
  
Step 2 : **Install** it using the command (Centos) given below: 
:: 
   
   yum localinstall jdk-8uxxx-linux-x64.rpm
 
Step 3 : **Set** the below in .bash_profile::

   export JAVA_HOME=/usr/java/jdk1.8.0_xxx-amd64/

Below are the overall steps for installing Fire Insights on VM:

#. Create VM on Azure
#. Update inbound rule
#. SSH into the Azure VM
#. Download Fire Insights. `Click here <https://www.sparkflows.io/download>`_ to download.
#. Unzip it
#. Create H2 Database
#. Start Fire

Steps
------

#. Create a VM on Azure::

    Create a VM, if you do not already have it running.

#. Update the inbound rule ::

    - SSH port i.e. 22 should be accessible to SSH to Azure VM.
    - Fire would listen on port 8080, so ensure that it is opened.
    

#. SSH into the VM::

    ssh -i my.pem userp@public ip.
    
#. Ensure that java 8 is already installed, if not, follow the above steps to install it. ::

    java -version

#. Download the fire tgz file by any of the following links:

    * https://www.sparkflows.io/download    
                  OR   
    * https://www.sparkflows.io/archives
                  OR
    * wget **https://s3.amazonaws.com/sparkflows-release/fire/rel-x.y.z/2/fire-x.y.z.tgz**
  
  
#. Unpack it::

    tar xvf fire-x.y.z.tgz


#. Create H2 Database::

    Fire stores its metadata into the embedded H2 database. You can also connect it to an external MySQL database.

      cd <fire install_dir>
      ./create-h2-db.sh
    
#. Launch Fire Server::

    cd <fire install_dir>
    ./run-fire-server.sh start

#. Open your web browser and navigate to:: 
  
    <machine_ip>:8080

#. Login with the following default username and password. Fire Insights by default comes with 2 users:: 

    Username : admin Password : admin
    Username : test Password : test
   
   
Loading Example Workflows
-------------------------

#. From the home page of Fire Insights, click on **Load Example Applications**.

#. Upload the Fire examples data with default or if data is available at any other location, point to that location.

       
Install and Start Running Example Workflows
------------------------

#. Start off with executing the example workflows::

    - Fire comes pre-packaged with a number of example workflows, you can start executing these workflows.
    
    

