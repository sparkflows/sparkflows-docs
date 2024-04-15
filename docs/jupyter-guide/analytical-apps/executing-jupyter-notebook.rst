Notebook Execution Using Jupyter
================================

Follow the below steps to execute notebook on Kubernetes cluster:

Step 1 : Create Jupyter Notebook Connection
++++++++++++++++

#. Input the required general attributes:
   
   * **Connection Name** - Any string to identify your connection.
   * **Postback URL** - <fireinsight server host>:<port>/messageFromSparkJob
     
     For example - http://192.168.49.1:8080/messageFromSparkJob
   
   * **Title** - Any string name to identify your connection.
   * **Description** (Optonal) - About connection.

     .. figure:: ../../_assets/jupyter/add_jupyter_connection_1.png
        :alt: jupyter-notebook
        :width: 60%


#. Input the kubernetes configuration details:
   
   * **Path** - (Optional) Path of kubernetes configuration. For example - **/home/user1/.kube/kubeconfig**
   * **Namespace** - Namespace of kubernetes where the notebook will get executed. Default value - **default** 
   * **Docker image** - Notebook docker image - Default value - **sparkflows/fire:jupyternotebook.4**
   * **Another available image** - **sparkflows/fire:jupyternotebook.5**

     .. figure:: ../../_assets/jupyter/add_connection_kubernetes.png
        :alt: jupyter-notebook
        :width: 60%

Step 2 : Create Analytical App
++++++++++++++++++++++++++++++

#. Go to **Applications** and click on **Create button**.
#. Input the **name** of application (Alphanumeric).
#. Select **Execution type** - Jupyter Notebook.
#. Input the **Path** of notebook. For example - **jupyter_lab_3.ipynb** or **jupyter_with_additonal_parameters.ipynb**.
#. Select **Jupyter Notebook connection** from drop down.
#. Next, add one **stage** which must have an Execute button with action - execute. Click on **Run**. 

   .. figure:: ../../_assets/jupyter/analytics-app-jupyter-run.png
      :alt: jupyter-notebook
      :width: 70%

`Click here <https://docs.sparkflows.io/en/latest/user-guide/web-app/index.html>`_ to get more details on how to create Analytical Apps.
