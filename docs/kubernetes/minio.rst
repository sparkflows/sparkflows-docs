Install Minio
=============

Below are the steps for installing Minio on the Kubernetes cluster. Perform it on any machine from which the Kubernetes cluster is accessible.

* Assuming kubernetes cluster is up and running and the kubectl is installed, we now need to install kubectl plugin for MinIO that will initialize the MinIO cluster::
   
   sudo yum install -y wget
   wget https://github.com/minio/operator/releases/download/v4.2.2/kubectl-minio_4.2.2_linux_amd64 -O kubectl-minio
   chmod +x kubectl-minio
   sudo mv kubectl-minio /usr/local/bin/

* Run the following command to verify installation of the plugin::
   
   kubectl minio version
   
* Run the following command to initialize the Operator::
  
   kubectl minio init
   
* Run the following command to verify the status of the Operator::

   kubectl get pods -n minio-operator
   
  The output resemebles the following::
 
   NAME                              READY   STATUS    RESTARTS   AGE
   console-7c855c9789-9dtrb          1/1     Running   0          5d3h
   minio-operator-66849f98b7-fhswb   1/1     Running   0          5d3h

* Run the following command to create a local proxy to the MinIO Operator Console::

   kubectl minio proxy -n minio-operator

  The output should resemeble the following::

   Starting port forward of the Console UI.

   To connect open a browser and go to http://localhost:9090

   Current JWT to login: eyJhbGciOiJSUzI1N....
  
* Open your browser to the provided address and use the **JWT token** to log in to the Operator Console.

  .. figure:: ../_assets/kubernetes/minio-login.png
     :alt: MinIO Login
     :width: 60%

* Once you've logged in, click on **Create Tenant** to open the tenant creation workflow.

  .. figure:: ../_assets/kubernetes/create-tenant.png
     :alt: MinIO Create Tenant
     :width: 60%
   

   
* The Operator Console Create New Tenant walkthrough builds out a MinIO Tenant. The following list describes the basic configuration sections.

- **Name** - Specify the *Name*, *Namespace*, and *Storage Class* for the new Tenant. 
  
  The *Storage Class* must correspond to a [Storage Class](#default-storage-class) that corresponds to [Local Persistent Volumes](#local-persistent-volumes)   that can support the MinIO Tenant.
  
  The *Namespace* must correspond to an existing [Namespace](#minio-tenant-namespace) that does *not* contain any other MinIO Tenant.
  
  Enable *Advanced Mode* to access additional advanced configuration options. 
 
  .. figure:: ../_assets/kubernetes/configure-tenant.png
     :alt: MinIO Configure Tenant
     :width: 60% 

- **Tenant Size** - Specify the *Number of Servers*, *Number of Drives per Server*, and *Total Size* of the Tenant.

  The *Resource Allocation* section summarizes the Tenant configuration based on the inputs above.
   
  Additional configuration inputs may be visible if *Advanced Mode* was enabled in the previous step.
 
  .. figure:: ../_assets/kubernetes/tenant-size.png
     :alt: MinIO Configure Tenant size
     :width: 60%
   
- **Preview Configuration** - summarizes the details of the new Tenant.
  
  .. figure:: ../_assets/kubernetes/review-tenant.png
     :alt: MinIO Review Tenant config
     :width: 60%
   
* After configuring the Tenant to your requirements, click **Create** to create the new tenant.

  The Operator Console displays credentials for connecting to the MinIO Tenant. You must download and secure these credentials at this stage. 
   
  You cannot trivially retrieve these credentials later.

  You can monitor Tenant creation from the Operator Console.

* Once the tenant is up and running, you can monitor the same from the operator console.

  .. figure:: ../_assets/kubernetes/monitor-tenant.png
     :alt: MinIO Monitor tenant
     :width: 60%

Interacting with the tenant
------------------------------

After the creation of tenant, using the operator console, its time to create buckets using the MinIO CLI aka **mc**.

* Install the MinIO CLI::
   
   curl https://dl.min.io/client/mc/release/linux-amd64/mc \
    --create-dirs \
    -o $HOME/minio-binaries/mc
    chmod +x $HOME/minio-binaries/mc
    export PATH=$PATH:$HOME/minio-binaries/
    
* Use the downloaded credentials to connect with the newly created tenant from another application or pod in the cluster::
    
    # Add alias
    mc alias set minio https://minio.demo.svc.cluster.local <access_key> <access_secret_key>
    
    # Create a bucket for Spark logs
    mc mb minio/spark/logs
    
* The above created bucket will be used for storing the spark logs.
 
 
 
  

  

