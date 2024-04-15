Installing JupyterHub
==================

This document outlines the steps for installing JupyterHub.

Prerequisites
-------------

Before installing JupyterHub, ensure that you have the following:

* A Linux/Unix-based system.
* Python 3.6 or greater. An understanding of using pip for installing Python packages is helpful.
* nodejs/npm. Install nodejs/npm, using your operating system’s package manager. If you are using pip, install a recent version of nodejs/npm. 

  For example, install it on Linux (Debian/Ubuntu) using ::

    sudo apt-get install nodejs npm

  .. Note:: `nodesource <https://github.com/nodesource/distributions#table-of-contents>`_ is a great resource to get more recent versions of the nodejs runtime, if your system package manager only has an old version of Node.js (e.g. 10 or older).

Installation
------------

JupyterHub can be installed with pip (and the proxy with npm) using the below ::

 python3 -m pip install jupyterhub
 npm install -g configurable-http-proxy
 python3 -m pip install jupyterlab notebook  # needed if running the notebook servers in the same environment


Test your installation. If installed, these commands should return the packages’ help contents ::

 conda install -c conda-forge jupyterhub  # installs jupyterhub and proxy
 conda install jupyterlab notebook  # needed if running the notebook servers in the same environment   


Start the Hub Server
-----------------------

To start the Hub server, run the command ::

 jupyterhub

Visit **http://localhost:8000** in your browser, and sign in with your Unix credentials.

To allow multiple users to sign in to the Hub server, you must start jupyterhub as a privileged user, such as root ::

 sudo jupyterhub
