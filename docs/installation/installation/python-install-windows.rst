Python Installation on Windows
++++++++++++++++++++++++++++++++

Python is only needed if you need to use Python and the PySpark engine in Fire Insights. Python modules in Fire Insights use Python 3.6+.

Below are steps for installing Anaconda.

  * Download Anaconda from the below Link
     * https://www.anaconda.com/products/individual
     * https://www.anaconda.com/products/individual#Downloads
 

Once the download completes, run the .exe installer

Click Next to confirm the installation
---------------------------------------

.. figure:: ../../_assets/installation/anaconda.PNG
   :alt: Installations
   :width: 45%


Agree to the License
----------------------

.. figure:: ../../_assets/installation/anaconda_agreement.PNG
   :alt: Installations
   :width: 45%

Advanced Installation Options screen
--------------------------------

It is recommended to not check "Add Anaconda to my PATH environment variable"

.. figure:: ../../_assets/installation/anaconda_path.PNG
   :alt: Installations
   :width: 45%


Open the Anaconda Prompt from the Windows start menu
----------------------------------------------------

At the Anaconda prompt, check the ``conda --version``

.. figure:: ../../_assets/installation/conda_version.PNG
   :alt: Installations
   :width: 45%
   
Reference Link
------------

* https://problemsolvingwithpython.com/01-Orientation/01.03-Installing-Anaconda-on-Windows/


Create virtual environment using conda
--------------------------------------

Run below command to Create virtual environment using conda.

::

    conda create --name venv python=3.7

.. figure:: ../../_assets/installation/virtual_env.PNG
   :alt: Installations
   :width: 45%

Activate Virtual environment and Check list of python package
---------------------------------------------------------------

Run Below command to activate and check list of python package available by default.

::

    conda activate venv
    python --version
    pip list

.. figure:: ../../_assets/installation/activate_conda_env.PNG
   :alt: Installations
   :width: 45%

Install Other Dependent Packages
----------------------

Install the other required packages:

::

    pip install -r requirements.txt
   
``requirements.txt`` file is available in the installation directory of Fire Insights : fire-x.y.x/dist/fire/requirements.txt

.. figure:: ../../_assets/installation/req_text.PNG
   :alt: Installations
   :width: 45%


Install dependency for fbprophet package (Windows 10)
----------------------------------------- 

Install pystan:

::

    conda install pystan -c conda-forge

.. figure:: ../../_assets/installation/conda-pystan.PNG
   :alt: Installations
   :width: 45%

Install fbprophet:

::

    conda install -c conda-forge fbprophet

.. figure:: ../../_assets/installation/fbprophet_conda.PNG
   :alt: Installations
   :width: 45%

Check the version of fbprophet Installed:

::

    pip list

.. figure:: ../../_assets/installation/piplist_conda.PNG
   :alt: Installations
   :width: 45%

Once the above steps have completed successfully, run the below command to ensure everything was setup correctly.

::

    python ./dist/__main__.py

.. figure:: ../../_assets/installation/pyspark_server.PNG
   :alt: Installations
   :width: 45%

Enable PySpark Engine in Fire Insights
--------------------------------------

Login to Fire Insights application and go to configurations and set ``app.enablePySparkEngine`` to ``true`` and save the changes. Now you can start using PySpark engine in Fire Insights. 

.. figure:: ../../_assets/installation/pyspark_configurations.PNG
   :alt: Installations
   :width: 45%

Removing Conda virtual Environment
----------------------------------

::

    conda deactivate
    conda env remove --name name of virtual environment
    Delete those package from exact location

