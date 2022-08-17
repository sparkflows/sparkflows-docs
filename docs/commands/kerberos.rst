Kerberos Commands
==============

https://spark.apache.org/docs/latest/security.html#using-a-keytab

https://kb.iu.edu/d/aumh#use

https://medium.com/analytics-vidhya/kerberos-and-hadoop-c8bdd7f1c7f3


* kinit using keytab::

    kinit -kt fire.keytab user@example.com 
    
* kinit using username::

    kinit username@Principal
    
* klist::

    klist -e -k -t fire.keytab
    klist (For details on validity and expirations of Service Principal)
    
* destroy existing ticket::

    kdestroy
    
* get the details on installed Kerberos libraries::

    krb5-config --all

