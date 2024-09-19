Pre-deployment checklist for Sparkflows on UA 1.5
==========

This document lists pre-deployment checklist for the installation of Sparkflows on UA 1.5.


Summary
----------------------------------------


.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Access Required
     - Reason
   * - Jump server
     - To Access HPE resources.
   * - Admin access to kubectl
     - To get information on Nodes etc and run different kubectl command.
   * - Access to create namespace and has the default-editor service account
     - admin is able to create or use a custom namespace which has the default-editor service account.
   * - Livy
     - Test if Livy credentials are correct and connection endpoint are accessible.
   * - Data Fabric
     - To upload the Sparkflows Jar, Cloud.py and upload sample data to read and write and is accessible to livy.
   * - Data Fabric
     - To upload the Sparkflows Jar, Cloud.py and upload sample data to read and write and is accessible to livy.
   * - Keycloak client credentials
     - Client ID and Client credential details.
   * - Sparkflows Domain
     - To be configured in Keycloak.
   * - Hive Access
     - If only Hive Database is used. To be configured in Sparkflows.
   * - Livy - PVC
     - Required for storage of logs.
   * - Hive SSL Secret
     - Kubernetes secret used for connecting to hive.
   * - Keycloak SSL cert secret
     - Kubernetes secret for configuring SSL with Keycloak.
   * - Database secret
     - Kubernetes secret for storing the metadata. It would be needed for either MySql or Postgres based on the db selected.
 
Remote Desktop / Jump server access
----------------------------------------

In order to deploy and debug the failures, we need access to the Jump server through which we can execute the kubectl commands and other diagnostic scripts.

Edge Node access on both Data Fabrics and UA would be needed via Remote Desktop Access.

Kubernetes cluster access
----------------------------------------

kubectl commands will be executed in order to debug the pods and containers running in the Kubernetes cluster of UA.

Ensure **metrics-server** is installed(By default it is expected to be installed in UA 1.5):

Make sure you have **metrics-server** installed in your cluster. If not, you’ll need to install it first. 

Below are few of the commands that can be used for debuging purposes:

* Get the list of nodes:

To list all the nodes in your cluster, use::

	kubectl get nodes
	
* Check CPU and memory usage:

To check the current CPU and memory usage of each node, use::

	kubectl top nodes
	
This command will show the CPU and memory usage metrics for each node in the cluster.

* Using kubectl create namespace Command:

You can create a new namespace by running the following command::

	kubectl create namespace <namespace-name>
	
Livy on YARN Connectivity (Recommended)
----------------------------------------

Given the username and password, calculate the base64 encoding of username:password

::

	echo -n 'username:password' | base64

Now run the curl command for jumpstation for testing the Livy connectivity

::

	curl --location --request GET 'https://{LIVY_HOSTNAME}/batches' --header 'Authorization: Basic c3Bhcmtmb233OkFkbWluMTIzNA=='--header 'Content-Type: application/json'

Livy on EzUA Connectivity 
----------------------------------------

When Livy is running in UA, then following are steps to authenticate with Keycloak, generate token and use that token to access Livy service

* Authenticate with Username/Password and obtain the auth token

::
 
	$ USERNAME=sparkflows
	$ PASSWORD=Passw0rd
	$ KC_ADDR=keycloak.sparkflows.net
	response_json=$(curl --data
	"username=$USERNAME&password=$PASSWORD&grant_type=password&client_id=ua-grant" "https://$KC_ADDR/realms/UA/protocol/openid-connect/token")

* Extract the access token from the response

::

	ACCESS_TOKEN=$(echo "$response_json" | jq -r '.access_token')

* Use the access token to authenticate with Livy

::

	curl https://spark-livy.sparkflows.net/sessions -k --header "Authorization: Bearer $ACCESS_TOKEN" --header 'Content-Type: application/json'

Connectivity from Livy to Sparkflows
----------------------------------------

Once authentication is successful, we need to make sure if Livy is able to connect with Sparkflows server. This is required for sending post back messages to sparkflows on capture Spark logs.

* Import the Sparkflows certificate into Datafabric’s Java keystore

::

	keytool -import -noprompt -trustcacerts -alias sparkflows-cert -file sparkflows-sslcert.crt -keystore ${JAVA_HOME}/lib/security/cacerts -storepass changeit

