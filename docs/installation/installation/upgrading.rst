Upgrading
==============

Stop Fire Server
--------------------------

Stop Fire server using the below command from Fire home directory::

    run-fire-server.sh stop


Download the new Fire tgz file
------------------------------

Download Fire tgz file from::

  - https://www.sparkflows.io/download  OR  
  
  - Via the direct link.
  
Unpack it
-----------

Unpack the tgz file::

    tar xvf fire-x.y.z.tgz

Upgrade the H2 or MySQL database
--------------------------------

* If you have updated the ``conf/db.properties`` file, copy it from your old location to the new directory.
* Backup your existing H2 database files. By default they are in your home directory as ``firedb.mv.db``
* If you are using MySQL, backup the fire database in MySQL.
* Execute the following commands to upgrade the Fire database schema::

    cd <install_dir>/fire-x.y.z
    
    ./create-h2-db.sh      OR     ./create-mysql-db.sh
    
``The above command creates or updates the existing db if one already exists.``


If PySpark engine is enabled, upgrade python dependencies as well
--------------------------------

* Activate the python environment by running from Fire home directory ``source env/bin/activate``.
* Upgrade the dependencies in the environment via ``pip install -r fire-x.y.x/dist/fire/requirements.txt``.

Restart Fire Server
-------------------

Restart the Fire server using the below command from Fire home directory::

  run-fire-server.sh start
