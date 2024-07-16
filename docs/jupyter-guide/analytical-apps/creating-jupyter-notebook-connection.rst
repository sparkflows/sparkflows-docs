Creating Jupyter Notebook Connection
================================

This document outlines the steps to create a Jupyter Notebook Connection and configure a Kubernetes cluster.


Creating Jupyter Notebook connection
++++++++++++++

Fire enables you to create a **Jupyter Notebook Connection** and use it to submit **applications**. Connections can be established at various levels:

* **Global**  : Everyone has access to these connections.
* **Group**   : Users belonging to the group have access to these connections.
* **Project** : Users having access to the project have access to these connections.
 
Below are the steps to create a Jupyter Notebook Connection:

Step 1 : Enable Jupyter Notebook in Fire Insights
--------------------

#. **Login** to Fire Insights.
#. Navigate to **Administration -> Configurations -> Connection**. 
#. **Enable** the Jupyter Notebook connection by setting the below parameter:

   ::

       connection.jupyterNotebook.enabled	 : true

   .. figure:: ../../_assets/jupyter/jupyter_enable.PNG
      :alt: jupyter
      :width: 60%

Step 2 : Add and Save the Connection
-------------------

Once you save the above configurations:

#. Navigate to **Administration -> Global Connections -> Add Connections** as shown below:

   .. figure:: ../../_assets/aws/livy/administration.png
     :alt: jupyter
     :width: 60%

#. Click on **Add Connection For Group**.

   .. figure:: ../../_assets/azure/synapse_addconnection.png
      :alt: jupyter
      :width: 60%

#. On the pop-up window, select connection as **Compute Connection** and enter other parameters as shown below:

   .. figure:: ../../_assets/jupyter/jupyter_notebook_connection.PNG
      :alt: jupyter
      :width: 60%

#. Once you have selected  the connection type & groups, add the **additional connection parameters** needed as per your environment.

   Input the following details in **GENERAL tab**:

    
   * **Connection Name** - Any string to identify your connection.
   * **Postback URL** - <fireinsight server host>:<port>/messageFromSparkJob
     
   For example - http://192.168.49.1:8080/messageFromSparkJob
   
   * **Title** - Any string name to identify your connection.
   * **Description** (Optonal) - About connection.

   .. figure:: ../../_assets/jupyter/add_jupyter_connection_1.png
      :alt: jupyter-notebook
      :width: 60%

   .. Note:: Make Sure that the **Postback URL** is accessible from Kubernetes Cluster to get response back to Fire Insights UI.

   Input the following details in **KUBERNETES tab**:

   * **Path** - (Optional) Path of kubernetes configuration. For example - **/home/user1/.kube/kubeconfig**
   * **Namespace** - Namespace of kubernetes where the notebook will get executed. Default value - **default** 
   * **Docker image** - Notebook docker image - Default value - **sparkflows/fire:jupyternotebook.33**
   * **You can use your own image as well** if you created notebook and built and pushed the docker image.

   .. figure:: ../../_assets/jupyter/add_connection_kubernetes.png
       :alt: jupyter-notebook
       :width: 60%

   .. Note:: Make sure that the **Path** updated should be accessible from Fire Insights VM.

#. Once you have updated the above parameters, click on **Save** to save the connection.
