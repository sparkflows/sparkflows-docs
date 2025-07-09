Sparkflows on HPE Data Fabric
=====
This document outlines the steps to install HPE Datafabric using the Datafabric Installer and configure it to mount volumes locally via NFS.

Data Fabric Installation
----
Use the Datafabric installer for a simplified installation on a VM. Follow the steps below to install the datafabric:

Step 1: Obtain the Authentication Token
++++
* Obtain the **token** from your HPE Support account, that will be used to authenticate, against the hpe installer packages. You need to login to the HPE support center as shown below.

  .. figure:: ../../_assets/hpe/hpe-support-center.png
      :width: 60%
      :alt: HPE Data Fabric

* Once logged in, click on the link below to navigate to the **token page**.
  
  https://support.hpe.com/hpesc/swd/entitlement-token-service/generate

  .. figure:: ../../_assets/hpe/hpe-token-page.png
      :width: 60%
      :alt: HPE Data Fabric


Step 2: Select a Node for Running the Installer
++++
* Select any node to run the Installer. It does not need to be one of the nodes on which you plan to install the cluster. 
* Download the **mapr-setup.sh** script. You can download the setup script directly from **package.ezmeral.hpe.com** to the node that will run the Installer:

  :: 

     wget --user=<email> --password=<token> 
     https://package.ezmeral.hpe.com/releases/installer/mapr-setup.sh -P /tmp


Step 3: Change Script Permissions
++++
* Change the file permissions so that you can run the file.

  ::
     
    chmod +x /tmp/mapr-setup.sh

Step 4: Run the Setup Script
++++
* Run the **mapr-setup.sh** script to configure the node to run the Installer. Run the following command as the **root user** from the directory that contains the script.

  ::

     /tmp/mapr-setup.sh -r https://<email>:<token>@package.ezmeral.hpe.com/releases/


**Note:** You must include your HPE Passport email and token and specify the name of the internet repository. The Installer remembers this information for later use. The script prompts you for some information. If you have not used this script before, consider reviewing **"Using mapr-setup.sh"** to be prepared.


Step 5: Start the Installer
++++
* Open the Installer URL in your browser: https://<Installer Node hostname/IPaddress>:9443
  
  You are prompted to log in as the **cluster administrator user** that you configured while running the mapr-setup.sh script.


Mounting Datafabric volumes
-----

**1.** Setup EDF to mount DF volumes to local mount points. This is made possible via NFS gateway of the MaprFS. Follow the steps below to mount the volumes locally:

  * Start the RPC Service

    ::

       service rpcbind start
       # OR using the below command to start it manually
       rpcbind -f -d

  * Start nfs-common

    ::

       service nfs-common start


  * Start the NFS Gateway

    ::

       /opt/mapr/bin/maprcli node services -name nfs -nodes maprdemo -action start

  * Mount the Volume Locally

    ::

       mount -o hard,nolock maprdemo:/mapr /mapr


  * Access your mounted Datafabric volume via the following path:

    ::

       /mapr/maprdemo.mapr.io/














































