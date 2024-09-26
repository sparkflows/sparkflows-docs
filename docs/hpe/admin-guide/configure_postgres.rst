Configure access to Postgres & Hive Metastore
=====

This document explains in detail the steps involved in configuring access to Postgres & Hive Metastore on HPE UA.

Make sure that the pods running in HPE Ezmeral Platform can access the Postgres server, as this is the database that will be used to store the metadata of Sparkflows.

Once the access is checked, you need to create a kubernetes secret resource with name as **sparkflows-db-secret** that would contain the base64 encoded values for all the credentials used.

Following are the list of environment variables that will be mounted from the sparkflows-db-secret which is present in the directory - **kubernetes/config/secrets.yaml**

#. **KEYSTORE_PASSWORD:** The default value is 12345678. If you have created a custom keystore then you can update this password accordingly.

#. **DB_HOST:** This will store the base64 encoded value of Postgres Database that will be used to store the Sparkflows’ metadata.

#. **DB_USERNAME:** This will store the base64 encoded value of Postgres DB username.

#. **DB_PASSWORD:** This will store the base64 encoded value of Postgres DB password.

#. **HIVE_TRUSTSTORE_PASSWORD(Optional):** This will store the base64 encoded trust store password required to connect to Hive metastore

#. **HIVE_USERNAME(Optional):** This will store the base64 encoded hive username

#. **HIVE_PASSWORD(Optional):** This will store the base64 encoded hive password

	::
		
		apiVersion: v1
		kind: Secret
		metadata:
		  name: sparkflows-db-secret
		  namespace: sparkflows
		type: Opaque
		data:
		  KEYSTORE_PASSWORD: <Keystore password(bas64 encoded)>
		  DB_HOST: <Postgres Host(bas64 encoded)>
		  DB_USERNAME: <Postgres DB username(bas64 encoded)>
		  DB_PASSWORD: <Postgres DB password(bas64 encoded)>
		  HIVE_TRUSTSTORE_PASSWORD: <Hive truststore password(bas64 encoded)>
		  HIVE_USERNAME: <Hive username(bas64 encoded)>
		  HIVE_PASSWORD: <Hive password(bas64 encoded)>

Sparkflows needs access to the Hive’s trust store that needs to be mounted on a volume. Connect with the HPE team to create a persistent volume to store the Hive SSL truststore and upload the truststore files to that volume and also create a persistent volume claim, with name as **sparkflows-hive-ssl-pvc** that will be used by Sparkflows Pod to read that volume
