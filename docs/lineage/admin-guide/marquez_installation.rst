Marquez Installation Guide
=========================

This document provides step-by-step instructions for installing and running **Marquez** using **Docker** and **Kubernetes**. 

Once Marquez is installed and running, you will proceed to configure it with Sparkflows as detailed in :doc:`/lineage/admin-guide/lineage_configuration`.

Overview
--------

`Marquez <https://marquezproject.ai>`_ is an open-source metadata service and the reference implementation of the `OpenLineage <https://openlineage.io>`_ standard. In a Sparkflows deployment, Sparkflows emits lineage events (datasets, job runs, and column transformations) via the OpenLineage Spark agent to Marquez. Marquez stores and indexes this metadata, allowing Sparkflows to render comprehensive data lineage graphs and pipeline dependency traces.

Architecture and Default Ports
------------------------------

Marquez consists of three primary components:

* **Marquez HTTP API (Port 5000):** The RESTful API endpoint that accepts OpenLineage events and serves metadata queries. This is the endpoint configured in Sparkflows as ``openlineage.end.point``.
* **Marquez Admin & Healthchecks (Port 5001):** The administrative interface providing metrics and service healthcheck endpoints (``/healthcheck``).
* **Marquez Web UI (Port 3000):** An interactive web application for browsing jobs, datasets, runs, and lineage graphs directly.
* **PostgreSQL Database (Port 5432):** The backing relational datastore for Marquez metadata.

.. list-table:: Marquez Default Port Mapping
   :widths: 20 15 65
   :header-rows: 1

   * - Service
     - Default Port
     - Description
   * - Marquez HTTP API
     - ``5000``
     - OpenLineage event ingestion and metadata REST API. Used by Sparkflows.
   * - Marquez Admin
     - ``5001``
     - Admin operations, server metrics, and health status.
   * - Marquez Web UI
     - ``3000``
     - Web UI to explore jobs, datasets, and lineage graphs.
   * - PostgreSQL
     - ``5432``
     - Marquez metadata database.

Prerequisites
-------------

Before beginning the installation, ensure the following requirements are met:

* **System Resources:**
   * Minimum: 2 CPU cores, 4 GB RAM, 10 GB disk space.
   * Recommended for production: 4+ CPU cores, 8+ GB RAM, 50+ GB persistent storage.
* **Network Connectivity:** Ports ``5000``, ``5001``, and ``3000`` must be accessible from the machine where Sparkflows and Spark / Livy jobs run.
* **For Docker Deployment:**
   * Docker Engine 17.05 or higher.
   * Docker Compose v2.0 or higher.
   * Git.
* **For Kubernetes Deployment:**
   * Kubernetes cluster v1.12 or higher.
   * ``kubectl`` CLI configured to connect to your cluster.
   * Helm v3.1.0 or higher.

-------------------------------------------------------------------------------

Method 1: Installing Marquez with Docker
----------------------------------------

You can run Marquez using Docker either via the official Marquez startup script or via a standalone Docker Compose file.

Option A: Using the Official Marquez Repository Script (Quickstart)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Marquez project provides an automated startup script (``./docker/up.sh``) that configures the API, Web UI, and PostgreSQL database automatically.

#. **Clone the Marquez GitHub repository:**

   .. code-block:: bash

      git clone https://github.com/MarquezProject/marquez.git
      cd marquez

#. **Start Marquez:**

   Run the startup script:

   .. code-block:: bash

      ./docker/up.sh

   .. tip::

      * To start Marquez with sample lineage metadata (useful for testing), add the ``--seed`` flag:

        .. code-block:: bash

           ./docker/up.sh --seed

      * If port ``5000`` is already in use on your system (e.g., macOS AirPlay Receiver), specify an alternate API port using the ``--api-port`` flag:

        .. code-block:: bash

           ./docker/up.sh --api-port 9000

#. **Verify running containers:**

   Check that all Marquez containers are running:

   .. code-block:: bash

      docker ps

   You should see containers for:
   * ``marquez-api`` (Marquez HTTP API server)
   * ``marquez-web`` (Marquez Web UI)
   * ``marquez-db`` (PostgreSQL metadata database)

#. **Stopping Marquez:**

   To stop Marquez containers:

   .. code-block:: bash

      ./docker/down.sh

Option B: Using Standalone Docker Compose
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you prefer deploying Marquez without cloning the entire Marquez repository, create a dedicated directory and use a standalone ``docker-compose.yml`` file.

