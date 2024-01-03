Install Jupyter
--------------

With a Kubernetes cluster cluster available and Helm installed, we can install JupyterHub in the Kubernetes cluster using the JupyterHub Helm chart

- Initialize a Helm chart configuration file. Helm charts’ contain templates that can be rendered to the Kubernetes resources to be installed. A user of a Helm chart can override the chart’s default values to influence how the templates render.

In this step we will initialize a chart configuration file for you to adjust your installation of JupyterHub. We will name and refer to it as **config.yaml** going onwards

  .. code-block:: yml

   singleuser:
     defaultUrl: "/lab"
     extraEnv:
       JUPYTERHUB_SINGLEUSER_APP: "jupyter_server.serverapp.ServerApp"
     storage:
       type: none
       extraVolumes:
         - name: jupyterhub-shared
           persistentVolumeClaim:
             claimName: jupyterhub-shared-claim
       extraVolumeMounts:
         - name: jupyterhub-shared
           mountPath: /home/shared
        
- With the above configuration, create persistent volume and persistent volume claim as per the below configuration

  .. code-block:: yml
   
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: jupyter-pv
   spec:
     capacity:
       storage: 5Gi
     volumeMode: Filesystem
     accessModes:
       - ReadWriteOnce
     persistentVolumeReclaimPolicy: Delete
     storageClassName: local-storage
     local:
       path: /mnt/jupyter
     nodeAffinity:
       required:
         nodeSelectorTerms:
           - matchExpressions:
               - key: kubernetes.io/hostname
                 operator: In
                 values:
                   - n3.k8s
   ---
   apiVersion: v1
   kind: PersistentVolume
   metadata:
     name: jupyter-pv-shared
   spec:
     capacity:
       storage: 5Gi
     volumeMode: Filesystem
     accessModes:
       - ReadWriteOnce
     persistentVolumeReclaimPolicy: Delete
     storageClassName: local-storage
     local:
       path: /mnt/jupyter-shared
     nodeAffinity:
       required:
         nodeSelectorTerms:
           - matchExpressions:
               - key: kubernetes.io/hostname
                 operator: In
                 values:
                   - n1.k8s
   ---
   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: jupyterhub-shared-claim
     namespace: demo
   spec:
     accessModes:
       - ReadWriteOnce
     storageClassName: local-storage
     resources:
       requests:
         storage: 5Gi
  
- Make sure you've create a directory **/mnt/jupyter-shared** in the node **n1.k8s** for the persistent volume to work. Once done, run the following the create the PV and PVC::
   
   kubectl apply -f pv.yaml

- Make Helm aware of the JupyterHub Helm chart repository so you can install the JupyterHub chart from it without having to use a long URL name::

   helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
   helm repo update
   
- Now install the chart configured by your config.yaml by running this command from the directory that contains your config.yaml::

   helm upgrade --cleanup-on-fail \
   --install <helm-release-name> jupyterhub/jupyterhub \
   --namespace <k8s-namespace> \
   --create-namespace \
   --version=<chart-version> \
   --values config.yaml
   
  where:

  - <helm-release-name> refers to a Helm release name, an identifier used to differentiate chart installations. You need it when you are changing or deleting the   configuration of this chart installation. If your Kubernetes cluster will contain multiple JupyterHubs make sure to differentiate them. You can list your Helm releases with helm list.

  - <k8s-namespace> refers to a Kubernetes namespace, an identifier used to group Kubernetes resources, in this case all Kubernetes resources associated with the JupyterHub chart. You’ll need the namespace identifier for performing any commands with kubectl.

  - This step may take a moment, during which time there will be no output to your terminal. JupyterHub is being installed in the background.

  - If you get a release named <helm-release-name> already exists error, then you should delete the release by running helm delete <helm-release-name>. Then reinstall by repeating this step. If it persists, also do kubectl delete namespace <k8s-namespace> and try again.

  - In general, if something goes wrong with the install step, delete the Helm release by running helm delete <helm-release-name> before re-running the install command.

  - If you’re pulling from a large Docker image you may get a Error: timed out waiting for the condition error, add a --timeout=<number-of-minutes>m parameter to the helm command.

  - The --version parameter corresponds to the version of the Helm chart, not the version of JupyterHub. Each version of the JupyterHub Helm chart is paired with a specific version of JupyterHub. E.g., 0.11.1 of the Helm chart runs JupyterHub 1.3.0. For a list of which JupyterHub version is installed in each version of the JupyterHub Helm Chart, see the `Helm chart repo <https://jupyterhub.github.io/helm-chart/>`_.
  
  
- While Step 2 is running, you can see the pods being created by entering in a different terminal::
   
   kubectl get pod --namespace demo
   NAME                    READY     STATUS    RESTARTS   AGE
   hub-5d4ffd57cf-k68z8    1/1       Running   0          37s
   proxy-7cb9bc4cc-9bdlp   1/1       Running   0          37s

- Get the host where the proxy is running::
 
    kubectl get pod -n demo --selector="component=proxy" --output=wide
    NAME                    READY   STATUS    RESTARTS   AGE   IP           NODE     NOMINATED NODE   READINESS GATES
    proxy-6f5cf844f-c2sln   1/1     Running   0          34m   10.42.3.43   n3.k8s   <none>           <none>
    
- Get the port of the node, where the proxy is running::
    
    kubectl describe svc/proxy-public -n demo
    ...
    ...
    NodePort:                 http  31980/TCP
    ...
    ...
- Access the Jupyter lab from url - http://<public-ip-node>:31980/
