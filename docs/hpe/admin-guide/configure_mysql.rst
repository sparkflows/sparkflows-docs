Configure Access to MySql
=====

This document explains in detail the steps involved in configuring access to MySql on HPE UA.

Make sure that the pods running in HPE Ezmeral Platform can access the MySQL server, as this is the database that will be used to store the metadata of Sparkflows.

Once the access is checked, you need to create a kubernetes secret resource with name as **sparkflows-db-secret** that would contain the base64 encoded values for all the credentials used, as shown below

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
