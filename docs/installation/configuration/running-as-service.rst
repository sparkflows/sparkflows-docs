Running Fire as a Service
=========================

Fire Insights can be configured to run as a service. This way when the machine reboots, Fire Insights would be automatically restarted.

Below are the steps for configuring Fire Insights as a service:

Prerequisites
+++++++++++++

::
   
   Make sure that user has root privilege to create a service.
   System Distributions that have SystemD as init system (Amazon Linux 2, SLES 12, CentOS 7 or higher, Debian 8 or higher, RHEL 7 or higher, Ubuntu 15.04 or higher).

Create a Fire service
--------------------

Create a Fire service which runs as systemd service. This way Fire Insights would get started automatically on reboot.

Create the service in the folder '/etc/systemd/system'. Name the file 'fire.service'.

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

Add a Shell Script
----------------

Create a shell script 'fire.sh' and place it at '/home/sparkflows/fire.sh'.

Below are its content that make it executable.

::

    #!/bin/sh
    cd $fire_home/fire-3.1.0_spark_x.y.z
    ./run-fire-server.sh start

Verify using the steps below:

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
    
