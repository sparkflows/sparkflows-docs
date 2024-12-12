Pre-requisites
^^^^^^^^^^^^^^

Below are the Prerequisites for installing Fire Insights on a windows machine::


  - JDK 8 installed.
  - java and jar have to be in the PATH
  - 8+ GB of RAM on the machine.
  

Check JDK 8 is installed
====================

* Check the JDK version installed on your machine::

    Open the command window 
    Type the following command to check your java version : java -version

* If JDK 8 is not installed, follow the JDK installation steps mentioned below.


Install JDK 8
====================

* Download JDK 8 for windows using the link below:

  * https://www.oracle.com/java/technologies/downloads/#java8

* Click on the link for the JDK download for Windows. On the Oracle page that opens, scroll down and select download the x64 Installer.

* This will start the download of the exe file. Login into your Oracle account, when prompted, to start the download. If you do not already have an Oracle account, create one to download the exe file.

* Once the exe is downloaded, double click on the file. This will start the JDK installation as shown below:

  .. figure:: ../../../_assets/installation/install-wizard-jdk.png
   :alt: Installations
   :width: 60%


* Click on the next button, which will take you to the installation page where the path for the JDK   installation directory will be displayed. Leave this as default and click on the next button.

  .. figure:: ../../../_assets/installation/installation-path-jdk.png
   :alt: Installations
   :width: 60%


* The JDK installation will start and progress on installation will be displayed as shown below:

  .. figure:: ../../../_assets/installation/progress-jdk.png
   :alt: Installations
   :width: 60%


* Once installation is complete, click on the close button

  .. figure:: ../../../_assets/installation/close-jdk.png
   :alt: Installations
   :width: 60%

Update JAVA_HOME and PATH variables
====================

* To complete the installation of the JDK, add the JAVA_HOME variable to the system environment variables and set the path to installation path of the JDK as shown below:

  .. figure:: ../../../_assets/installation/java_home.png
   :alt: Installations
   :width: 60%

* Additionally, the path variable may also updated to bin folder of the JDK installation path

  .. figure:: ../../../_assets/installation/path_env.png
   :alt: Installations
   :width: 60%

Verify installation of Java
====================

* To verify if the installation is successful, from the command prompt, type the below command:
  >java -version
  If the installation was successful, it will display the version of JDK that has been installed, as shown below:

  .. figure:: ../../../_assets/installation/java_version.png
   :alt: Installations
   :width: 60%

* To find the installation path of Java, run this command 
  >where java

.. note::  If you have multiple versions of Java installed on you system, you can update the PATH using the steps outlined in either of the links below:

           * https://javatutorial.net/set-java-home-windows-10
           * https://www.java.com/en/download/help/path.xml
           
 
.. note:: With the above steps, you would have Fire Insights running locally on your laptop. It would not be able to submit jobs to a Spark cluster. For that, Fire Insights has to be installed on the edge node of the cluster.


Install winutils.exe
====================

winutils.exe is needed for running Apache Spark/Hadoop on windows machines. Follow the below steps to setup winutils.exe on your machine

   
- Download winutils.exe from https://github.com/steveloughran/winutils

      - winutils.exe can be directly downloaded from link below:
      - https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe
      - https://github.com/kontext-tech/winutils/blob/master/hadoop-3.3.0/bin/winutils.exe (For hadoop-3.3.*)
  
- Create hadoop folder in Your System : ``C:\hadoop``.

  .. figure:: ../../../_assets/installation/create-hadoop_directory.PNG
   :alt: Installations
   :width: 60%

- Create bin folder in hadoop directory : ``C:\hadoop\bin``.

  .. figure:: ../../../_assets/installation/create-bin_directory.PNG
   :alt: Installations
   :width: 60%

- Copy the downloaded winutils.exe to the bin directory : ``C:\hadoop\bin\winutils.exe``.

  .. figure:: ../../../_assets/installation/winutils.PNG
   :alt: Installations
   :width: 60%

- Add a new Environment Variable. ``HADOOP_HOME = C:\hadoop``
  
  .. figure:: ../../../_assets/installation/hadoop_environment.PNG
   :alt: Installations
   :width: 60%

  
- Update the System Environment Variable PATH by adding : ``%HADOOP_HOME%\bin``.


  .. figure:: ../../../_assets/installation/hadoop_environment_path.PNG
   :alt: Installations
   :width: 60%

* Guide to setting Environment Variables on Windows

  https://www.architectryan.com/2018/08/31/how-to-change-environment-variables-on-windows-10/

Install hadoop.dll
====================

hadoop.dll is needed for running Apache Spark/Hadoop on windows machines. Follow the below steps to setup ''hadoop.dll'' on your machine

- Download hadoop.dll from 
    * https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/hadoop.dll
    * https://github.com/kontext-tech/winutils/blob/master/hadoop-3.3.0/bin/hadoop.dll 
 
- Copy ''hadoop.dll'' to ''windows/system32'' folder and restart the system.
- Copy ''hadoop.dll'' to : ``C:\hadoop\bin\winutils.exe``.

.. note:: Make sure to download the appropriate version

Install Microsoft C Runtime Library
====================

Download and Install Microsoft C Runtime Library based on your system architecture.

- Download from
    * https://www.microsoft.com/en-us/download/details.aspx?id=40784



