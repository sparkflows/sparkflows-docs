Install and Integrate with OpenLineage
=====

This document explains, in detail, the steps involved in installing OpenLineage with the Marquez API using its Helm chart on HPE UA.

Prerequisites
------

.. note:: **Kubernetes Cluster:** Ensure you have access to a running Kubernetes cluster.

Installation Steps
---------------------------------

#. Download and extract the **marquez-0.49.tar.gz** file, which contains the Helm chart of the marquez API server.
#. Modify **values.yaml** to configure the database.

   ::
	
		db:
			host: postgres-marquez-marquez-postgres.sparkflows.svc.cluster.local
			port: "5432"
			name: marquez
			user: marquez
			password: marquez

#. Modify **values.yaml** to configure the virtual service.

   ::
	
		ezua:
		  domainName: "ezua.hpecatalystpoc.com"
		  virtualService:
			endpoint: "marquez.ezua.hpecatalystpoc.com"
			istioGateway: "istio-system/ezaf-gateway"
		  authorizationPolicy:
			namespace: "istio-system"
			providerName: "oauth2-proxy"
			matchLabels:
			  istio: "ingressgateway"

#. Once the modifications are complete, create a **tar.gz** file using the following command.

   ::
	
		tar -czvf marquez-v0.49.0.tar.gz marquez

#. Now, you can use Helm command to install the chart in the user namespace.
 
   ::
	
		helm install marquez-api-v3 chart -n sparkflows-3c0fd950

Configure Sparkflows to connect to the Marquez API
---------------------------------

#. Upload the JAR file **openlineage-spark_2.12-1.18.0.jar**, which is included in the **tar.gz** shared by the Sparkflows team.
#. Navigate to the **Administration** > **Configurations** and enable the Open lineage connection.
#. Navigate to the **Administration** > **Global/Group Connections** and add a new connection of type **Open Lineage**, after selecting the category to **Lineage** and enter the following details as shown in the image below.

   .. figure:: ../../_assets/hpe/Lineage-Edit-Connection.png
      :width: 60%
      :alt: Sparkflows On UA


   **Connection Name:** Enter a unique identifier of the connection. Any alphanumeric value can be used.

   **URL:** Marquez API host with port. This value will come from the EZUA service endpoint, for example:

   ::

		https://marquez.abc.net

   **SparkConf:** 
		
   ::
		
			spark.extraListeners: io.openlineage.spark.agent.OpenLineageSparkListener, spark.openlineage.transport.type:http, spark.openlineage.transport.url: https://marquez.sparkflows.net, spark.openlineage.facets.disabled: [spark.logicalPlan], spark.openlineage.debugFacet: enabled
			
   **Jars:** Enter OpenLineage Jar details. 

   ::

		hdfs:///apps/sparkflows/openlineage-spark_2.12-1.18.0.jar
	
#. **Test** and **save** the connection. Then, edit or create the Livy connection.
#. Go to the Lineage tab in the livy connection and choose the Lineage connection that you just created, as shown in the screenshot below

   .. figure:: ../../_assets/hpe/Lineage-Livy-Integration.png
      :width: 60%
      :alt: Sparkflows On UA

#. Now you should be able to see the list of namespaces by visiting the url: 

   ::

      https://<sparkflows.endpoint.net>/lineage

