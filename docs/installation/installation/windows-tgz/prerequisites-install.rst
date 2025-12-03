Prerequisites
^^^^^^^^^^^^^^

Below are the Prerequisites for installing Sparkflows on a windows machine::


  - JDK 17 installed.
  - java and jar have to be set in the PATH
  - 8+ GB of RAM on the machine.
  

Check JDK 17 is installed
====================

* Check the JDK version installed on your machine::

    Open the command prompt 
    Type the following command to check your java version : java -version

* If JDK 17 is not installed, it will display the message as below: 

  .. figure:: ../../../_assets/installation/check-java-installed.png
   :alt: Installations
   :width: 60%

   
   Now, follow the JDK 17 installation steps mentioned below.


Steps to Install JDK 17
====================

1. Download JDK 17 for windows using the link below:

   https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html

2. On the Oracle page that opens, scroll down and search **Windows x64 Installer**. Click on the download link. This will start the download of the **.exe** file. Log in to your Oracle account when prompted to start the download. If you do not already have an Oracle account, create one to download the **.exe** file.


3. Once the .exe file is downloaded, double-click it to start the JDK installation, as shown below:

   .. figure:: ../../../_assets/installation/install-wizard-jdk.png
     :alt: Installations
     :width: 60%


4. Click on **Next** button, which will take you to the installation page where the path for the JDK installation directory will be displayed. Leave this as default and click on **Next** button.

   .. figure:: ../../../_assets/installation/installation-path-jdk.png
      :alt: Installations
      :width: 60%


   The JDK installation will start and progress on installation will be displayed on the wizard.

5. Once the installation is complete, click on **Close** button to finish the setup.

   .. figure:: ../../../_assets/installation/close-jdk.png
      :alt: Installations
      :width: 60%

Update JAVA_HOME and PATH variables
====================

* To complete the installation of the JDK, add the JAVA_HOME variable to the system environment variables and set the path to installation path of the JDK as shown below:

  .. figure:: ../../../_assets/installation/java_home.png
   :alt: Installations
   :width: 60%

* Additionally, the path variable may also be updated to bin folder of the JDK installation path, as shown below.

  .. figure:: ../../../_assets/installation/path_env.png
   :alt: Installations
   :width: 60%

Verify Installation of Java
====================

* To verify that the installation was successful, open the Command Prompt and type the command: **java -version**. If the installation was successful, the version of the installed JDK will be displayed, as shown below:

  .. figure:: ../../../_assets/installation/java_version.png
   :alt: Installations
   :width: 60%

* To find the installation path of Java, run the command: **where java**.

.. note::  If you have multiple versions of Java installed on your system, you can update the PATH using the steps outlined in either of the links below:

           * https://javatutorial.net/set-java-home-windows-10
           * https://www.java.com/en/download/help/path.xml
           
 
.. note:: With the above steps, you would have Sparkflows running locally on your laptop. It would not be able to submit jobs to a Spark cluster. For that, Sparkflows has to be installed on the edge node of the cluster.


Install winutils.exe
====================

**winutils.exe** is needed for running Apache Spark/Hadoop on windows machines. Follow the steps below to setup winutils.exe on your machine:

   
- Download winutils.exe from https://github.com/steveloughran/winutils

      - winutils.exe can be directly downloaded from link below:
      - https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/winutils.exe
      - https://github.com/kontext-tech/winutils/blob/master/hadoop-3.3.0/bin/winutils.exe (For hadoop-3.3.x)
  
- Create hadoop folder in your system : ``C:\hadoop``.

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

- Add a new Environment Variable : ``HADOOP_HOME = C:\hadoop``.
  
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

**hadoop.dll** is needed for running Apache Spark/Hadoop on windows machines. Follow the steps below to setup ''hadoop.dll'' on your machine:

- Download hadoop.dll from 

    * https://github.com/steveloughran/winutils/blob/master/hadoop-2.7.1/bin/hadoop.dll 
    * https://github.com/kontext-tech/winutils/blob/master/hadoop-3.3.0/bin/hadoop.dll (For hadoop-3.3.x)
 
- Copy ''hadoop.dll'' to ''windows/system32'' folder and restart the system.
- Copy ''hadoop.dll'' to : ``C:\hadoop\bin\winutils.exe``.

.. note:: Make sure to download the appropriate version.

Install Microsoft C Runtime Library
====================

Download and Install Microsoft C Runtime Library based on your system architecture. As Hadoop does rely on some native libraries for certain operations (like filesystem access or compression), and on Windows, you may encounter DLL-related errors if these libraries are not properly set up.

- Download from

    * https://www.microsoft.com/en-us/download/details.aspx?id=40784



