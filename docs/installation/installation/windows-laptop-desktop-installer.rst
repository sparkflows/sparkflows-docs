Windows Installer for Laptop and Desktop
====================================
You can download and use the installer to install or upgrade Fire Insights on your laptop or desktop.

It is not recommended to use this installer on servers, where you need better control over the installation process.



Step 1 : Verify Prerequisites
-----------------------------

#. **JDK 1.8:** Ensure you have JDK 1.8 installed. You can download and install Java 8 from `here. <https://www.oracle.com/java/technologies/javase-jdk8-downloads.html>`_
#. **Permissions:** 

   * Ensure you have sufficient permissions to download and install Sparkflows in the user directory.
   * You need write permission to download winutils.exe inside the Windows directory and set the environment path.
#. **Set JAVA_HOME:**

   * After installing Java, you may need to set JAVA_HOME.
   * If you have multiple versions of Java installed on your system, you can update the PATH using the steps outlined in either of the links below:

     * `Set JAVA_HOME on Windows 10 <https://javatutorial.net/set-java-home-windows-10>`_
     * `Update PATH for Java <https://www.java.com/en/download/help/path.xml>`_
           

Step 2 : Download the Installer
---------------------

#. Download the installer from `here. <https://www.sparkflows.io/windows-download>`_


Step 3 : Install Sparkflows
----------------------------

#. Once downloaded, open and run the installer file. The default installer dashboard appears when you open the installer. Click the **Install Sparkflows** button to proceed to the install menu.

   .. figure:: ../../_assets/installer/initial-dashboard-view.jpg
      :alt: Installations
      :width: 60% 

#. In the Install menu, a list of the available Java versions currently present on the system will be displayed. Click the **Start Install** button to begin the installation of Sparkflows.

   .. figure:: ../../_assets/installer/initial-install-menu.jpg
      :alt: Installations
      :width: 60% 

#. After starting the installation, the Install Menu Dashboard will display further information related to winutils, the Java version, and their paths. It will also show the download progress and the location where the file is being downloaded.

   .. figure:: ../../_assets/installer/download-progress.jpg
      :alt: Installations
      :width: 60% 

#. Once the .tgz file is downloaded, it will be unzipped, and the H2 DB required to start Sparkflows will be created.

   .. figure:: ../../_assets/installer/unzipping-creatingdb.jpg
      :alt: Installations
      :width: 60% 

#. After the H2 DB is created, a prompt will appear to choose the port on which Sparkflows should run. If you press the **Continue** button, it will run on port 8080 by default.

   .. figure:: ../../_assets/installer/setting-port.jpg
      :alt: Installations
      :width: 60% 

#. If you click the **Change Port Number** button, you will be prompted to enter a new port number. After entering the new port number, press the **OK** button to start Sparkflows on that port.

   .. figure:: ../../_assets/installer/changing-port.jpg
      :alt: Installations
      :width: 60% 

   A message displaying **Starting Sparkflows on port** will appear in the Install Menu Dashboard.

   .. figure:: ../../_assets/installer/starting-sparkflows.jpg
      :alt: Installations
      :width: 60% 

   After Sparkflows has started, the message **Started Sparkflows on port** will be displayed in the Install Menu Dashboard, and the browser will automatically open and navigate to the Sparkflows login page.

   .. figure:: ../../_assets/installer/started-sparkflows.jpg
      :alt: Installations
      :width: 60% 

   .. figure:: ../../_assets/installer/started-sparkflows-browser.jpg
      :alt: Installations
      :width: 60% 

#. Login with the below credentials:
    - Username : admin
    - Password : admin

.. note::  On Windows, the PySpark engine will not get installed. Below are he funcationalities that will not be available on bare metal windows install. We recommend either docker on windows to access all functionalities or install Sparkflows on Linux:

           * AutoML
           * Prophet
           * ARIMA
           * Scikit learn models
           * Keras/Tensorflow models
           * A few other python native packages

Step 4 : Post-Installation Configuration
----------------------------------------

#. After Sparkflows has started, navigate to the Installer Dashboard Menu. It will be updated with data such as the Sparkflows server URL, status of the Sparkflows server, Java version being used and its related information, winutils location, H2 database status, and its related information.

   .. figure:: ../../_assets/installer/dashboard-after-start.jpg
      :alt: Installations
      :width: 60% 

#. If you stop the Sparkflows server by clicking the **Stop Sparkflows** button, the installer dashboard will be updated accordingly.

   .. figure:: ../../_assets/installer/dashboard-after-stop.jpg
      :alt: Installations
      :width: 60% 

#. Logs are accessible by navigating to the logs menu. Clicking the **View Server Logs** or **View Fire Logs** buttons will display the respective logs in a new window.

   .. figure:: ../../_assets/installer/logs-view-page.jpg
      :alt: Installations
      :width: 60% 

#. The history of actions related to the Sparkflows installer will also be visible in the History Menu in a table, showing the time when each action took place.

   .. figure:: ../../_assets/installer/history-page.jpg
      :alt: Installations
      :width: 60%