* Datafabric would be using another keystore for running the services. We need to merge the Java Keystore with Services keystore, which is stored in /opt/mapr/conf/ssl_keystore. For this to work, make sure you have the keystore password for the destination keystore too. Use the below command to merge the Java keystore to mapr keystore.

::

	$ cd /opt/mapr/server/manageSSLKeys.sh
	$ ./manageSSLKeys.sh merge ${JAVA_HOME}/lib/security/cacerts /opt/mapr/conf/ssl_truststore <src-truststore-password> <destination-truststore-password>

Ports to be opened
----------------------------------------

Sparkflows will be running as a service in HPE EzUA, that will be connecting to Livy endpoint and Data Fabric’s S3 endpoint. These are the two services running in EDF that will be accessed from Sparkflows. The outbound rule should be configured to allow traffic from Sparkflows to Livy and Datafabric (S3 endpoint)

Communication ports between UA and Data Fabrics would be automatically assigned by UA

Docker images 
----------------------------------------

The docker images will be stored here https://hub.docker.com/r/sparkflows/hpe
The links to the images need to be whitelisted for it to be downloaded.

Configure environment for Spark/Scala
----------------------------------------

Download the above jar used to submit the Spark job and upload to maprfs 

::

	mapr@edf hadoop fs -put fire-spark_3.3.0-core-3.1.0-jar-with-dependencies.jar /apps/sparkflows

Configure environment for PySpark 
----------------------------------------

Sparkflows currently depends on python3.8. If the current version installed of python on EDF is not 3.8, then follow the below steps to install Python 3.8

* Make sure you have the necessary development tools

::

	sudo yum groupinstall -y "Development Tools"
	sudo yum install -y openssl-devel bzip2-devel libffi-devel

* Download the desired Python versions from the official Python website and compile them.

::

	cd /usr/src
	sudo wget https://www.python.org/ftp/python/3.8.15/Python-3.8.15.tgz
	sudo tar xzf Python-3.8.15.tgz
	cd Python-3.8.15
	sudo ./configure --enable-optimizations
	sudo make altinstall

* Verify Installation

::

	python3.8 --version

* Connect with Sparkflows team to download the dependencies.zip and upload to the maprfs. 

::
            
	mapr@edf hadoop fs -put dep1.zip /apps/sparkflows
	mapr@edf hadoop fs -put dep2.zip /apps/sparkflows
	mapr@edf hadoop fs -put dep3.zip /apps/sparkflows

* Upload the workflowexecutecloud_livy.py to the maprfs

::

	mapr@edf hadoop fs -put workflowexecutecloud_livy.py /apps/sparkflows

* Ensure the PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON are set to python3.8 on both the master and worker nodes.

Checklist for Kubeflow/MLFlow Integration
----------------------------------------

Kubeflow and MLFlow requires tokens to be accessible to by the pods, to be able to authenticate with the Kubeflow & Mlflow services. These tokens are automatically generated and mounted as a volume if the Sparkflows service is running in the user namespace and has the service account set to default-editor.

* A username space, preferable with the name as sparkflows.
* A service account - default-editor that has the roles for listing pods/images in the kubeflow  namespace 

::

	kubectl get serviceaccounts -n sparkflows

Here’s a step-by-step approach:

* Get the RoleBindings for the ServiceAccount
You can filter RoleBindings to find which ones reference the given ServiceAccount. Use the following command, replacing <namespace> with the namespace where the ServiceAccount resides and <service-account-name> with the name of the ServiceAccount:

bash
Copy code

::

	kubectl get rolebindings -n <namespace> -o yaml | grep -A 10 "name: <service-account-name>"
	
* Get the ClusterRoleBindings for the ServiceAccount

Similarly, filter ClusterRoleBindings:

::

	kubectl get clusterrolebindings -o yaml | grep -A 10 "name: <service-account-name>"

* Extract the Roles and ClusterRoles

For each RoleBinding and ClusterRoleBinding you find, note the Role or ClusterRole being used. For example, if you find a RoleBinding that references role-name, you can then look up the details of that Role with:

::

	kubectl get role role-name -n <namespace> -o yaml

And for ClusterRoles:

::

	kubectl get clusterrole clusterrole-name -o yaml
