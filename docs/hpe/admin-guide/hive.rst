Hive Connection
========

Sparkflows can be Configure with Hive with the existing instance in HPE UA. 

To configure Hive with the existing instance in HPE UA, we need to first copy the ssl_truststore file to the **/root directory**. To do this, use the following command:

#. Find the pod id of the sparkflows

::

    $ kubectl get po -n sparkflows

    NAME                                              READY   STATUS    RESTARTS   AGE
    hpe-fire-sparkflows-fire-858f44cb87-llhjd         2/2     Running   0          94m
