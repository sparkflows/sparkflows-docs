Running Fire as a Service
=========================

Fire Insights can be configured to run as a service. This way, when the machine reboots, Fire Insights will be automatically restarted.



Prerequisites
----
* Make sure the user has root privileges to create a service.

* Ensure the system uses SystemD as the init system. Supported distributions include:

   * Amazon Linux 2

   * SLES 12

   * CentOS 7 or higher

   * Debian 8 or higher

   * RHEL 7 or higher

   * Ubuntu 15.04 or higher

Steps for Configuring Fire Insights as a Service
----

Step 1: Create a Fire Service
++++
* Create a Fire service that runs as systemd service. This way, Fire Insights will start automatically on reboot.

* Create the service in the folder ``/etc/systemd/system`` and name the file **fire.service**.

  Below, the user is 'sparkflows'. Name it as appropriate for your installation.

  ::

    [Unit]
    Description=Fire
    After=network.target

    [Service]
    Type=forking
    User=sparkflows
    ExecStart=/home/sparkflows/fire.sh
    RestartSec=35
    Restart=on-abort

   [Install]
   WantedBy=multi-user.target

Step 2: Add a Shell Script
++++

* Create a shell script named **fire.sh** and place it at ``/home/sparkflows/fire.sh``.

  Below are its content that make it executable.

  ::

    #!/bin/sh
    cd $fire_home/fire-3.1.0_spark_x.y.z
    ./run-fire-server.sh start

Step 3: Verify and Enable the Service
++++

- Refresh the systemd configuration files:

  ::

    systemctl daemon-reload
   
- Enable the service (if required) to start automatically at boot:

  ::

    systemctl enable fire.service
    
- Verify the systemd unit file configuration:

  ::

    systemctl restart fire.service
    systemctl status fire.service
    

  .. figure:: ../../_assets/user-guide/fire_service_status.PNG
     :scale: 80%
     :alt: fire service
     :align: center
    

.. note:: Make sure that services are enabled.
    
