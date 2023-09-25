Installation
======

To install JupyterLab for Python in Ubuntu environment, you need to have python and pip available.

Use below command to install::


    pip install --upgrade pip
    pip install jupyterlab
    jupyter-lab --ip=0.0.0.0 --port=8888

It will open the interface in your default web browser.

Fire can be configured to Jupyter Notebook. Below are  the steps involved in it:

1. Login to Fire web server URL

Once login to Fire web server URL, Goto ``ADMINISTRATION -->> Configurations`` and select ``NOTEBOOK``.


.. figure:: ..//_assets/operating/jupyter_notebook_1.PNG
   :alt: operating
   :width: 60%

Update the below parameters:

::

    notebook.enabled : true
    notebook.serverHost : jupyternotebook server url which include token
    notebook.serverToken : Token being used
    
.. note::  Make sure to change localhost to your domain name or your IP where Fire is running and it should be accessible.   


2. Open Jupyter Notebook

Once the above configuration is saved, refresh the web server URL and you will see ''Jupyter Notebook'', Open it.

.. figure:: ..//_assets/operating/jupyter_notebook-access.PNG
   :alt: operating
   :width: 60%

3. Access Jupyter Notebook

Once you click on ''Jupyter Notebook'', it will open a new page for Jupyter Notebook and you can run the python code on top of it.

.. figure:: ..//_assets/operating/jupyter_notebook_2.PNG
   :alt: operating
   :width: 60%

.. figure:: ..//_assets/operating/jupyter_notebook_command.PNG
   :alt: operating
   :width: 60%
