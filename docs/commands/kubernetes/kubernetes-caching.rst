Kubernetes Caching
==================

Pre-pulling Images in Kubernetes
--------------------------------

When you deploy a pod in Kubernetes, the container image is pulled from the container registry. This can cause a delay in the pod startup time. To avoid this delay, you can pre-pull the images on all the nodes in the cluster.

To achieve this, we can use a DaemonSet to deploy a pod on each node that pulls the required images. 
Here's an example:

  .. code-block:: YAML

        apiVersion: apps/v1
        kind: DaemonSet
        metadata:
        name: image-puller
        spec:
        selector:
            matchLabels:
            app: image-puller
        template:
            metadata:
            labels:
                app: image-puller
            spec:
            containers:
            - name: image-puller
                image: docker:latest
                command: ["/bin/sh", "-c", "for img in $(cat /images.txt); do docker pull $img; done"]
                volumeMounts:
                - name: image-list
                mountPath: /images.txt
                subPath: images.txt
            volumes:
            - name: image-list
                configMap:
                name: image-list


In this case, you need to create a ConfigMap named ``image-list`` containing the image names. This approach allows you to automate the process within the Kubernetes ecosystem.

There is another way to cache images on all nodes using the tool `Kubernetes Image Puller <https://github.com/che-incubator/kubernetes-image-puller>`_. This tool when deployed using helm chart, creates a daemon set which, based on the configured list of images, creates a pod for each of those images, with a sleep 720 command, to download images on all the nodes.

