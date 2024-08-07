Second Analytical App Example
=============================

This is a Jupyter Notebook-integrated Analytical App. It enables users to make selections on the Analytical App UI. A section of the Jupyter Notebook is executed based on the selection made using the logic defined in the code and the results are streamed back to the Fire Insights Analytical App UI.

Analytical App Overview
-----------------------

The below Analytical App performs the following tasks:

* Reads jupyter notebook named **ChurnAnalysisAndPrediction.ipynb** which is in the docker image in the home directory set in the docker image. The notebook can reside on any path inside the docker image.

  .. figure:: ../../_assets/jupyter/example-app-2.PNG
     :alt: jupyter
     :width: 60%

* This Analytical App has the following two stages:

  * **Introduction:** This stage describes the App, its business need, and the benefits that can be achieved by using it.
  * **Select Operation:** Users can select the operation they would like to perform. The selected option will be passed to the notebook as a parameter, and based on the desired logic, the corresponding action will be performed.
  
  .. figure:: ../../_assets/jupyter/example-app-2-2.png
     :alt: jupyter
     :width: 60%


Jupyter Notebook
----------------

Below is the Jupyter Notebook that gets invoked by the Analytical App and the results are seen in the Fire Insights Analytical App UI.

Jupyter Notebook **ChurnAnalysisAndPrediction.ipynb** contains the following:

::
  
    import sys
    import pandas as pd
    import numpy as np
    import pickle
    #import seaborn as sns
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots
    import plotly
    from sklearn.model_selection import train_test_split
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
    from sklearn.metrics import auc, recall_score, accuracy_score, precision_score, f1_score, precision_recall_curve
    from sklearn.ensemble import RandomForestClassifier
    from sklearn import tree

    #Initialize and Start Execution
    from fire_notebook.output.workflowcontext import RestWorkflowContext
    import sys
    parameters_list = sys.argv
    restworkflowcontext = RestWorkflowContext(parameters=parameters_list)
    message="20"
    #(id:int, title: str, progress: str):
    #"Profiling" OR "Modeling"
    option = restworkflowcontext.getParmeters(parameter_name="option", default="Profiling")

    restworkflowcontext.outputProgress(9, title="Progress", progress=message)

::
	
	# COMMAND ----------

	# Define custom CSS styles for the table
        
	custom_css = """
	<style>
	.my-table-class {
    	  font-family: Arial, sans-serif;
    	  border-collapse: collapse;
    	  width: 100%;
	}
       .my-table-class th {
    	background-color: #f2f2f2;
    	color: #333333;
    	font-weight: bold;
    	padding: 8px;
    	border: 1px solid #dddddd;
    	text-align: left;
	}
      .my-table-class td {
    	border: 1px solid #dddddd;
    	padding: 8px;
    	text-align: center;
	}
	.my-table-class tbody tr:nth-child(even) {
    	background-color: #f9f9f9;
	}
	.my-table-class tbody tr:hover {
    	background-color: #dddddd;
	}
	.my-table-class caption {
    	caption-side: top;
    	font-weight: bold;
    	margin-bottom: 10px;
	}
	</style>
	"""
	

::

	# Reading the data as pandas dataframe.
	import pandas as pd
	colnames=["state","account_length","area_code","phone_number","intl_plan","voice_mail_plan","number_vmail_messages","total_day_minutes","total_day_calls","total_day_charge","total_eve_minutes","total_eve_calls","total_eve_charge","total_night_minutes","total_night_calls","total_night_charge","total_intl_minutes","total_intl_calls","total_intl_charge","number_customer_service_calls","churn"]
	df = pd.read_csv("churn.all", names=colnames, header=None)

::

	# Determine what to run
	def run_options(option):
		if option == "Profiling":
			profile_data()
			data_preprocessing()
			data_visualization()
		elif option == "Modeling":
			model_training()

	# COMMAND ----------

	# Profiling methods
	def profile_data():
	  modhtml = f"{custom_css}\n{df.describe().to_html(classes='my-table-class')}"
	  return restworkflowcontext.outHTML(9, "Summary Statistics of the Churn Dataset ",  modhtml)

	# COMMAND ----------

	def data_preprocessing():
		# Data Pre-processing
		restworkflowcontext.outHTML(9, "", "Pre-processing Steps")

		modhtml = f"{custom_css}\nSize of the Churn Dataset: {df.shape}"
		restworkflowcontext.outHTML(9, "Size of the Churn Dataset", modhtml)

		columns_df = pd.DataFrame({"List of the Column Names available in the dataset": df.columns})
		modhtml = f"{custom_css}\n{columns_df.to_html(classes='my-table-class', index=False)}"
		restworkflowcontext.outHTML(9, "Columns Used in Churn Dataset", modhtml)

		has_nulls = df.isnull().values.any()
		if has_nulls:
			modhtml = f"{custom_css}\nCheck for Nulls: True"
		else:
			modhtml = f"{custom_css}\nNo null records found in the dataset."

		restworkflowcontext.outHTML(9, "Check for Nulls", modhtml)


	# COMMAND ----------

	def data_visualization():
		# Data Visualization
		restworkflowcontext.outHTML(9, "", "Data Visualization")
		
		message = "30"
		restworkflowcontext.outputProgress(9, title="Progress", progress=message)
		
		# Distribution Chart
		fig = plotly.offline.plot([go.Histogram(x=df['total_day_calls'], nbinsx=5)], output_type='div', include_plotlyjs=False)
		example_plotly = f'{fig}'
		restworkflowcontext.outPlotly(9, title="TotalDayCalls Distribution Chart", text=example_plotly )
		
		message = "40"
		restworkflowcontext.outputProgress(9, title="Progress", progress=message)
		
		def df_to_plotly(df):
			return {'z': df.values.tolist(),
					'x': df.columns.tolist(),
					'y': df.index.tolist()}
		
		dfcorr = df.corr()
		
		fig = plotly.offline.plot([go.Heatmap(z=dfcorr.values, x=dfcorr.columns, y=dfcorr.index)],
								  output_type='div',
								  include_plotlyjs=False)
		example_plotly = f'{fig}'
		restworkflowcontext.outPlotly(9, title="Correlation Heatmap", text=example_plotly)

