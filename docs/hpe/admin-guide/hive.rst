Hive Configurations
========

You can configure Sparkflows with an existing Hive instance in HPE UA. This document provides the steps to set up the connection.

Follow the steps given below.


Step 1 : Copy the ssl_truststore File to the Root Directory
------------------------------------------------------------
To configure Hive with Sparkflows, first copy the ssl_truststore file to the /root directory inside the Sparkflows pod.

#. Find the Pod ID of Sparkflows by using the following command: 

   ::

       $ kubectl get po -n sparkflows

       NAME                                              READY   STATUS    RESTARTS   AGE
       hpe-fire-sparkflows-fire-858f44cb87-llhjd         2/2     Running   0          94m

#. Copy the ssl_truststore file from your Unix machine to the Sparkflows pod using the command:
   ::

       $ kubectl cp ssl_truststore <pod-id>:/root -n sparkflows


Step 2 : Configure the Hive Connection String
----------------------------------------------------
#. Use the following connection string to connect to Hive:

   ::

        jdbc:hive2://xxxx.com:10000/default/undefined;ssl=true;auth=ldap;sslTrustStore=/root/ssl_truststore;trustStorePassword=xxxxx;user=hivetest;password=xxxxx

   .. note:: Ensure that the path to the ssl_truststore file is absolute.



Step 3 : Access Hive in Sparkflows
------------------------------------------

Once the configuration is saved, you can access Hive through the **Data/Hive** tab and in Workflows within Sparkflows.

