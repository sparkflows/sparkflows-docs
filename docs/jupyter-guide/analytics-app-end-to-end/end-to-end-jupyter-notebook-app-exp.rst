End-To-End Jupyter Notebook Analytical App Example
==================

Below are the steps to create Analytical App which integrate with Jupyter Notebooks:

Step 1: Login to Fire Insights
-------------------------------

#. Open Fire Insights Home Page.
#. Enter your credentials and click **sign in**. 

Step 2 : Enable Jupyter Notebook in Sparkflows
--------------------

#. **Login** to Sparkflows.
#. Navigate to **Administration -> Configurations -> Connection**. 
#. **Enable** the Jupyter Notebook connection

Step 3 : Create a Jupyter Notebook
--------------------

#. Create a Jupyter Notebook having business logic execution steps.

Step 4: Create the Application
---------------------------

#. Go to **Applications** and click on **Create button**.
#. Input the **name** of application (Alphanumeric).
#. Select **Execution type** - Jupyter Notebook.
#. Input the **Path** of notebook. For example - **jupyter_lab_3.ipynb** or **jupyter_with_additonal_parameters.ipynb**.
#. Select **Jupyter Notebook connection** from drop down.
#. Next, add one **stage** which must have an Execute button with action - execute. Click on **Run**. 

   .. figure:: ../../_assets/jupyter/analytics-app-jupyter-run.png
      :alt: jupyter-notebook
      :width: 70%