::

	# Model Training method

	def model_training():
	  features = ["number_vmail_messages","total_day_minutes","total_day_calls","total_day_charge","total_eve_minutes","total_eve_calls","total_eve_charge","total_night_minutes","total_night_calls","total_night_charge","total_intl_minutes","total_intl_calls","total_intl_charge","number_customer_service_calls"]
	  data = df
	  # Churn False. with 1 and True. with 0
	  data = data.replace(to_replace="False.",value="1").replace(to_replace="True.",value="1")
	  split_ratio = 0.8

	  # Features with churn
	  data1 = data[features + ['churn']]
	  data1.fillna(0, inplace=True)
	  y=data1["churn"]
	  X=data1.drop('churn', axis=1)
	  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio,
														 stratify=y, random_state=12345)
	  # Parameters related to RandomForestClassifier
	  depth = 6
	  randstate = 1234
	  rf_clf = RandomForestClassifier(max_depth=depth, random_state=randstate)
	  rf_clf.fit(X=X_train, y=y_train)
	  with open("Churn_model_new.pkl", "wb") as f:
		pickle.dump(rf_clf, f)
	  rf_train_pred_prob = rf_clf.predict_proba(X_train)
	  rf_test_pred_prob = rf_clf.predict_proba(X_test)
	  rf_y_pred_train = rf_clf.predict(X_train)
	  rf_y_pred_test = rf_clf.predict(X_test)
	  trainreport = pd.DataFrame(classification_report(y_train,rf_y_pred_train,digits=2, output_dict=True)).T
	  restworkflowcontext.outHTML(9, title="Training Set Metrics", text=trainreport.to_html())

	  testreport = pd.DataFrame(classification_report(y_test,rf_y_pred_test,digits=2, output_dict=True)).T
	  restworkflowcontext.outHTML(9, title="Testing Set Metrics", text=testreport.to_html())
		 

::

	# COMMAND ----------

	run_options(option)

	# COMMAND ----------

	message="100"
	restworkflowcontext.outputProgress(9, title="Progress", progress=message)

	message = "Job Execution Completed."
	restworkflowcontext.outSuccess(9, title="Success", text=message)

Executing the Application
-------------------------

When you run the Analytical App, it utilizes the Jupyter Notebook connection to submit the job to Kubernetes cluster and streams back the response back from the Jupyter Notebook to the Fire Insights Analytical App UI.

* The **Introduction Stage** is displayed below. Click on the Get Started button to proceed to the next stage.

  .. figure:: ../../_assets/jupyter/example-app-2-3.png
     :alt: jupyter
     :width: 60%


* The **Select-Operation Stage** is displayed below. Users can select from the following options based on the action they need to perform:

  * **Profiling of Transaction Data** to perform data profiling and view summary statistics of the dataset, as well as to check for null values.
  * **Model Training and Prediction** to train a model and perform churn prediction.

  After making the selection, click on the **Run** button to execute the notebook.
  
  .. figure:: ../../_assets/jupyter/example-app-2-4.png
     :alt: jupyter
     :width: 60%

Printing Results
------------------

* Summary Statistics of the dataset:

  .. figure:: ../../_assets/jupyter/example-app-2-5.png
     :alt: jupyter
     :width: 60%
   
* Null Values in the dataset:

  .. figure:: ../../_assets/jupyter/example-app-2-6.png
     :alt: jupyter
     :width: 60%   
   
* Histogram displaying distribution of total_day_calls values:

  .. figure:: ../../_assets/jupyter/example-app-2-7.png
     :alt: jupyter
     :width: 60%   
   
* Correlation matrix between various data columns:

  .. figure:: ../../_assets/jupyter/example-app-2-8.png
     :alt: jupyter
     :width: 60%   
   
* Model Training: Confusion Matrix:

  .. figure:: ../../_assets/jupyter/example-app-2-9.png
     :alt: jupyter
     :width: 60%   
   
* Model Training: Model Accuracy:

  .. figure:: ../../_assets/jupyter/example-app-2-10.png
     :alt: jupyter
     :width: 60%   
   
* Model Prediction: Prediction Results:

  .. figure:: ../../_assets/jupyter/example-app-2-11.png
     :alt: jupyter
     :width: 60%   
