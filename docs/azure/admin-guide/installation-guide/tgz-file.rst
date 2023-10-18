Using tgz File
=========
This document explains in detail the steps required to install Sparkflows using tgz file.

Follow the below steps to install Sparkflows using tgz file :

Step 1 : SSH into the Azure VM
------------
   
#. SSH into the AWS Instance using:

   * Public ipv4 IP from the Azure console and 
   * The `PEM` file (key file) downloaded while bringing up the Azure VM and
   * The command as below :
     ::
         ssh -i sparkflows.pem sparkflows@21.xxx.xxx.113

  

   .. Note::
            * Run all the below steps as a user with sudo permission. If unsure, please run the below commands as `root` user.
            * If you are using Ubuntu, you may have to run the following and then select ``No``. ::

              sudo dpkg-reconfigure dash


Step 2 : Download and install JDK 8
--------------

#. On **CentOS**, install and Open JDK 1.8 by running the following :
       
   ::
         
         sudo yum install -y java-1.8.0-openjdk-devel
                     
   
   Or On **Ubuntu**, install and Open JDK 1.8 by running the following :
       
   ::
         
         sudo apt install openjdk-8-jdk
        

#. Check the version of JAVA by running the following :

   :: 
      
         java -version

   On successful installation and checking java version, one would see the below:

   .. figure:: ../../../_assets/aws/aws-deployment/install.png
      :alt: aws-deployment
      :width: 60%

Step 3 : Download the latest Sparkflows TAR
--------------

#. For **CentOS**, install `wget` command using :
     
   ::

        sudo yum -y install wget

   Or for **Ubuntu**, install `wget` command using :
     
   ::

        sudo apt-get install wget (Ubuntu)

#. Download the latest TAR from :
     
   ::

        wget https://sparkflows-release.s3.amazonaws.com/fire/rel-3.1.0/3/fire-3.x.y_spark_3.2.1.tgz

#. Extract the TAR by using :
     
   ::

       tar xvf fire-3.x.y_spark_3.2.1.tgz


#. Create DB tables with Schema :
     
   Sparkflows metadata can be stored in RDS or it has embedded H2DB by default.
     
     * Go to inside the sparkflows binary extracted directory :
       ::
          cd  fire-3.x.y_spark_3.2.1

     * Create the DB and schema by running the following :
       ::
          ./create-h2-db.sh

   .. Note:: For detailed information on connecting to RDS, `click here. <https://docs.sparkflows.io/en/latest/installation/configuration/database/mysql-db.html#>`_

Step 4 : Install Python
-----------
   
#. For **CentOS**, run the below commands to install all the Python dependencies using :
     
   ::
        
        cd ..

   ::

        sudo yum -y update

   ::

        sudo yum install -y gcc openssl-devel bzip2-devel libffi-devel zlib-devel

   ::

        wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

   ::

        tar xzf Python-3.7.0.tgz

   ::

        cd Python-3.7.0

   ::

        sudo ./configure --enable-optimizations

   ::

        sudo yum -y install make

   ::

        sudo make altinstall

   ::

        cd ..

   Or for **Ubuntu**, run the below commands to install all the Python dependencies using :
     
   ::
        
        cd ..

   ::

        sudo apt -y update

   ::

        sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev wget libbz2-dev

   ::

        wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz

   ::

        tar xzf Python-3.7.0.tgz

   ::

        cd Python-3.7.0

   ::

        sudo ./configure --enable-optimizations

   ::

        sudo make altinstall

   ::

        cd ..

#. Check the system wide version of python installed by running : 
     
   ::
        
         python3.7 --version

#. Install Python Libraries :
     
   Create the virtual environment, activate it and install the python libraries inside it by running :
     
   ::
        
        python3.7 -m venv venv

   ::

        source venv/bin/activate

   ::

        pip install pip --upgrade

   ::

        pip install pystan

   ::

        pip install convertdate

#. Install all the other python libraries from the `requirements.txt` file :
     
   ::
        
         pip install -r fire-3.x.y_spark_3.2.1/dist/fire/requirements.txt

   .. Note:: This can run into `Memory error` if there is not enough free RAM on the machine. In that case, please split the dependencies in `requirements.txt` into multiple parts and install.

#. Check if all dependencies are installed by running :
     
   ::
        
        pip list

Step 5 : Start Sparkflows Server
-----------
#. Start the Sparkflows server by running the below :
     
   ::
         
            ./run-fire-server.sh start

   .. Note:: By default Sparkflows will run on 8080(http) and 8443(https). To adjust and personalize the port settings :

      You can modify the configurations in the **application.properties** file located within **fire-3.x.y_spark_3.2.1/conf**.

