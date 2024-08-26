Reading Data From Incorta Table
====

This document explains in detail the steps involved in Reading Data From Incorta Table using **Read Incorta** Node.

Step 1 : Read Data from Incrta Table using Read Incorta node
-------------------------

* Configure Read Incorta Node as below and click on Refresh Schema to read data from table.
* Select a **Connection** value from the dropdown. This connection needs to be setup at Global or at the Project level to read Incorta data.
* Enter a table name in the **DB Table** field in **[Schema Name].[Table Name]** format.
* Click on the **Refresh Schema** button to fetch Schema details from the selected table.

   .. figure:: ../../_assets/incorta/rd-read-incorta-node.png
      :width: 60%
      :alt: Incorta User Guide
	  
Step 2 : Save Parquet Node
----------------

* Data undergoes various transformation after reading data from the Incorta table. 
* Processed data needs to be saved in Parquet format using **Save Parquet** node.
* For better management of data it is advisable to save data at the location **as suggested by the Incorta team**:
	gs://ic-spflow-rxghy-bucket/Tenants/default/data/[USE CASE NAME]
	Example : gs://ic-spflow-rxghy-bucket/Tenants/default/data/Price-Elasticity-B2B-V1/Processed-Data/

   .. figure:: ../../_assets/incorta/rd-save-parquet.png
      :width: 60%
      :alt: Incorta User Guide
	  
Step 3 : Read Parquet Node
----------------

* Saved data in the gcs location can be read using **Read Parquet** node.
* Node can be configured as below.

   .. figure:: ../../_assets/incorta/rd-read-parquet.png
      :width: 60%
      :alt: Incorta User Guide
	  
