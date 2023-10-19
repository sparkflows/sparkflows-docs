Installation
======

To install JupyterLab for Python on Ubuntu environment, you need to have python and pip available.

Use below command to install: ::


    pip install --upgrade pip
    pip install jupyterlab
    jupyter lab --generate-config

   Above command will generate jupyter_lab_config.py in ~/.jupyter directory

Change to directory .jupyter - cd ~/.jupyter directory

Customize the jupyter_lab_config.py file of jupyterlab and change the configuration below::

    NotebookApp
    .open_browser = False
    ServerApp
    .allow_origin = '*'
    .certfile = '/home/ubuntu/fullchain.pem' # ssl certificate
    .config_file = '~/.jupyter/jupyter_lab_config.py' #config file path
    .cookie_options = {'SameSite': 'None', 'Secure': True}
    .default_url = '/lab'
    .disable_check_xsrf = True
    .file_url_prefix = '/lab/tree'
    .ip = '0.0.0.0'
    .keyfile = '/home/ubuntu/privkey.pem'
    .notebook_dir = '/home/ubuntu/jupyter-lab/'
    .port = 8888
    .token = '123456'
    .tornado_settings = {   'cookie_options': {'SameSite': 'None', 'Secure': True},
    'headers': {   'Content-Security-Policy': "frame-ancestors 'self' "
                                              'https://sparkflows_dns:port'}}



.. note:: Make sure to create certificate for running jupyterlab on https

    jupyter-lab --ip=0.0.0.0 --port=8888

It will open the interface in your default web browser.

Fire can be configured to Jupyter Notebook. Below are  the steps involved in it:

Step 1 : Login to Fire web server URL
.............

#. Once login to Fire web server URL, Goto **ADMINISTRATION -->> Configurations** and select **NOTEBOOK**.


    .. figure:: ../../../_assets/operating/jupyter_notebook_1.PNG
       :alt: operating
       :width: 60%

#. Update the below parameters:

    ::

        notebook.enabled : true
        notebook.serverHost : jupyternotebook server url which include token
        notebook.serverToken : Token being used
    
    .. note::  Make sure to change localhost to your domain name or your IP where Fire is running and it should be accessible.   


Step 2 : Open and Access Jupyter Notebook
.............

#. Once the above configuration is saved, refresh the web server URL and you will see **Jupyter Notebook**, Open it.

    .. figure:: ../../../_assets/operating/jupyter_notebook-access.PNG
       :alt: operating
       :width: 60%

#. Access Jupyter Notebook

   Once you click on **Jupyter Notebook**, it will open a new page for Jupyter Notebook and you can run the python code on top of it.

    .. figure:: ../../../_assets/operating/jupyter_notebook_2.PNG
       :alt: operating
       :width: 60%

    .. figure:: ../../../_assets/operating/jupyter_notebook_command.PNG
       :alt: operating
       :width: 60%
