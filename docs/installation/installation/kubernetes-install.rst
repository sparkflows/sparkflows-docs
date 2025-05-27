Kubernetes Installation
===============

Deploy Sparkflows with MySQL on Kubernetes using Helm charts.

What You Need
=============

* Kubernetes cluster running
* ``kubectl`` and ``helm`` installed
* Sparkflows Helm charts
* Database credentials file (``secrets.yaml``)

Setup Steps
===========

1. Create Namespace
-------------------

.. code-block:: bash

   kubectl create namespace sparkflows

2. Deploy MySQL
---------------

.. code-block:: bash

   helm install mysql ./chart/mysql --namespace default

Check MySQL is running:

.. code-block:: bash

   kubectl get pods --namespace default

3. Configure Database Connection
--------------------------------

Get MySQL ClusterIP and encode it:

.. code-block:: bash

   echo -n 'ClusterIP' | base64

Update ``secrets.yaml`` with the encoded ClusterIP as ``DB_HOST``, then apply:

.. code-block:: bash

   kubectl apply -f ./config/secrets.yaml --namespace sparkflows

4. Deploy Sparkflows
--------------------

.. code-block:: bash

   helm install fire ./chart/fire --namespace sparkflows

Check deployment:

.. code-block:: bash

   kubectl get pods --namespace sparkflows

5. Verify Connection
--------------------

.. code-block:: bash

   kubectl logs <fire-pod-name> --namespace sparkflows

Common Issues
=============

**Probe Failures**: Increase ``initialDelaySeconds`` and ``timeoutSeconds`` in ``values.yaml``

**MySQL Connection**: 

* Verify ``DB_HOST`` in secrets
* Confirm MySQL runs on port 3306

Key Points
==========

* MySQL deploys in ``default`` namespace
* Sparkflows app deploys in ``sparkflows`` namespace  
* Secrets must be applied before deploying the app
* Use ClusterIP (not service name) for database host

More Kubernetes based deployment options
===========================================

* https://docs.sparkflows.io/en/latest/aws/admin-guide/aws-eks/deployment.html
* https://docs.sparkflows.io/en/latest/kubernetes/fire-insights.html
* https://docs.sparkflows.io/en/latest/jupyter-guide/analytical-apps/create-docker-image.html


