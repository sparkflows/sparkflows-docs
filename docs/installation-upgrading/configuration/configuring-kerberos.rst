Configuring Kerberos
====================

Fire runs with a kerberized Spark cluster. Below are the steps for configuring it:
 
* **Generate a keytab for Fire**
 
        
 
* **Place it in .../fire-1.x.y/conf directory**::
 
    This is not required as keytab directory in Fire is configurable although this is the recommended location.
 
* **Make sure only the user running fire application has access to the keytab**. For example::
 
    -rw------- 1 sparkflows staff 436 Jun 29 16:06 hive.keytab
 
    Ideally, take away the write access too, as no one should be able to modify a keytab once its been generated.
 
* **Go to Administration/Configuration and update the following configurations to enable Kerberos for Fire**


+-------------------------+-------+------------------------------------------------------+
| Configuration           | Value | Details                                              |
+=========================+=======+======================================================+
| kerberos.enabled        | true  | Set it to true to enable Kerberos for Sparkflows     |
+-------------------------+-------+------------------------------------------------------+
| kerberos.keytab         |       | Absolute path of the keytab generated for Sparkflows |
+-------------------------+-------+------------------------------------------------------+
| kerberos.principal      |       | Kerberos Principal of the keytab of Sparkflows       |
+-------------------------+-------+------------------------------------------------------+
| kerberos.KERBEROS_REALM |       | Kerberos Realm                                       |
+-------------------------+-------+------------------------------------------------------+
| kerberos.KERBEROS_KDC   |       | KDC Server                                           |
+-------------------------+-------+------------------------------------------------------+

Steps for generating the keytab for Fire
----------------------------------------

Below are the steps for generating the keytab file. **We have chosen sparkflows as the principal name. But you can have it as any user you are running Sparkflows Fire with**.

* **Start kadmin.local and add the new principal ``sparkflows@VENICE.HADOOP``**::

    $ kadmin.local
 
    kadmin.local: addprinc -randkey sparkflows@VENICE.HADOOP
                                         
    WARNING: no policy specified for sparkflows@VENICE.HADOOP; defaulting to no policy
    Principal "sparkflows@VENICE.HADOOP" created.

* **Create sparkflows key tab file**::

    kadmin.local: xst -norandkey -k sparkflows.keytab sparkflows@VENICE.HADOOP

    Entry for principal sparkflows@VENICE.HADOOP with kvno 1, encryption type aes256-cts-hmac-sha1-96 added to keytab

    WRFILE:sparkflows.keytab.

    Entry for principal sparkflows@VENICE.HADOOP with kvno 1, encryption type aes128-cts-hmac-sha1-96 added to keytab

    WRFILE:sparkflows.keytab.

    Entry for principal sparkflows@VENICE.HADOOP with kvno 1, encryption type des3-cbc-sha1 added to keytab     WRFILE:sparkflows.keytab.

    Entry for principal sparkflows@VENICE.HADOOP with kvno 1, encryption type arcfour-hmac added to keytab WRFILE:sparkflows.keytab.

    Entry for principal sparkflows@VENICE.HADOOP with kvno 1, encryption type des-hmac-sha1 added to keytab WRFILE:sparkflows.keytab.

    Entry for principal sparkflows@VENICE.HADOOP with kvno 1, encryption type des-cbc-md5 added to keytab WRFILE:sparkflows.keytab.


* **Exit kadmin.local**::

    kadmin.local: exit
 
 
 
Verifying that the keytab file was correctly created
----------------------------------------------------

Below are the steps for verifying the keytab file::

    $ ls -l sparkflows.keytab
    -rw------- 1 root root 382 Jul 24 17:55 sparkflows.keytab
 
    Further verify the contents of keytab file. A normal keytab file depending on your krb5.conf settings, looks like this
 
    $ klist -e -k -t sparkflows.keytab

    Keytab name: FILE:sparkflows.keytab

    KVNO Timestamp Principal
    .....................................................................................................................................................
    1 07/24/16 17:55:07 sparkflows@VENICE.HADOOP (aes256-cts-hmac-sha1-96)

    1 07/24/16 17:55:08 sparkflows@VENICE.HADOOP (aes128-cts-hmac-sha1-96)

    1 07/24/16 17:55:08 sparkflows@VENICE.HADOOP (des3-cbc-sha1)

    1 07/24/16 17:55:08 sparkflows@VENICE.HADOOP (arcfour-hmac)

    1 07/24/16 17:55:08 sparkflows@VENICE.HADOOP (des-hmac-sha1)

    1 07/24/16 17:55:08 sparkflows@VENICE.HADOOP (des-cbc-md5)


