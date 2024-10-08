Install/Integrate with OpenLineage
=====

This document explains in detail the steps involved in installing OpenLineage with the Marquez API using its Helm chart on HPE UA.

Pre-requisites
------

.. note:: **Kubernetes Cluster:** Ensure you have access to a running Kubernetes cluster.

Installation Steps
---------------------------------

#. Download and extract the **marquez-0.49.tar.gz** file that contains the helm char of the marquez api server.
#. Modify the **values.yaml** to configure the database configuration.

	::
	
		db:
			host: postgres-marquez-marquez-postgres.sparkflows.svc.cluster.local
			port: "5432"
			name: marquez
			user: marquez
			password: marquez

#. Modify the **values.yaml** to configure the virtual service

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

#. Once the modifications are complete, tar.gz the file using the below command.

	::
	
		tar -czvf marquez-v0.49.0.tar.gz marquez

#. Now you can use helm command to install the chart in the user namespace
 
	::
	
		helm install marquez-api-v3 chart -n sparkflows-3c0fd950

Configure Sparkflows to connect with Marqeuz API
---------------------------------

#. Upload the jar **openlineage-spark_2.12-1.13.1.jar**, that exists in tar.gz shared by Sparkflows team.
#. Navigate to the **Administration** > **Configuration** and add enable the Open lineage connection
#. Navigate to the **Administration** > **Global/Group connection** and add a new connection type **Open Lineage**, after selecting the category to **Lineage** and enter the following details as shown in the screenshot

   .. figure:: ../../_assets/hpe/Lineage-Edit-Connection.png
      :width: 60%
      :alt: Sparkflows On UA


	**Connection Name:** <Any alpha numeric value>
	**URL:** Marquez API host with port. This value will come from the ezua service endpoint that would be something like this, https://marquez.abc.net
	**SparkConf:** 
		
		::
		
			spark.extraListeners: io.openlineage.spark.agent.OpenLineageSparkListener, spark.openlineage.transport.type:http, spark.openlineage.transport.url: <https://marqeuz.abc.net - Change this as per your configured endpoint>, spark.openlineage.facets.disabled: [spark.logicalPlan], spark.openlineage.debugFacet: enabled
			
	**Jars:** hdfs:///apps/sparkflows/openlineage-spark_2.12-1.13.1.jar
	
#. Test and Save the connection, and now edit/create the Livy connection
#. Go to the Lineage tab in the livy connection and choose the Lineage connection that you just created, above as shown in the screenshot below

   .. figure:: ../../_assets/hpe/Lineage-Livy-Integration.png
      :width: 60%
      :alt: Sparkflows On UA

#. Now you should be able to see the list of namespaces by visiting the url: 

    ::

      https://<sparkflows.endpoint.net/lineage

