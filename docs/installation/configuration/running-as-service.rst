Running Fire as a Service
=========================

Fire Insights can be configured to run as a service. This way when the machine reboots, Fire Insights would be automatically restarted.

Below are the steps for configuring Fire Insights as a service.

Prerequisites
+++++++++++++

::
   
   Make sure that user have root privilege to create a service.
   System Distribution have SystemD as init system (Amazon Linux 2, SLES 12, CentOS 7 or higher, Debian 8 or higher, RHEL 7 or higher, Ubuntu 15.04 or higher)

Create a fire service
--------------------

Create a fire service which run as systemd service as specific user(for Fire Insights to start up at reboot), inside `/etc/systemd/system` location, which trigger a shell script to start Fire Insights server.


