Windows Installation using Installer
====================================

The Sparkflows installer for Windows installs, starts, upgrades and uninstalls Sparkflows on a laptop or desktop from a single application. It checks the prerequisites, downloads and extracts Sparkflows, sets up the Python virtual environment for the Agent and Polars engines, creates the H2 database and starts the server.

.. note:: On bare-metal Windows installations, the PySpark engine is not supported, so features like AutoML, Prophet, ARIMA, Scikit-learn, Keras/TensorFlow and some Python-native packages will be unavailable. For full functionality, use :doc:`docker-windows-install` or install Sparkflows on Linux.


Installer Prerequisites
-----------------------

* **Python 3.9 (64-bit)**: version 3.9.2 or later, and below 3.10 (3.9.2 to 3.9.x only). Python 3.9.0, 3.9.1 and 3.10 or later are not supported. It is used to create the Python virtual environment for the Agent and Polars engines. Download it from https://www.python.org/downloads/release/python-3913/.
* **Memory:** 8 GB RAM or more; 16 GB recommended.
* **Internet access**, to download Sparkflows (about 2.5 GB) and the Python packages.

The installer takes care of the rest:

* **Java 17** is bundled with the installer, so a separate Java installation is not needed.
* **winutils.exe** is downloaded to ``C:\hadoop\bin`` if it is not already present, and the ``HADOOP_HOME`` and ``PATH`` user environment variables are set automatically.


Download and Open the Installer
-------------------------------

#. Download the installer from `here <https://www.sparkflows.ai/download>`_ and install it.
#. Open **Sparkflows Installer** from the desktop shortcut or the Start menu.

The left menu of the installer has the following sections:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Menu
     - Use it to
   * - Dashboard
     - See the status of the installation and the server, and start, stop or restart Sparkflows.
   * - Install / Upgrade
     - Install Sparkflows, or upgrade it to a newer version. Shown as **Upgrade** once Sparkflows is installed.
   * - AI Agents & Apps
     - Follow step-by-step guides to get the values for LLM, vector database and JDBC connections.
   * - Logs
     - View the Sparkflows server logs and the Fire logs.
   * - History
     - See a record of installer and server activity.
   * - Update Installer
     - Update the installer application. Shown only when a new installer version is available.
   * - Documentation / Support
     - Open the Sparkflows documentation or the Sparkflows support page.
   * - Uninstall
     - Remove Sparkflows from the machine. Shown once Sparkflows is installed.


Install Sparkflows with the Installer
-------------------------------------

Open **Install** from the left menu and start the installation. The installer runs six steps in order, and shows the progress of each step on the right:

.. list-table::
   :widths: 25 75
   :header-rows: 1

   * - Step
     - What it does
   * - Prerequisites
     - Checks Java 17, winutils and Python (3.9.2 or later, below 3.10).
   * - Download
     - Downloads the Sparkflows installation package to ``C:\Users\<user>\fire``.
   * - Unzip
     - Extracts the downloaded package.
   * - Setup Python Venv
     - Creates the Python virtual environment (``engine-venv``) for the Agent and Polars engines.
   * - Create H2 DB
     - Creates the local H2 database (``firedb``) in the user home directory.
   * - Start Sparkflows
     - Starts the Sparkflows server.

#. **Prerequisites and download.** The download can be paused and resumed with the button on the **Download** step. If the network drops, the download retries automatically and resumes from where it stopped.

   .. figure:: ../../_assets/installer/windows/install-download-in-progress.png
      :alt: Download in progress
      :width: 80%

   .. figure:: ../../_assets/installer/windows/install-download-paused.png
      :alt: Download paused
      :width: 80%

#. **Unzip.** The package is extracted into the installation folder.

   .. figure:: ../../_assets/installer/windows/install-unzip.png
      :alt: Unzip in progress
      :width: 80%

#. **Setup Python Venv.** A window shows the output of the Python virtual environment setup while the required packages are installed. This takes a few minutes.

   .. figure:: ../../_assets/installer/windows/install-python-venv-window.png
      :alt: Python virtual environment setup window
      :width: 80%

#. **Create H2 DB and choose the port.** After the H2 database is created, the installer asks which port Sparkflows should run on. Click **CONTINUE** to use port 8080, or **CHANGE PORT NUMBER** to enter another port.

   .. figure:: ../../_assets/installer/windows/install-port-prompt.png
      :alt: Port prompt
      :width: 80%

   .. figure:: ../../_assets/installer/windows/install-change-port-dialog.png
      :alt: Change port dialog
      :width: 40%

   The port must be between 1024 and 49151, and must not be in use by another application.

