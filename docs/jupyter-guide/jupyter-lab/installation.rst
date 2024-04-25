Installing JupyterLab
======

JupyterLab can be installed on the machine running Fire Insights, which integrates with Jupyter.

To install JupyterLab for Python in the Ubuntu environment, you need to have Python and pip available.

Use the command below to install JupyterLab:

Use below command to install Jupyter lab: ::

    pip install --upgrade pip
    pip install jupyterlab
    jupyter lab --generate-config

   The above command will generate jupyter_lab_config.py in ~/.jupyter directory

Change to the Jupyter directory using the command: cd ~/.jupyter


Customize the jupyter_lab_config.py file of JupyterLab and change the configurations using the below::

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



.. note:: Make sure to have an SSL certificate for running JupyterLab on HTTPS.

Start Jupyter server using the command given below::

   jupyter-lab --ip=0.0.0.0 --port=8888

Now, try accessing JupyterLab in your browser using the public server URL along with the port number.

