Influx DB Configuration
=================================
This document outlines the procedure for configuring the Influx Database connection to integrate InfluxDB with Sparkflows. Once set up, Sparkflows monitoring module will provide insights into model performance and operational metrics.

To configure, follow the steps below:

Step 1 : Creating Influx Database Connection 
-----

#. Login to **Fire Insights**. 
#. Navigate to **Administration -> Global/Group Connections -> Add Connection For All**. 

   An **Add Connection** page will be displayed as shown below.


   .. figure:: ../../../_assets/mlops/Influx_create_connection.png
      :alt: Influx Create Connection
      :width: 60%

#. Now, configure the connection as follows and click on **Save** button. The influx connection will be created in Sparkflows.


  * **Credential Store:** Select 'Do Not Use Credential Store' from the dropdown.
  * **Category:** Select the category as **Storage**.
  * **Connection Type:** Select the connection type as **InfluxDB** from the dropdown.
  * **Authentication Type:** Select the type as **User Credential**.
  * **Connection Name:** Enter the name of the connection as **INFLUX_DB_CONNECTION**.
  * **URL:** Enter the url(e.g., http://20.65.224.29:8086).
  * Enter a valid username and password in the respective fields.
  * **Title:** Enter a relevant title for the connection( e.g., INFLUX_DB_CONNECTION).
  * **Organisation:** Enter **my-org** in this field.
  * **Bucket:** Enter **my-bucket** in this field.
  * **Description:** Enter a relevant description if required (optional).


Step 2 : Testing Influx Database Connection 
-----

After entering the connection details, click the **Test Connection** button to test the connection. If successful, it will display a validation message **Successfully Connected**, as shown below.

   .. figure:: ../../../_assets/mlops/Influx_test_connection.png
       :alt: Influx Create Connection
       :width: 60%

Step 3 : Updating Influx Database Connection 
-----

#. Click the **Edit** icon from the **Actions** menu next to the InfluxDB connection. 

   An **Edit Connection** page will be displayed as shown below. 

   .. figure:: ../../../_assets/mlops/Influx_update_connection.png
      :alt: Influx Create Connection
      :width: 60%

#. Now, modify the required database connection details and click on **Update** button.

Step 4 : Monitoring with Sparkflows
-----
Once the model is deployed, Sparkflows monitoring module provides the detailed information on environment, deployment type, deployment mode, problem type, alerts and all the metrics needed to monitor how model is being used and performing over time from influx DB, as shown below. 

   .. figure:: ../../../_assets/mlops/11_Monitoring_Page.png
        :alt: Continuous ML
        :width: 70%

**Monitoring Metrics**
+++++

- **Predictions over time**-Tracks model predictions over a period. 

  .. figure:: ../../../_assets/mlops/average-prediction.png
     :alt: Predictions over time
     :width: 70%
- **Scoring latency**-Monitors response time for scoring over a period of time.

  .. figure:: ../../../_assets/mlops/latency-over-time.png
     :alt: Scoring latency over a period of time
     :width: 70%
- **Number of rows scored**-Measures data processed over a period of time.

  .. figure:: ../../../_assets/mlops/prediction-row-count.png
     :alt: Number of rows scored over a period of time
     :width: 70%

- **Model drift**-Detects changes in model performance over time.

  .. figure:: ../../../_assets/mlops/drift-over-time.png
     :alt: Model drift over time
     :width: 70%


