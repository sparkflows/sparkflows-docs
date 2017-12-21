Configuring Kerberos
--------------------

Fire runs with a kerberized Spark cluster. Below are the steps for configuring it:
 
* **Generate a keytab for Fire**
 
        
 
* **Place it in .../fire-1.x.y/conf directory**
 
         This is not required as keytab directory is configurable although this is a good place to put it.
 
         Make sure only the user running fire application has access to the keytab. For example:
 
         **-rw------- 1 sparkflows staff 436 Jun 29 16:06 hive.keytab**
 
         Ideally, take away the write access too, as no one should be able to modify a keytab once its been generated.
 
* **Go to Administration/Configuration and update the following configurations to enable Kerberos for Fire**


+-------------------------+-------+------------------------------------------------------+
| Configuration           | Value | Details                                              |
+-------------------------+-------+------------------------------------------------------+
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

