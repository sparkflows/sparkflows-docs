InfluxDB and Grafana Setup
===========

This document provides a guide on setting up InfluxDB and Grafana using Docker for monitoring and visualization. It includes the following key aspects:

* Overview of InfluxDB and Grafana
* Prerequisites for Setting up InfluxDB and Grafana
* Setting up InfluxDB
* Connecting Grafana to InfluxDB


Overview of InfluxDB and Grafana 
-----

**InfluxDB** is an open source time series database optimized for fast and highly available storage for time series data. It is commonly used for monitoring, application metrics, IoT sensor data, real-time analytics, and more.

**Grafana** is an open source data visualization and monitoring platform. It allows users to create dashboards and visualize data from a variety of sources like Prometheus and InfluxDB.
Grafana allows users to quickly create visualizations of their data, such as graphs, tables, and heatmaps. It also provides alerting capabilities to notify users when certain conditions are met.

Prerequisites for Setting up InfluxDB and Grafana
-----

To install InfluxDB and Grafana, ensure you have the following installed on your system:

#. InfluxDB CLI
#. Docker Desktop

Docker setup
+++++

Here, we will use docker-compose to manage Grafana and InfluxDB. Follow the steps below:

#. Before running the following script, navigate to the **directory** where you want the project to be located.

#. Once you are in the desired folder, run the following script in the command line to create a **docker-compose.yml** file that defines the network and images used for InfluxDB and Grafana.

   ::

       mkdir influxdb-getting-started-with-grafana
       cd influxdb-getting-started-with-grafana
       cat > ./docker-compose.yml <<EOF
       version: "3"

       networks:
         monitoring:

       services:
         influxdb:
           image: influxdb:2.3.0
           ports:
             - 8086:8086
           networks:
             - monitoring

         grafana:
           image: grafana/grafana:9.0.4
           ports:
             - 3000:3000
           networks:
             - monitoring
       EOF



#. To start the containers, run the following command:

   ::

       docker-compose up -d

InfluxDB Setup
-----

The required credential setup for initiating a connection to InfluxDB is as follows:

#. To create initial super-admin credentials, organization, bucket and the all-access security token, run the following **influx setup command**:

   ::

       influx setup --name myinfluxdb2 --host http://localhost:8086 \
       -u admin -p admin54321 -o my-org \
       -b my-bucket -t my-token -r 0 -f


   The superuser, organization, bucket, and access token have been created. Additionally, the influx command creates a new server configuration object and stores it in the active configuration named **myinfluxdb**.

.. Note:: You can define multiple configurations to easily work with multiple InfluxDB 2 servers. The configuration objects are stored locally in the **$HOME/.influxdbv2/configs** file on your computer. To list all available server configurations, use the command **influx config ls**.

Grafana and InfluxDB Connection Setup
-----

To visualize data from InfluxDB in Grafana, you need to add InfluxDB as a data source in Grafana UI. Follow the steps below:

#. Open Grafana in your browser: http://localhost:3000/datasources

#. Sign in using: 

   * Username: admin 
   * Password: admin

#. Click on **Skip** when prompted to set a new password.

#. In the left menu, click on **Gear** icon to open **Data Sources**.

#. Click on **Add data source** and Select **InfluxDB**.

#. Change the **Query Language** dropdown from **InfluxQL** to **Flux**.

#. In the **HTTP** section, set URL to http://influxdb:8086/.

#. In the **InfluxDB Details** section, enter **my-org** in the Organization field and **my-token** in the Token field. (Once the save and test button is clicked, the password is hidden and replaced with configured.)

#. Click on **Save & Test** button: If successful, it will display two green notifications:

   * 3 buckets found
   * Datasource updated

.. Note:: The address http://influxdb:8086/ is the address visible from the Grafana container in the internal network orchestrated by docker-compose.

`Click here <https://www.influxdata.com/blog/getting-started-influxdb-grafana/>`_ to get more details on setting up Grafana and Influx DB.
