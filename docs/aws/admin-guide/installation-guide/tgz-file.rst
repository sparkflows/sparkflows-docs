Using TGZ File
=========
This document explains in detail the steps required to install Sparkflows in an AWS Instance using tgz file.

Follow the below steps to install Sparkflows using tgz file :

Step 1 : SSH into the AWS Instance
------------
   
#. SSH into the AWS Instance using:

   * Public ipv4 IP from the AWS console and 
   * The `PEM` file (key file) downloaded while bringing up the AWS Instance and
   * The command as below :
     ::
         ssh -i sparkflows.pem ec2-user@21.xxx.xxx.113

  

 .. Note::
            * Run all the below steps as a user with sudo permission. If unsure, please run the below commands as `root` user.
            * If you are using Ubuntu, you may have to run the following and then select ``No``. 

            ::

              sudo dpkg-reconfigure dash

Step 2 : Follow the Installation steps below
---------------
Now that you have SSH'd into the VM, you can follow the documentation below to complete the installation process.

For Linux, follow the documenation here:
https://docs.sparkflows.io/en/latest/installation/installation/linux-installation/index.html

For Windows, follow the documentation here:
https://docs.sparkflows.io/en/latest/installation/installation/windows-tgz/index.html

