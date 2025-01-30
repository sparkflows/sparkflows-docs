InfluxDB and Grafana Setup
========

InfluxDB and Grafana overview
----

overview
++++++++

InfluxDB is an open source time series database that is optimized for fast and highly available data storage for time series data in use cases like monitoring, application metrics, IoT sensor data, real-time analytics, and more.


Grafana is an open source data visualization and monitoring platform. It is used to create dashboards and visualize data from a variety of sources like Prometheus or InfluxDB.
Grafana allows users to quickly create visualizations of their data, such as graphs, tables, and heatmaps. It also provides alerting capabilities, allowing users to be notified when certain conditions are met.


Setting up InfluxDB and Grafana
++++++

Installing InfluxDB and Grafana. First you’ll need to make sure you have the following on your system:


#. InfluxDB CLI
#. Docker Desktop

Docker setup
+++++

This document will use docker-compose to manage Grafana and InfluxDB. Before running the following script make sure to navigate to the directory where you want the project to be located.
Once you are in the desired folder, run the following script in the command line:

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

This script will create a docker-compose.yml file which defines the network and images used for InfluxDB and Grafana. To start the containers you just need to run the following command:

::

    docker-compose up -d

InfluxDB setup
+++++

Setup of credentials required when initiating connection to InfluxDB is as follows.

Create initial super-admin credentials, organization, bucket and the all-access security token. Run the influx setup command:

::

    influx setup --name myinfluxdb2 --host http://localhost:8086 \
    -u admin -p admin54321 -o my-org \
    -b my-bucket -t my-token -r 0 -f


The superuser, organization, bucket, and access token have been created. In addition, the influx command creates a new server configuration object and stores it into the active config named myinfluxdb.

.. Note:: You can define as many configs as you want to work with multiple InfluxDB2 servers easily. The configuration objects are stored locally in the $HOME/.influxdbv2/configs file on your computer. To list all available server configurations use the command influx config ls.

Grafana and InfluxDB connection setup
+++++

#. Add data source in Grafana UI
#. Open in browser http://localhost:3000/datasources
#. Sign in as user admin, password admin.
#. Click on Skip to skip the question about the new password.
#. In the left menu, click on the Gear icon, to open Data Sources.
#. Click on Add data source.
#. Select InfluxDB.
#. Replace InfluxQL with Flux in the dropdown called Query Language.
#. Type http://influxdb:8086/ at the URL field in the section called HTTP.
#. Write my-org into the Organization field in the InfluxDB Details section.
#. Type my-token in the Token field. (Once the save and test button is clicked, the password is hidden and replaced with configured.)
#. Save & Test: Success will display two green notifications (3 buckets found + Datasource updated).

.. Note:: The address http://influxdb:8086/ is the address visible from the Grafana container in the internal network orchestrated by docker-compose.

`Click here <https://www.influxdata.com/blog/getting-started-influxdb-grafana/>`_ to get more details on setting up Grafana and Influx DB.
