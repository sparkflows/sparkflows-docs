Configure Access to MySql
=====
This document explains in detail the steps involved in configuring access to MySql on HPE UA.

Step 1 : Verify MySQL Access
------------------------------------
Ensure that the pods running in the HPE Ezmeral Platform can access the MySQL server. MySQL will serve as the database to store Sparkflows metadata. Make sure there is connectivity between the platform and the MySQL server.


Step 2 : Create a Kubernetes Secret for Database Credentials
------------------------------------------------------------
Next, you need to create a Kubernetes secret named as **sparkflows-db-secret**. This secret will store the base64 encoded credentials required for accessing the MySQL database.

Use the following template to define the Kubernetes secret:


	::

		apiVersion: v1
		kind: Secret
		metadata:
		  name: sparkflows-db-secret
		  namespace: sparkflows
		type: Opaque
		data:
		  KEYSTORE_PASSWORD: <Keystore password(bas64 encoded)>
		  DB_HOST: <MySQL Host(bas64 encoded)>
		  DB_USERNAME: <MySQL DB username(bas64 encoded)>
		  DB_PASSWORD: <MySQL DB password(bas64 encoded)>
		  HIVE_TRUSTSTORE_PASSWORD: <Hive truststore password(bas64 encoded)>
		  HIVE_USERNAME: <Hive username(bas64 encoded)>
		  HIVE_PASSWORD: <Hive password(bas64 encoded)>

Ensure that all sensitive information, including database credentials, is encoded using base64.
