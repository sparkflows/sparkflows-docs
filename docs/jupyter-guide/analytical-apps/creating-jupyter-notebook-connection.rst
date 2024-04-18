Creating Jupyter Notebook Connection
================================

This document outlines steps to create Jupyter Notebook Connection and configure Kubernetes cluster.

Creating Jupyter Notebook connection
++++++++++++++

Sparkflows enables you to create **Jupyter Notebook Connection** and use it to submit **Application**. Connections can be at various levels:

  * **Global**  : Everyone has access to these connections.
  * **Group**   : Users belonging to the group have access to these connections.
 
Below are the steps to create Jupyter Notebook Connection:

Step 1 : Enable Jupyter Notebook in Sparkflows
--------------------

#. **Login** to Sparkflows.
#. Navigate to **Administration -> Configurations -> Connection**. 
#. **Enable** the Jupyter Notebook connection by setting the below parameter:

   ::

       connection.jupyterNotebook.enabled	 : true

   .. figure:: ../../_assets/jupyter/jupyter_enable.PNG
      :alt: synapse
      :width: 60%



Step 2: Input the Required General Attributes
------------------------------------
Input the following details:   
  
   * **Connection Name** - Any string to identify your connection.
   * **Postback URL** - <fireinsight server host>:<port>/messageFromSparkJob
     
     For example - http://192.168.49.1:8080/messageFromSparkJob
   
   * **Title** - Any string name to identify your connection.
   * **Description** (Optonal) - About connection.

     .. figure:: ../../_assets/jupyter/add_jupyter_connection_1.png
        :alt: jupyter-notebook
        :width: 60%

.. Note:: Make Sure that ``Postback URL`` is accessible from Kubernetes Cluster to get response back to Sparkflows UI.

Step 2 : Input the Kubernetes Configuration Details
------------------------------------------------
Input the configuration details as below:
   
   * **Path** - (Optional) Path of kubernetes configuration. For example - **/home/user1/.kube/kubeconfig**
   * **Namespace** - Namespace of kubernetes where the notebook will get executed. Default value - **default** 
   * **Docker image** - Notebook docker image - Default value - **sparkflows/fire:jupyternotebook.4**
   * **Another available image** - **sparkflows/fire:jupyternotebook.5**

     .. figure:: ../../_assets/jupyter/add_connection_kubernetes.png
        :alt: jupyter-notebook
        :width: 60%


