Feature Engineering 
====
Sparkflows provides a set of nodes under the Feature Engineering category to compute various engineered features from transactional or user data. These nodes are designed to enhance datasets for machine learning models by generating insightful features such as grouping, time-series attributes, and moving averages.

GROUP BY Node
----
The GROUP BY node computes feature engineering tasks such as group by, frequency, recency, average days between purchases, total value of purchases, and customer age. These are computed per user using the selected operations.

Node Configuration
++++

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/groupby-configuration.png
    :alt: FE Node
    :width: 70%
  
- **Group By Columns:** Select the columns from the dropdown to group by.
- **Enable Frequency:** Enable frequency count per user ID by setting it to true.
- **Enable Recency:** Enable recency computation (last purchase date) per user ID by setting it to true and select the Date column from the dropdown to compute recency from.
- **Enable Avg Days Between:** Enable computation of average days between purchases by setting it to true and select the Date column from the dropdown to compute average days between.
- **Enable Value of Purchase:** Enable total value of purchase per user by setting it to true.
- **Columns to Sum:** Select the Numeric columns to sum per user from the dropdown.
- **Enable Customer Age:** Enable it by setting to true to compute age of customer from DOB.


Workflow
++++

   .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/groupby-workflow.png
    :alt: FE Node
    :width: 70%
  
- **Input:** Takes DataFrame(s) as input for processing.
- **Processing:** Groups data based on selected columns and computes enabled features.
- **Output:** Returns engineered features as a DataFrame.


Node Output
++++

**Data Summaries:** Engineered features including frequency, recency days, average days between, summed purchase values, and customer age, as shown below.

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/groupby-output.png
    :alt: FE Node
    :width: 70%
  
Time Series Node
----

The Time Series Features node computes various time-series related features from a DataFrame containing transactional data.

Node Configuration
++++

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/time-seires-configuration.png
    :alt: FE Node
    :width: 70%
  
- **User ID Column (mandatory):** Select the column representing the user or entity ID.
- **Date/Timestamp Column (mandatory):** Select the column representing the transaction date or timestamp.
- **Amount Column (optional):** Select the column representing the transaction amount .
- **Item Column (optional):** Select the column representing the item purchased.
- **Category Column (optional):** Select the column representing the transaction category.
- **Enable Days Since Last Transaction:** Set it to true to calculate the time elapsed since the user's last transaction (in days/hours).
- **Enable Days Until Next Transaction:** Set it to true to calculate the time remaining until the user's next transaction (in days/hours).
- **Enable Transaction Hour:** Set it to true to extract the hour from the transaction timestamp.
- **Enable Transaction Day of Week:** Set it to true to extract the day of the week from the transaction timestamp and select the day to be considered as the start of the week.
- **Enable Transaction Day of Month:** Set it to true to extract the day of the month from the transaction timestamp.
- **Enable Week of Year:** Set it to true to extract the week of the year from the transaction timestamp.
- **Enable Is Weekend:** Set it to true to create a binary flag indicating if the transaction occurred on a weekend..
- **Enable Is Month Start:** Set it to true to create a binary flag if the transaction is at the start of the month and select the number of days from the start of the month to consider.
- **Enable Is Month End:** Set it to true to create a binary flag if the transaction is at the end of the month and select the day of the month from which to consider the end.
- **Enable Time Since First Transaction:** Set it to true to calculate the time elapsed since the user's very first transaction (in days/hours).
- **Enable Time of Day Bin:** Set it to true to categorize transactions into 'night', 'morning', 'afternoon', and 'evening'.
- **Enable Season:** Set it to true to assign a season to each transaction based on the month.
- **Enable Average Time Between Transactions:** Set it to true to calculate the average time between a user's transactions (in days/hours).
- **Enable Rolling Transaction Count:** Set it to true to count the number of transactions in a rolling window (with window size in days).
- **Enable Rolling Amount Mean:** Set it to true to compute a rolling average of transaction amounts over a defined window.
- **Enable Days Since Last Same Item:** Set it to true to calculate time since the last purchase of the same item (in days/hours).
- **Enable Days Since Last Same Category:** Set it to true to calculate time since the last purchase in the same category (in days/hours).


Workflow
++++

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/time-series-workflow.png
    :alt: FE Node
    :width: 70%

- **Input:** Takes a DataFrame with user, date, and optionally amount, item, and category columns.
- **Processing:** Computes enabled time-series features and appends them to the original DataFrame.
- **Output:** Returns the original DataFrame with new time-series feature columns appended.


Node Output
++++

**Data Summaries:** Time-series features like days since last transaction, transaction hour, season, etc, as shown below.

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/time-series-output-1.png
    :alt: FE Node
    :width: 70%

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/time-series-output-2.png
    :alt: FE Node
    :width: 70%

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/time-series-output-3.PNG
    :alt: FE Node
    :width: 70%

Moving Average Node
----

The Moving Average Features node computes various global moving average features from a DataFrame containing transactional data.

Node Configuration
++++

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/moving-avg-configuration.png
    :alt: FE Node
    :width: 70%

- **Date/Timestamp Column (mandatory):** Select the column representing the transaction date or timestamp from the dropdown.
- **User ID Column (optional):** Select the column representing the user or entity ID.
- **Amount Column (optional):** Select the column representing the transaction amount.
- **Quantity Column (optional):** Select the column representing the quantity.
- **Enable Global Moving Avg Txn Count Per Day:** Enable global average transaction count per day over the required window by setting it to true.
- **Enable Global Moving Avg Gap Days:** Enable global average gap days between transactions over the required window by setting it to true.
- **Enable Global Hourly Avg Txn Count:** Enable global average transaction count per hour over the required window by setting it to true.
- **Enable Global Daily Avg Amount:** Enable global average amount per day over the required window by setting it to true.
- **Enable Global Moving Avg Amount:** Enable global average transaction amount over the required window by setting it to true.
- **Enable Global Moving Avg Sales Per Day:** Enable global average sales (quantity) per day over the required window by setting it to true.
- **Enable Global Moving Avg Unique Users Per Day:**  Enable global average unique users per day over the required window by setting it to true.



Workflow
++++

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/moving-average-workflow.png
    :alt: FE Node
    :width: 70%

- **Input:** Takes a DataFrame with date, and optionally user, amount, quantity columns.
- **Processing:** Computes enabled global moving average features and appends them to the original DataFrame.
- **Output:** Returns the original DataFrame with new global moving average feature columns appended.

Node Output
++++

**Data Summaries:** Global moving average features like moving average amount, transaction count per day, etc, as shown below.

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/moving-avg-output-1.png
    :alt: FE Node
    :width: 70%

 .. figure:: ../_assets/user-guide/machine-learning/feature-engg-nodes/moving-avg-output-2.png
    :alt: FE Node
    :width: 70%













