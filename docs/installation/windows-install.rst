Install on Windows OS
^^^^^^^^^^^^^^^^^^^^^^^

Fire Insights can be installed to run independenty on Windows.


Installation Steps of Fire Insights with H2 DB
----------------------------------------------

* Download the fire tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unpack it

Unpack the tgz file.

* Create H2 DB::

      cd <fire install_dir>
      .\create-h2-db.bat
    
* Launch Fire Server::

    cd <fire install_dir>
    .\run-fire-server.bat start

* Open your web browser and navigate to:: 
  
    <machine_name>:8080/index.html

* Login with:: 

    admin/admin or test/test



.. note::  You may change the password for the two accounts which come pre-configured to your choice of password from the Fire UI - Administration tab.

    admin/admin
    test/test

.. note:: In Local mode, Sparkflows Fire runs in a Jetty server and all the spark jobs are executed within the web-server

Stopping Fire
-------------

Stop Fire with the below::

    .\run-fire.bat stop
    
    
Stopping the Fire Server
------------------------

Stop the Fire Server with the below::

    .\run-fire-server.bat stop
    
    

