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

6. Configure Hadoop environment
    a. Find the JAVA Home directory::
            
            readlink -f /usr/bin/javac
    b. Add the java home directory and hadoop installation directory in hadoop-env.sh ( at the end)::

            export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.382.b05-1.el7_9.x86_64
            export HADOOP_CLASSPATH+="$HADOOP_HOME/lib/*.jar"

7. Configure user .bashrc
    Now that you have the Hadoop environment setup, it's time to configure the currently logged-in user setting so that you can run the Hadoop commands from anywhere.
    Copy and paste the following as per the installation directory::
      
      export HADOOP_HOME=/usr/local/hadoop
      export SPARK_HOME=/home/sparkflows/spark
      export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
      export HADOOP_INSTALL=$HADOOP_HOME
      export HADOOP_MAPRED_HOME=$HADOOP_HOME
      export HADOOP_COMMON_HOME=$HADOOP_HOME
      export HADOOP_HDFS_HOME=$HADOOP_HOME
      export YARN_HOME=$HADOOP_HOME
      export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
      export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin:$SPARK_HOME/bin
      export HADOOP_OPTS="-Djava.library.path=$HADOOP_HOME/lib/native"

8. Javax activation
   Install Javax by going to the hadoop directory::

      cd /usr/local/hadoop/lib
      sudo wget https://jcenter.bintray.com/javax/activation/javax.activation-api/1.2.0/javax.activation-api-1.2.0.jar

      Verify your hadoop by typing hadoop version::

      $ hadoop version
      
      Hadoop 3.3.5
      Source code repository https://github.com/apache/hadoop.git -r 706d88266abcee09ed78fbaa0ad5f74d818ab0e9
      Compiled by stevel on 2023-03-15T15:56Z
      Compiled with protoc 3.7.1
      From source with checksum 6bbd9afcf4838a0eb12a5f189e9bd7
      This command was run using /usr/local/hadoop/share/hadoop/common/hadoop-common-3.3.5.jar


9. Edit core-site.xml
   The core-site.xml file tells the Hadoop daemon where NameNode is located in the cluster. It contains Hadoop Core configuration settings such as I/O settings shared by HDFS and MapReduce.::

      sudo vi $HADOOP_HOME/etc/hadoop/core-site.xml

   Copy following lines and paste it in core-site.xml::

      <configuration>
       <property>
       <name>fs.default.name</name>
             <value>hdfs://<namenode-ip>:9000</value>
       <description>The default file system URI</description>
       </property>
      </configuration>

10. Make a directory for node metadata storage and give it hadoop’s ownership::

      sudo mkdir -p /home/hadoop/hdfs/{namenode,datanode}
      sudo chown -R hadoop:hadoop /home/hadoop/hdfs









  

   

