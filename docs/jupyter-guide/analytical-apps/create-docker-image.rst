Create Docker image with the Jupyter notebook 
================

Create a Docker image containing user-created notebooks, data, and required dependencies.

Refer to the `Dockerfile and other details <https://github.com/sparkflows/fire-tools/tree/main/jupyter-docker>`_ to get more details.

Below are the Docker commands used to build the image and push it to Docker Hub, making it accessible for pulling:
::

    Docker Build command - docker build -t username/repo:tagname 

    Docker Push command - docker push username/repo:tagname


.. note:: Ensure that you replace **username/repo** and **tagname** with the actual names. Take note of the image name, which will be used in the next steps when creating a Jupyter connection in Fire Insights.

Deploy Docker image in Kubernetes
---------------------------------

Fire Insights uses the below YAML files to deploy in kubernetes cluster:

deployment.yaml
+++++

    .. code:: YAML

        apiVersion: apps/v1
        kind: Deployment
        metadata:
            name: sparkflows-app
            labels:
                app: sparkflows-app
        spec:
            replicas: 1
            selector:
                matchLabels:
                app: sparkflows-app
            template:
                metadata:

                labels:
                    app: sparkflows-app
                spec:
                serviceAccountName: sparkflows-admin
                volumes:
                    - name: sparkflows-vol
                    persistentVolumeClaim:
                        claimName: fire-pvc
                containers:
                    - name: sparkflows-fire-jupyter
                    image: "sparkflows/fire:py_3.2.1_3.2.81-rc1"
                    imagePullPolicy: IfNotPresent
                    volumeMounts:
                        - name: sparkflows-vol
                        mountPath: /data
                    env:
                        - name: KEYSTORE_PASSWORD
                        value: "12345678"

                    ports:
                        - name: http
                        containerPort: 8080
                        protocol: TCP
                    livenessProbe:
                        httpGet:
                        path: /
                        port: 8080
                        initialDelaySeconds: 80
                        periodSeconds: 20
                    readinessProbe:
                        httpGet:
                        path: /
                        port: 8080

        ---

        apiVersion: v1
        kind: Service
        metadata:
            name: sparkflows-app
            labels:
                app: sparkflows-app
        spec:
            type: LoadBalancer
            ports:
                - port: 8080
                targetPort: http
                protocol: TCP
                name: http
            selector:
                app: sparkflows-app

serviceaccount.yaml
+++++
Create a user account with a name say `sparkflows-admin`, and add the role which was used to create the EKS in the annotation
    
        .. code:: YAML
    
            apiVersion: v1
            kind: ServiceAccount
            metadata:
                name: sparkflows-admin
            annotations:
                eks.amazonaws.com/role-arn: arn:aws:iam::xxxxxxxxxxxx:role/eks-stem

role.yaml
+++++
Create user job role, that defines the set of permissions required for Sparkflows in order to run Jupyter notebook.
    
        .. code:: YAML
    
            apiVersion: rbac.authorization.k8s.io/v1
            kind: ClusterRole
            metadata:
            name: job-creator
            rules:
            - apiGroups: ["batch",""]
              resources:
              - jobs
              - pods
              - pods/log
              verbs:
              - create
              - get
              - update
              - watch
              - list
              - delete


binding.yaml
+++++
Bind the role using the job-binding resource, with subject as sparkflows-admin
    
        .. code:: YAML
    
            apiVersion: rbac.authorization.k8s.io/v1
            kind: ClusterRoleBinding
            metadata:
                name: job-creator-binding
            subjects:
            - kind: ServiceAccount
                name: sparkflows-admin
                namespace: default
            roleRef:
                kind: ClusterRole
                name: job-creator
                apiGroup: rbac.authorization.k8s.io




