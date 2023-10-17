Install using Docker Image
==========
Sparkflows can be installed and run on Linux (Ubuntu) using the Docker image from the Docker Hub.

To download Sparkflows using Docker Image, follow the steps given below :

#. **Download and install Docker on your Linux machine**

   * Docker Desktop (https://docs.docker.com/engine/install/)
      * Download the Docker CE
      * Verify that the docker is up and running and the the docker version by running the following :
        ::
            docker --version
     
      * Executing the Docker Command Without Sudo(Optional) :
        ::
           sudo usermod -aG docker ${USER}

#. **Installation Steps**

   * Set up the environment variables. The local mount directory is (**/home/username/sparkflows**).

     Create this directory by using **mkdir** in the below docker run command. 

     Please update it to directory structure on your machine. 

     Replace **XX** with the Sparkflows version you want to install :
     ::
        export SPARK_VERSION=3.2.1
        export RELEASE_VERSION=3.X.XX
        export FIRE_VERSION=3.1.0
        export SPARKFLOWS_ROOT=/home/username/sparkflows

   * Pull the latest Sparkflows docker image from Docker hub :
     ::
         docker pull sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}


   * Start the docker image using the docker run command below :
  
     The local mount directory is (**/home/username/sparkflows**) in the below docker run command. 

     Please update it to directory structure on your machine. 

     Reduce/Increase the memory allocated to a lower value depending on the RAM on the machine. 

     Eg: Using ``-m 8g`` will allocate 8GB to the Sparkflows container.
     ::
        docker run -m 16g -p 8080:8080 -p 9443:9443 \
        -v ${SPARKFLOWS_ROOT}:/usr/local/fire-${RELEASE_VERSION}_spark_${SPARK_VERSION} \
        -e KEYSTORE_PASSWORD=12345678 \
        -e FIRE_HTTP_PORT=8080 \
        -e FIRE_HTTPS_PORT=9443 \
        -e FIRE_VERSION=${FIRE_VERSION} \
        sparkflows/fire:py_${SPARK_VERSION}_${RELEASE_VERSION}

     **Note :** We recommend 16GB or above.
     
     For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/docker-linux-install.html>`_


Step 5 : Accessing Sparkflows & Creating Users
++++
Pick the public IP or DNS of the machine from AWS Console -> Instances and hit the URL: http://sparkflows_IP:8080

By default Sparkflows comes with default user **admin** and **test** with default password as **admin** and **test** respectively.

If you want to create new users, it can be done from Sparkflows **Administration Tab** by choosing **Users** as shown in the image below :

      .. figure:: ../../_assets/aws/livy/administration.PNG
         :alt: livy
         :width: 60%

Step 6 : Reloading Sample Project
++++

Fire Insights by default comes with sample Project which can be reloaded in Fire Insight application.

For detailed information, `click here. <https://docs.sparkflows.io/en/latest/installation/installation/load-sample-projects.html>`_

Step 7 : Submitting Jobs to EMR Cluster
++++
By default Sparkflows job can be submitted on the local machine itself. 

It can be configured to submit the jobs to AWS EMR cluster for scalability.

For more information, `click here. <https://docs.sparkflows.io/en/latest/aws/admin-guide/emr-livy/index.html>`_
