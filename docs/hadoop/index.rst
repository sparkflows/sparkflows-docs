Hadoop Installation Guide
=========

Fire Insights is seamlessly integrated with Hadoop Distributed File system. With Fire Insights you can perform self-serve data processing, analytics and machine learning with data stored in HDFS.

In this guide, we'll see how we can setup Hadoop 3.x multi-node cluster.

**Note:** Do the following in all the nodes.

1. Install Java 1.8 and wget:: 

      sudo yum install -y java-1.8.0-openjdk-devel wget

2. Download and extract Hadoop 3.3.5::

      wget https://archive.apache.org/dist/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
      
      tar -xvf hadoop-3.3.5.tar.gz

3. Setup user for hadoop::

      sudo adduser hadoop
      sudo passwd hadoop
      sudo usermod -aG wheel hadoop
4. Configure hadoop installation directory::

      sudo mv /home/sparkflows/hadoop-3.3.5 /usr/local/hadoop
      sudo mkdir /usr/local/hadoop/logs
      sudo chown -R hadoop:hadoop /usr/local/hadoop

5. Configure SSH

   You need to configure it to allow passwordless SSH between the three machines. This step is essential because Hadoop requires passwordless SSH to communicate between the nodes in the cluster.

   To configure passwordless SSH, you need to generate SSH keys on the master node and copy the public key to the authorized_keys file on each of the slave nodes. You can generate SSH keys by running the following command on the master node::

      ssh-keygen -t rsa


   After generating the SSH keys, you can copy the public key to the authorized_keys file on each of the slave nodes using the following command::

     ssh-copy-id <slave-node-ip>


  

   

