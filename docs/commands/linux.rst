Linux Commands
===============
    
Find disk usage
----------------

::

    df -h


Find the size of the various folders
-------------------

::

    du -sh *

Remove all the wheel files in the cache
-----------

::

    pip cache purge

Create and Remove directory
--------------

::

    mkdir directoryname
    rmdir directoryname
    

Compare two files
---------------

::

    diff -y -W 70 test.txt test1.txt 

Find file with name
------------------

::

    find . -name *ones*

Summary of the memory usage
-------------------------

::

    free -h

Search for lines which contain a search pattern
------------------------------

::

   grep train *.txt

History of commands
-------------------

::

   history

List command
------------

::

   ls -lh

Move command
----------

::

   mv source destination
   
List Files in directory and subdirectory
----------------

::

    ls -R

Lists running processes
------------

::

    ps

Lists running java processes
------------

::

    ps aux | grep -i --color java
    
    
Find current directory path
---------------

::

    pwd

Find real-time display of the data
---------------

::

   top

Find system information
-------------

::

    uname -a

List the currently logged in users
----------

::

    w

Find IP
----------

::

    ifconfig

Check Memory use in Linux
------------

::

    cat /proc/meminfo

Check Maximum User Process on Linux
------------

::

    ulimit -u

thread count of all the proceses run by User on Linux
------------

::

    ps -eLf | grep 'myuser' | wc -l

View the list of processes
------------

::

    top
    
Download Files
--------------

Using wget::

    wget https://domainname.com/abc.csv
    
    
Using curl::

    curl https://domainname.com/abc.csv -o abc.csv
    curl -LO https://domainname.com/abc.csv

clear command
--------------

::

    clear
    
    
