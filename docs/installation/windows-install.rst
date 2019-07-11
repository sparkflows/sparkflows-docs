Install on Windows OS
^^^^^^^^^^^^^^^^^^^^^^^

Fire Insights can be installed to run independenty on Windows.


Installation Steps of Fire Insights with H2 DB
----------------------------------------------

* Download the fire tgz file from:

  * https://www.sparkflows.io/download  OR   
  * https://www.sparkflows.io/archives
  
  
* Unpack the downloaded tgz file. Below are some tools which can be used for it::

    WinRar : https://www.rarlab.com/download.htm
    WinZip : https://www.winzip.com
    7-Zip : https://www.7-zip.org/download.html

    
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

    
    
.. note::  Two user accounts come preconfigured with Fire Insights.

           * admin/admin
           * test/test
    
    You may change these usernames and passwords in Fire under the menu Administration/Users 



Stopping Fire
-------------

Stop Fire with the below::

    .\run-fire.bat stop
    
    
Stopping the Fire Server
------------------------

Stop the Fire Server with the below::

    .\run-fire-server.bat stop
    
    

