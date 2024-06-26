Kubernetes
==========
    
Services
----------------

::

    # Get commands with basic output
    kubectl get services                          # List all services in the namespace
    


Volumes
-------------------

::

    # List PersistentVolumes sorted by capacity
    kubectl get pv --sort-by=.spec.capacity.storage

Pods
-------------------

::

    # Get all running pods in the namespace
    kubectl get pods --field-selector=status.phase=Running
    kubectl get pods --all-namespaces             # List all pods in all namespaces
    kubectl get pods -o wide                      # List all pods in the current namespace, with more details
    kubectl get pods                              # List all pods in the namespace
    kubectl get pod my-pod -o yaml                # Get a pod's YAML
