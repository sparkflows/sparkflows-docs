Hive Configurations
========

Sparkflows can be Configure with Hive with the existing instance in HPE UA. 

To configure Hive with the existing instance in HPE UA, we need to first copy the ssl_truststore file to the **/root directory**. To do this, use the following command:

#. Find the pod id of the sparkflows

   ::

       $ kubectl get po -n sparkflows

       NAME                                              READY   STATUS    RESTARTS   AGE
       hpe-fire-sparkflows-fire-858f44cb87-llhjd         2/2     Running   0          94m

#. Copy the ssl_truststore from the Unix machine

   ::

       $ kubectl cp ssl_truststore <pod-id>:/root -n sparkflows

#. Use the following connection string

   ::

        jdbc:hive2://xxxx.com:10000/default/undefined;ssl=true;auth=ldap;sslTrustStore=/root/ssl_truststore;trustStorePassword=xxxxx;user=hivetest;password=xxxxx

.. note:: Make sure to update the configurations with absolute path.

#. Acess Hive

Once the above configurations are saved, you can access Hive in **Data/Hive** and **workflows**
