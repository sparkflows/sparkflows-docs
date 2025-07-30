Installing InfluxDB on Kubernetes (K3s)
====

This document outlines the steps to install InfluxDB on a Kubernetes cluster powered by K3s.

Prerequisites
----
Before you begin, ensure you have the following:

* A running K3s cluster.
* kubectl configured to connect to your K3s cluster.
* Helm installed on your local machine. If you haven’t installed helm, then run the below command to install Helm:

  ::
    
     curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

Installation Steps
----

**Step 1: Add the InfluxData Helm Repository**
+++++++++++++++++++++++++++++++++++++++++++++++++++

1. First, you need to add the InfluxData Helm repository to your Helm configuration. This will allow you to access the official InfluxDB Helm charts.

   ::

      helm repo add influxdata https://helm.influxdata.com/
      helm repo update

**Step 2: Create a Namespace for InfluxDB**
+++++++++++++++++++++++++++++++++++++++++++++
1. It's good practice to install applications in their own dedicated namespaces. Create a namespace for InfluxDB:

   ::

      kubectl create namespace influxdb

**Step 3: Install InfluxDB using Helm**
+++++++++++++++++++++++++++++++++++++++++++++
1. Now you can install InfluxDB using its Helm chart. You can customize the installation by providing a **values.yaml** file or by setting individual parameters.

   **Basic Installation**
  
   For a basic installation, you can run:

   ::

      helm install influxdb influxdata/influxdb2 \
     --namespace influxdb \
     --set persistence.enabled=true \
     --set persistence.size=20Gi

   **Customized Installation (Recommended)**
  
   For more control over the installation, it's recommended to create a **values.yaml** file with your desired configurations. Here's an example **values.yaml** for InfluxDB:

   ::

        # values.yaml for InfluxDB
        persistence:
           enabled: true
           size: 10Gi
           storageClassName: local-path # Use the default storage class for K3s

        influxdb:
          admin:
            enabled: true
            user: admin
            password: changeme # IMPORTANT: Change this to a strong password!


   Save this content as **influxdb-values.yaml** and then install InfluxDB:

   ::

      helm install influxdb influxdata/influxdb -f influxdb-values.yaml -n influxdb

**Step 4: Verify the Installation**
+++++++++++++++++++++++++++++++++++++++

1. After the installation, you can check the **status of the InfluxDB pods** to ensure they are running correctly:

   ::

      kubectl get pods -n influxdb

2. You should see output similar to the below, indicating the InfluxDB pod is running:

   ::

      NAME                             READY   STATUS    RESTARTS   AGE
      influxdb-xxxxxxxxxx-xxxxx        1/1     Running   0          XmXs


**Step 5: Extract the Influx DB password**
+++++++++++++++++++++++++++++++++++++++++++++

1. Find the **secret name** using the below command:

   ::

      kubectl get secrets -n influxdb
      NAME                             TYPE                 DATA   AGE
      influxdb-influxdb2-auth          Opaque               2      2m5s
      sh.helm.release.v1.influxdb.v1   helm.sh/release.v1   1      2m5s


2. Now extract the **admin password**, using the below command:

   :: 

      kubectl get secret influxdb-influxdb2-auth -o jsonpath="{.data.admin-password}" -n influxdb | base64 --decode

      *************sdfWA04A*****

**Step 6: Access InfluxDB UI (Port Forwarding)**
++++++++++++++++++++++++++++++++++++++++++++++

1. To access the InfluxDB web UI, you can use port forwarding to expose the service to your local machine.

   As a first step, get the service name:

   ::

      kubectl get svc -n influxdb

      NAME                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
      influxdb-influxdb2   ClusterIP   10.43.216.235   <none>        80/TCP    59m


2. Using the above service name, **influxdb-influxdb2** and the port number **80**, port forward the requests:

   ::

      kubectl port-forward --address 0.0.0.0 svc/influxdb-influxdb2 80:8086 -n influxdb

3. Now you can open your web browser and navigate to http://<vm-host>:8086 to access the InfluxDB UI. Use the **admin credentials** you configured during the installation (e.g., **admin** and **password** extracted in the Step 5).

**Step 7: Clean Up (Optional)**
+++++++++++++++++++++++++++++++++++

1. If you need to uninstall InfluxDB, you can do so using Helm:

   ::

      helm uninstall influxdb -n influxdb
      kubectl delete namespace influxdb










