#. **Start Sparkflows.** Sparkflows starts on the chosen port, and the browser opens the Sparkflows login page. All steps show **Complete**, and the **Start Sparkflows** step shows **Running**.

   .. figure:: ../../_assets/installer/windows/install-complete-server-running.png
      :alt: Installation complete
      :width: 80%

   Use **OPEN IN BROWSER** to open Sparkflows again, or **CHANGE PORT** to move it to another port. Changing the port stops the server and starts it again on the new port.

#. Login with the default user ``admin`` / ``admin``.

Click **VIEW INSTALLATION LOGS** at the top right of the page to see the installation-level logs. The **Installation Error Log** tab shows any errors.

.. figure:: ../../_assets/installer/windows/install-installation-logs.png
   :alt: Installation logs
   :width: 80%

If a step fails, the **Dashboard** shows **RETRY INSTALLATION**, or **CONTINUE INSTALLATION** if Sparkflows was already downloaded.


Installer Dashboard
-------------------

The **Dashboard** shows the state of the installation and the server.

.. figure:: ../../_assets/installer/windows/dashboard-running.png
   :alt: Dashboard with Sparkflows running
   :width: 80%

* **Current Build**: the installed Sparkflows version. It shows **LATEST**, or **UPDATE AVAILABLE** when a newer version can be installed.
* **Quick Actions**:

  * **Open Sparkflows**: opens Sparkflows in the browser.
  * **Stop Service** / **Start Service**: stops or starts the Sparkflows server.
  * **Restart**: restarts the Sparkflows server.
  * **Open Folder**: opens the installation folder in File Explorer.

* **Installation Path**: the installation folder, the free disk space and the installation date.
* **Python**: the Python version and the path of the Python virtual environment. Click **View installed packages** to list the Python packages in the virtual environment.
* **Server**: whether the server is running, its URL and the default admin login.
* **Java & Hadoop**: the Java version in use and the winutils location.
* **H2 Database**: the database files, their size and their folder.
* **Recent Activity**: the latest installer and server events. Click **View All Activities** to open **History**.

Use the copy icon next to a path to copy it.

.. figure:: ../../_assets/installer/windows/dashboard-details.png
   :alt: Dashboard details
   :width: 80%

.. figure:: ../../_assets/installer/windows/dashboard-installed-python-packages.png
   :alt: Installed Python packages
   :width: 60%

When the server is stopped, the **Server** card shows **STOPPED**, and **Start Service** replaces **Stop Service**:

.. figure:: ../../_assets/installer/windows/dashboard-stopped.png
   :alt: Dashboard with the server stopped
   :width: 80%

When Sparkflows is started from the Dashboard, the installer asks for the port to use, the same as during installation.


AI Agents & Apps
----------------

**AI Agents & Apps** is a reference for setting up the connections that AI Agents and Applications in Sparkflows need. Nothing here is configured in the installer: follow the steps to get the values, then add them in Sparkflows under **Administration -> Global & Groups Connections**. Click **READ THE GUIDE** to open the matching connection guide in the documentation.

* **AI Agents** tab: steps to create an API key and choose a model for **Azure OpenAI**, **OpenAI**, **Gemini** and **Anthropic**, and to create a **Pinecone** index for agents that search your own documents.
* **Applications** tab: steps to install **MySQL** or **PostgreSQL** and create the database used by Sparkflows Applications through a JDBC connection.

Each guide ends with the exact values to enter in the Sparkflows connection.

.. figure:: ../../_assets/installer/windows/ai-agents-azure-openai.png
   :alt: AI Agents - Azure OpenAI
   :width: 80%

.. figure:: ../../_assets/installer/windows/ai-agents-openai.png
   :alt: AI Agents - OpenAI
   :width: 80%

.. figure:: ../../_assets/installer/windows/ai-agents-gemini.png
   :alt: AI Agents - Gemini
   :width: 80%

.. figure:: ../../_assets/installer/windows/ai-agents-anthropic.png
   :alt: AI Agents - Anthropic
   :width: 80%

.. figure:: ../../_assets/installer/windows/ai-agents-pinecone.png
   :alt: AI Agents - Pinecone
   :width: 80%

