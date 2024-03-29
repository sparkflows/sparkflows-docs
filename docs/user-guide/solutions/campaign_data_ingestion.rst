Data Ingestion
---------------
Sparkflows allows the User to ingest the data from many different data sources using heterogeneous data formats.

.. figure:: ../../_assets/tutorials/solutions/campaign_analytics/campaign_analytics_data_ingestion_v1.png
   :alt: Data Profiling
   :width: 75%

Datasets for Current Solution are stored in various CSV files. 

- The Transactions dataset contains product purchase details of various households. 
- The Households dataset contains customer demographic info.
- The Campaigns dataset contains references to both household and coupon data. 
- The Coupon dataset contains references to the products.
- The Coupon_Redemptions dataset contains info on which household availed of what type of coupons for which campaigns.
- The Campaigns_Households dataset joins the data between households and campaigns.
- The Solution also uses product reviews text data for analyzing customer sentiments.

.. figure:: ../../_assets/tutorials/solutions/campaign_analytics/campaign_analytics_dataset_v1.png
   :alt: Data Profiling
   :width: 75%
