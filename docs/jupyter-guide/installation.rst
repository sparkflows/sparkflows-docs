Installing JupyterLab
======

JupyterLab can be installed on the machine running Fire Insights. Fire Insights integrates with Jupyter.

To install JupyterLab for Python on Ubuntu environment, you need to have python and pip available.

To install JupyterLab for Python in Ubuntu environment, you need to have python and pip available.

Use below command to install jupyter lab: ::

    pip install --upgrade pip
    pip install jupyterlab
    jupyter lab --generate-config

   The above command will generate jupyter_lab_config.py in ~/.jupyter directory

Change to directory jupyter using command: cd ~/.jupyter

Customize the jupyter_lab_config.py file of jupyterlab and change the configurations below::

    #NotebookApp
    c.NotebookApp.open_browser = False
    #ServerApp
    c.NotebookApp.allow_origin = '*'
    c.ServerApp.certfile = '/home/ubuntu/fullchain.pem' # ssl certificate
    c.ServerApp.config_file = '~/.jupyter/jupyter_lab_config.py' #config file path
    c.ServerApp.cookie_options = {'SameSite': 'None', 'Secure': True}
    c.LabApp.default_url = '/lab'
    c.ServerApp.disable_check_xsrf=True
    c.ServerApp.file_url_prefix = '/lab/tree'
    c.NotebookApp.ip = '0.0.0.0'
    c.ServerApp.keyfile = '/home/ubuntu/privkey.pem'
    c.ServerApp.notebook_dir = '/home/ubuntu/jupyter-lab/' #Replace notebook dir with your own directory
    c.NotebookApp.port = 8888
    c.ServerApp.token = '123456' # Replace token with your own token
    c.ServerApp.tornado_settings = { 'headers': { 'Content-Security-Policy': "frame-ancestors 'self' https://sparkflows_dns:port"},"cookie_options": {'SameSite': 'None', 'Secure': True}}



.. note:: Make sure to have a SSL certificate for running jupyterlab on https.

Start jupyter server using below command::

   jupyter-lab --ip=0.0.0.0 --port=8888

 Now try to access jupyter lab on browser using public server url along with port.

