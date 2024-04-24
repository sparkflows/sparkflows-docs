Example Analytical App-2
==================

This is a Jupyter Notebook integrated Analytical App. It enables the user to make selection on App UI. A section of Jupyter Notebook is executed based on the selection made using the logic defined in the code.

Analytical App Overview
--------

The below Application does the following:

* Reads jupyter notebook **jupyter_lab_3.ipynb**.

  .. figure:: ../../_assets/jupyter/example-app-2-1.png
     :alt: jupyter
     :width: 60%

* This App has below two stages:

  - **Introduction:** This stage describes about the App, business need and benefits that can be achieved by using the App.
  - **Select Operation:** User can select operation that they would like to perform. Selected option would be passed to the notebook as a parameter and based on the logic desired action would be performed. 

  .. figure:: ../../_assets/jupyter/example-app-2-2.png
     :alt: jupyter
     :width: 60%


Jupyter Notebook
------

Below is the Jupyter Notebook which gets invoked by the Analytical App and to output the results back to the Analytical App:

Jupyter Notebook **jupyter_lab_3.ipynb**, contains the below:

::

   print("I am jupyter lab")
   I am jupyter lab

::
  
    import os
    os.getcwd()
    print()
    import sys
    print(sys.argv)
	
	# Pandas and Numpy
	import pandas as pd
	import numpy as np
	import pickle

	# Matplotlib graph
	import seaborn as sns
	import matplotlib.pyplot as plt
	import plotly.graph_objs as go
	# import plotly.graph_objects as go
	from plotly.subplots import make_subplots
	import plotly
	%matplotlib inline


	from sklearn.model_selection import train_test_split
	from sklearn.model_selection import train_test_split
	from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
	from sklearn.metrics import auc, recall_score, accuracy_score, precision_score, f1_score, precision_recall_curve

	from sklearn.ensemble import RandomForestClassifier
	from sklearn import tree

	webserverURL = sys.argv[1]
	jobId = sys.argv[2]
	option = sys.argv[3]

::
  
    webserverURL = "http://localhost:8080/messageFromSparkJob"
    jobId = "123456789"
    from fire_notebook.output.workflowcontext import RestWorkflowContext
    restworkflowcontext = RestWorkflowContext(webserverURL, jobId)

	message="20"
	#(id:int, title: str, progress: str):
	restworkflowcontext.outputProgress(9, title="Progress", progress=message)

::

	# COMMAND ----------

	# Define custom CSS styles for the table
	custom_css = """

	"""

::

	#Reading the data as pandas dataframe.
	import pandas as pd
	colnames=["state","account_length","area_code","phone_number","intl_plan","voice_mail_plan","number_vmail_messages","total_day_minutes","total_day_calls","total_day_charge","total_eve_minutes","total_eve_calls","total_eve_charge","total_night_minutes","total_night_calls","total_night_charge","total_intl_minutes","total_intl_calls","total_intl_charge","number_customer_service_calls","churn"]
	df = pd.read_csv("/tmp/datasets/churn.all", names=colnames, header=None)

::

	#Determine What to run
	def run_options(option):
		if option == "Profiling":
			profile_data()
			data_preprocessing()
			data_visualization()
		elif option == "Modeling":
			model_training()

	# COMMAND ----------

	#Profiling Function
	def profile_data():
	  modhtml = f"{custom_css}\n{df.describe().to_html(classes='my-table-class')}"
	  return restworkflowcontext.outHTML(9, "Summary Statistics of the Churn Dataset ",  modhtml)

	# COMMAND ----------

	def data_preprocessing():
		# Data Pre-Processing
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
		
		#plt.figure(figsize=(12,6))
		#sns.set('notebook')
		#sns.distplot(boston_df.Price, bins=20)
		#plt.show()
		
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

	# Model Training

	def model_training():
	  features = ["number_vmail_messages","total_day_minutes","total_day_calls","total_day_charge","total_eve_minutes","total_eve_calls","total_eve_charge","total_night_minutes","total_night_calls","total_night_charge","total_intl_minutes","total_intl_calls","total_intl_charge","number_customer_service_calls"]
	  data = df
	  # Churn False. with 1 and True. with 0
	  data = data.replace(to_replace="False.",value="1").replace(to_replace="True.",value="1")
	  split_ratio = 0.8
	  # features with churn
	  data1 = data[features + ['churn']]
	  data1.fillna(0, inplace=True)
	  y=data1["churn"]
	  X=data1.drop('churn', axis=1)
	  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=split_ratio,
														 stratify=y, random_state=12345)
	  # some parameters related to RandomForestClassifier
	  depth = 6
	  randstate = 1234
	  rf_clf = RandomForestClassifier(max_depth=depth, random_state=randstate)
	  rf_clf.fit(X=X_train, y=y_train)
	  with open("/dbfs/FileStore/Churn_datasets/RF_Model/Churn_model_new.pkl", "wb") as f:
		pickle.dump(rf_clf, f)
	  rf_train_pred_prob = rf_clf.predict_proba(X_train)
	  # rf_train_pred_prob
	  rf_test_pred_prob = rf_clf.predict_proba(X_test)
	  # rf_test_pred_prob

	  rf_y_pred_train = rf_clf.predict(X_train)
	  rf_y_pred_test = rf_clf.predict(X_test)

	  trainreport = pd.DataFrame(classification_report(y_train,rf_y_pred_train,digits=2, output_dict=True)).T
	  
	  print(trainreport)
	  restworkflowcontext.outHTML(9, title="Training Set Metrics", text=trainreport.to_html())
	  # restworkflowcontext.outStr(3,"Training Set Metrics - "+str(trainreport),"Classification Report")
	  # print("Test Classification Report " )
	  testreport = pd.DataFrame(classification_report(y_test,rf_y_pred_test,digits=2, output_dict=True)).T
	  restworkflowcontext.outHTML(9, title="Testing Set Metrics", text=testreport.to_html())
	  # restworkflowcontext.outStr(3,"Testing Set Metrics - "+str(testreport),"Classification Report")
		 

::

	# COMMAND ----------

	run_options(option)

	# COMMAND ----------

	message="100"
	restworkflowcontext.outputProgress(9, title="Progress", progress=message)

	message = "Job Execution Completed."
	restworkflowcontext.outSuccess(9, title="Success", text=message)

Executing the application
------------------

Once you run the application, it uses **Jupyter Notebook** connection to submit and print the response back from Jupyter Notebook to Sparkflows UI.

* Introduction Stage is displayed as below. Click on **Get Started** button to move to the next stage.

  .. figure:: ../../_assets/jupyter/example-app-2-3.png
     :alt: jupyter
     :width: 60%


* Select-Operation Stage is displayed as below. User can select below options based on the action needs to be performed:

  * **Profiling of Transaction Data** to perform Data Profiling to view Summary Statistics of the dataset, to view null values present in the dataset and so on.
  * **Model Training and Prediction** to train model and perform churn prediction.

  After making the selection click on **Run** button to execute the notebook.

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