#. **Create a working directory:**

   .. code-block:: bash

      mkdir marquez && cd marquez

#. **Create the ``docker-compose.yml`` file:**

   .. code-block:: yaml

      version: '3.7'

      services:
        db:
          image: postgres:14-alpine
          container_name: marquez-db
          restart: always
          environment:
            - POSTGRES_USER=marquez
            - POSTGRES_PASSWORD=marquez
            - POSTGRES_DB=marquez
          volumes:
            - marquez-db-data:/var/lib/postgresql/data
          ports:
            - "5432:5432"
          healthcheck:
            test: ["CMD-SHELL", "pg_isready -U marquez -d marquez"]
            interval: 5s
            timeout: 5s
            retries: 5

        api:
          image: marquezproject/marquez:0.51.1
          container_name: marquez-api
          restart: always
          depends_on:
            db:
              condition: service_healthy
          environment:
            - MARQUEZ_PORT=5000
            - MARQUEZ_ADMIN_PORT=5001
            - POSTGRES_HOST=db
            - POSTGRES_PORT=5432
            - POSTGRES_USER=marquez
            - POSTGRES_PASSWORD=marquez
            - POSTGRES_DB=marquez
          ports:
            - "5000:5000"
            - "5001:5001"

        web:
          image: marquezproject/marquez-web:0.51.1
          container_name: marquez-web
          restart: always
          depends_on:
            - api
          environment:
            - MARQUEZ_HOST=api
            - MARQUEZ_PORT=5000
            - WEB_PORT=3000
          ports:
            - "3000:3000"

      volumes:
        marquez-db-data:

#. **Start Marquez with Docker Compose:**

   .. code-block:: bash

      docker compose up -d

#. **Check container status:**

   .. code-block:: bash

      docker compose ps

-------------------------------------------------------------------------------

Method 2: Installing Marquez with Kubernetes
--------------------------------------------

For production and cloud environments, Marquez provides an official Helm chart located in the Marquez repository under the ``chart/`` directory.

Option A: Deploying via the Official Marquez Helm Chart (Recommended)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. **Clone the Marquez repository:**

   .. code-block:: bash

      git clone https://github.com/MarquezProject/marquez.git
      cd marquez/chart

#. **Update Helm chart dependencies:**

   The Helm chart includes PostgreSQL as a subchart dependency. Update the dependencies before installing:

   .. code-block:: bash

      helm dependency update

#. **Install the Helm Chart:**

   * **Option 1: Deploy with embedded PostgreSQL (for testing/evaluations):**

     .. code-block:: bash

        helm install marquez . \
          --namespace lineage \
          --create-namespace \
          --set postgresql.enabled=true

   * **Option 2: Deploy with an external PostgreSQL database (Recommended for Production):**

     For production setups, connect Marquez to an external managed database (e.g., AWS RDS PostgreSQL, Azure Database for PostgreSQL, Cloud SQL):

     .. code-block:: bash

        helm install marquez . \
          --namespace lineage \
          --create-namespace \
          --set postgresql.enabled=false \
          --set marquez.db.host="<POSTGRES_HOST>" \
          --set marquez.db.port=5432 \
          --set marquez.db.name="marquez" \
          --set marquez.db.user="<POSTGRES_USER>" \
          --set marquez.db.password="<POSTGRES_PASSWORD>"

#. **Verify the deployment:**

   Check the status of pods and services in the ``lineage`` namespace:

   .. code-block:: bash

      kubectl get pods -n lineage
      kubectl get svc -n lineage

   All pods (API, Web, and DB) should display a status of ``Running``.

#. **Run the Helm chart tests:**

   Validate the connectivity and availability of Marquez services:

   .. code-block:: bash

      helm test marquez -n lineage

