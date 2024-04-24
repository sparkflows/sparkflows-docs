Creating Analytical App
==================

Below are the steps to create an Analytical App that integrates with Jupyter Notebooks.

Step 1: Login to Fire Insights
-------------------------------

#. Open the Fire Insights Home Page.
#. Enter your credentials and click **Sign In**.

Step 2: Create the Application
---------------------------

#. Go to **Applications** and click on the **Create button**.
#. Input the **name** of application (Alphanumeric).
#. Select **Execution type** as Jupyter Notebook.
#. Input the **Path** of the notebook. For example - **jupyter_lab_3.ipynb** or **jupyter_with_additonal_parameters.ipynb**.
#. Select the **Jupyter Notebook connection** from the drop down.
#. Next, add one stage which must have an **Execute button** with the action set to **execute**. Click on **Run**.


   .. figure:: ../../_assets/jupyter/analytics-app-jupyter-run.png
      :alt: jupyter-notebook
      :width: 70%

   `Click here <https://docs.sparkflows.io/en/latest/user-guide/web-app/index.html>`_ to get more details on how to create Analytical Apps.

#. Now, you can run the application. It will submit the job, and you will see the response back in the Fire Insights UI.
