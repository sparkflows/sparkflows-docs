Kubernetes
==========

Cluster Information
----------------
Following list of commands help you to understand the resources allocated for the kubernetes cluster.

Display endpoint information about the master and services in the cluster
****

::    

  kubectl cluster-info

Display the Kubernetes version running on the client and server
****

::

    kubectl version --short --output=json | jq .serverVersion.gitVersion

Get the configuration of the cluster
****

::

    kubectl version --short --output=json | jq .serverVersion.gitVersion

List all the nodes
****

::

    kubectl get nodes

Describe Node
****

::

    kubectl describe node <node-name>

Get Node Resources:
****

::

    kubectl describe node <node-name> | grep -i capacity

Get Node Status
****

::

    kubectl get nodes -o wide

Get Node Metrics
****

::

    kubectl top node <node-name>
 

Deployments
----------------

::

    # List one or more deployments
    kubectl get deployment
    # Display the detailed state of one or more deployments
    kubectl describe deployment <deployment_name>

Services
----------------

::
                              
    # List all services in the namespace
    kubectl get services
    


Volumes
-------------------

::

    # List PersistentVolumes sorted by capacity
    kubectl get pv --sort-by=.spec.capacity.storage

Namespaces
-------------------

::

    # Create namespace 
    kubectl create namespace <namespace_name>
    # List one or more namespaces
    kubectl get namespace <namespace_name>
    # Display the detailed state of one or more namespace
    kubectl describe namespace <namespace_name>
    # Delete a namespace
    kubectl delete namespace <namespace_name>
    # Display Resource (CPU/Memory/Storage) usage for a namespace
    kubectl top namespace <namespace_name>
 


Pods
-------------------

::

    # Get all running pods in the namespace
    kubectl get pods --field-selector=status.phase=Running
    kubectl get pods --all-namespaces             # List all pods in all namespaces
    kubectl get pods -o wide                      # List all pods in the current namespace, with more details
    kubectl get pods                              # List all pods in the namespace
    kubectl get pod my-pod -o yaml                # Get a pod's YAML