.. figure:: ../../_assets/installer/windows/applications-mysql.png
   :alt: Applications - MySQL
   :width: 80%

.. figure:: ../../_assets/installer/windows/applications-postgresql.png
   :alt: Applications - PostgreSQL
   :width: 80%


Installer Logs
--------------

**Logs** shows the Sparkflows logs inside the installer:

* **VIEW SERVER LOGS**: the Sparkflows server activity.
* **VIEW FIRE LOGS**: node-level request handling and local job communication.

The **Log Viewer** shows the latest entries. Use **REFRESH** to reload it, **OPEN LOG FILE** to open the full log file, and the arrow button to jump to the end.

.. figure:: ../../_assets/installer/windows/logs-server.png
   :alt: Server logs
   :width: 80%

.. figure:: ../../_assets/installer/windows/logs-fire.png
   :alt: Fire logs
   :width: 80%


Installer History
-----------------

**History** is a chronological record of installer and server activity, such as downloads, database creation, port changes, and server starts and stops. Use **Search** to find an entry, and the drop-down to show **All activity**, only **Server** activity or only **Installation** activity.

.. figure:: ../../_assets/installer/windows/history.png
   :alt: History
   :width: 80%

.. figure:: ../../_assets/installer/windows/history-filter.png
   :alt: History filter
   :width: 80%


Upgrade Sparkflows
------------------

When the installer starts, it checks whether a newer version of Sparkflows is available. If there is one, it shows a **Sparkflows Update Available** notification with the new version number. Click **Upgrade** to go to the **Upgrade** page, or **Dismiss** to upgrade later.

If a new version of the installer itself is available, an **Installer Update Available** notification is shown as well. See `Update the Installer`_.

.. figure:: ../../_assets/installer/windows/upgrade-notifications.png
   :alt: Update notifications
   :width: 80%

After the notification is dismissed, the **Dashboard** still shows **UPDATE AVAILABLE** under **Current Build**:

.. figure:: ../../_assets/installer/windows/dashboard-update-available.png
   :alt: Dashboard with an update available
   :width: 80%

To upgrade:

#. Open **Upgrade** from the left menu, then click **UPGRADE**.

   .. figure:: ../../_assets/installer/windows/upgrade-available-page.png
      :alt: Upgrade page with an update available
      :width: 80%

#. Click **OK** to confirm. The installer stops the running Sparkflows server during the upgrade.

   .. figure:: ../../_assets/installer/windows/upgrade-confirm.png
      :alt: Upgrade confirmation
      :width: 45%

#. The installer backs up the existing installation, then downloads, extracts and sets up the new version using the same steps as the installation, and starts Sparkflows again.

If the upgrade fails, the installer rolls back to the previous version automatically. Start the server again from the **Dashboard**. If an upgrade is interrupted, the Dashboard shows **RESUME UPGRADE** to finish it.

When Sparkflows is already on the latest version, the **Upgrade** page has no **UPGRADE** button and shows the steps of the current installation.

.. figure:: ../../_assets/installer/windows/upgrade-page.png
   :alt: Upgrade page on the latest version
   :width: 80%


Update the Installer
--------------------

When a new version of the installer is available, the **Installer Update Available** notification is shown, and an **Update Installer** item appears in the left menu. Click **Update** on the notification, or open **Update Installer** from the menu.

.. figure:: ../../_assets/installer/windows/update-installer.png
   :alt: Update Installer page
   :width: 80%

The page shows the installer version you are running and the latest available version. To update:

#. Click **Stop Service** to stop Sparkflows. Your server, database and logs are not changed; only the installer application is replaced.
#. Download the new installer. ``sparkflows-installer.exe`` is recommended on Windows.
#. Close the installer, then run the new installer to install the new version.

The installer version is shown at the bottom of the left menu. Click **CHECK AGAIN** to check for a newer installer.


Uninstall Sparkflows
--------------------

#. Click **Uninstall** at the bottom of the left menu.
#. Review the list of files that will be removed: the installation folder and the H2 database files.
#. Click **UNINSTALL** to remove them, or **CANCEL** to keep Sparkflows.

.. figure:: ../../_assets/installer/windows/uninstall-confirm.png
   :alt: Uninstall confirmation
   :width: 45%

The installer stops Sparkflows before removing files. If Sparkflows cannot be stopped, or a file is in use by another program, no files are removed and the installer lists the steps to follow. Uninstalling cannot be undone.
