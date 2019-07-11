Windows Prerequisites
+++++++++++++

Below are the Prerequisites for installing Fire Insights on a windows machine::

  - JDK 1.8 installed.
  - java and jar have to be in the PATH
  - 5GB+ of RAM.
  - Python 3.X (when running Python and PySpark, otherwise not needed)

Check JDK 1.8
-------------

* Check the JDK version installed on your machine::

    Open terminal window 
    Type ``java -version``

* If JDK 1.8 is not installed, follow the JDK installation steps mentioned below.


Install JDK 1.8
---------------

* Download JDK 1.8 for windows using below link::

    https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

* Install java by double clicking on downloaded exe file

* After installation, make sure java is in the path::

    Open a new terminal window 
    Type ``java -version``


Python
------

If using Python and PySpark (not needed for the core features of Fire Insights) ::

  - Python 3.X can be set up with the Python virtual environment and activated
    * :doc:`../python-install`
    
 
.. note:: In order to connect Fire Insights to an Apache Spark cluster, it has to be installed on the edge node of the cluster.

   
