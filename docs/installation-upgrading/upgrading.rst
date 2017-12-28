Upgrading
---------

Stop Fire if it is running
--------------------------

Download and unzip the Fire tgz file
------------------------------------

  * Download the fire tgz file

  * Unzip it : **tar xvf fire-1.4.2.tgz**

Upgrade the H2 or MySQL database
--------------------------------

  * If you have updated the conf/db.properties file, copy it from your old location to the new directory
  * Backup your existing H2 db files. By default they are in your home directory as firedb.mv.db
  * If you are using MySQL, backup the fire database in MySQL.
  * Execute the following commands on the Command Line to upgrade the Fire database


    * cd <install_dir>/fire-1.4.2

    * ./create-h2-db.sh      OR     ./create-mysql-db.sh
    
        (the above command creates or updates the existing db if one already exists)​


Restart Fire
-------------