#. **Expose Marquez services:**

   * **Option 1: Port-Forwarding (for local or internal testing):**

     Forward the API and Web UI ports to your local workstation:

     .. code-block:: bash

        # Expose Marquez API
        kubectl port-forward svc/marquez-api 5000:5000 -n lineage &

        # Expose Marquez Web UI
        kubectl port-forward svc/marquez-web 3000:3000 -n lineage &

   * **Option 2: Ingress (for enterprise domain access):**

     Configure an Ingress resource to route traffic to Marquez API and Web UI using your domain (e.g., ``https://marquez.sparkflows.net``):

     .. code-block:: yaml

        apiVersion: networking.k8s.io/v1
        kind: Ingress
        metadata:
          name: marquez-ingress
          namespace: lineage
          annotations:
            kubernetes.io/ingress.class: nginx
        spec:
          rules:
          - host: marquez.sparkflows.net
            http:
              paths:
              - path: /api
                pathType: Prefix
                backend:
                  service:
                    name: marquez-api
                    port:
                      number: 5000
              - path: /
                pathType: Prefix
                backend:
                  service:
                    name: marquez-web
                    port:
                      number: 3000

Option B: Deploying via Kubernetes Manifests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your environment does not use Helm, you can apply standard Kubernetes manifests:

.. code-block:: yaml

   apiVersion: v1
   kind: Namespace
   metadata:
     name: lineage
   ---
   apiVersion: apps/v1
   kind: Deployment
   metadata:
     name: marquez-api
     namespace: lineage
   spec:
     replicas: 1
     selector:
       matchLabels:
         app: marquez-api
     template:
       metadata:
         labels:
           app: marquez-api
       spec:
         containers:
         - name: marquez-api
           image: marquezproject/marquez:0.51.1
           ports:
           - containerPort: 5000
             name: http
           - containerPort: 5001
             name: admin
           env:
           - name: MARQUEZ_PORT
             value: "5000"
           - name: MARQUEZ_ADMIN_PORT
             value: "5001"
           - name: POSTGRES_HOST
             value: "<POSTGRES_HOST>"
           - name: POSTGRES_PORT
             value: "5432"
           - name: POSTGRES_USER
             value: "<POSTGRES_USER>"
           - name: POSTGRES_PASSWORD
             value: "<POSTGRES_PASSWORD>"
           - name: POSTGRES_DB
             value: "marquez"
           readinessProbe:
             httpGet:
               path: /healthcheck
               port: 5001
             initialDelaySeconds: 15
             periodSeconds: 10
   ---
   apiVersion: v1
   kind: Service
   metadata:
     name: marquez-api
     namespace: lineage
   spec:
     type: ClusterIP
     ports:
     - port: 5000
       targetPort: 5000
       name: http
     - port: 5001
       targetPort: 5001
       name: admin
     selector:
       app: marquez-api

Apply the manifest:

.. code-block:: bash

   kubectl apply -f marquez-deployment.yaml

-------------------------------------------------------------------------------

Verifying the Marquez Installation
----------------------------------

After deploying Marquez, perform the following verification steps:

1. **Verify the Healthcheck Endpoint:**

   Query the Marquez admin healthcheck endpoint:

   .. code-block:: bash

      curl -i http://<marquez-host>:5001/healthcheck

   A healthy installation returns an ``HTTP 200 OK`` status with healthcheck details.

2. **Verify the OpenLineage API Endpoint:**

   Query the namespaces API:

   .. code-block:: bash

      curl -i http://<marquez-host>:5000/api/v1/namespaces

   A successful response returns ``HTTP 200 OK`` with a JSON object listing active namespaces (or an empty list if fresh).

3. **Access the Marquez Web UI:**

   Open your browser and navigate to:

   .. code-block:: text

      http://<marquez-host>:3000

   You should see the Marquez web interface displaying datasets, jobs, and lineage graph navigation.

-------------------------------------------------------------------------------

Next Steps: Configuring Marquez with Sparkflows
-----------------------------------------------

Now that Marquez is successfully installed and verified, note your Marquez API endpoint URL (for example, ``http://localhost:5000`` or ``https://marquez.sparkflows.net``).

Proceed to the next document to configure Sparkflows to emit data lineage to this Marquez instance:

👉 **:doc:`/lineage/admin-guide/lineage_configuration`**

Key parameters you will configure in the next step using your Marquez details:

.. list-table:: Marquez Parameters Used in Sparkflows Configuration
   :widths: 35 30 35
   :header-rows: 1

   * - Marquez Parameter
     - Sparkflows Property / Field
     - Configuration Location
   * - Marquez API Endpoint (e.g. ``http://localhost:5000`` or ``https://marquez.sparkflows.net``)
     - ``openlineage.end.point``
     - **Administration > Configurations** (Step 3)
   * - Marquez Lineage Server URL
     - ``Lineage URL``
     - **Administration > Connections > Add Connection** (Category: Lineage, Type: Open Lineage) (Step 5)
   * - Spark OpenLineage Listener
     - ``openlineage.spark.extraListeners``
     - Sparkflows Configurations & Connections
