Using TGZ File
=========
This document outlines the steps required to install Sparkflows on a GCP virtual machine (VM) using a TGZ file.

Follow the steps given below to complete the installation:

Step 1 : SSH into the GCP VM
------------
   
**SSH into the Azure Instance using these steps:**

* Obtain the Public IPv4 address from the GCP console. 
* Use the PEM file (key file) that was downloaded while bringing up the Azure VM.
* Execute the following command to establish the SSH connection:
  ::
      ssh -i sparkflows.pem sparkflows@21.xxx.xxx.113

  

 .. Note::
            * Run all the below steps as a 'user with sudo permission'. If unsure, please run the below commands as a 'root' user.
            * If you are using Ubuntu, you may have to run the following command and then select '**No**'. 

              ::

                 sudo dpkg-reconfigure dash

Step 2 : Follow the Installation steps
---------------
Once you have successfully SSH'd into the VM, proceed with the installation process by following the appropriate documentation based on your operating system:

* **For Linux**, follow this documenation:
  https://docs.sparkflows.io/en/latest/installation/installation/linux-install.html

* **For Windows**, follow this documentation:
  https://docs.sparkflows.io/en/latest/installation/installation/windows-install.html

