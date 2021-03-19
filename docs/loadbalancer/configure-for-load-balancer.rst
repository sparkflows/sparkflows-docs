Configure for Load Balancer
===========================

In order to scale out, multiple machines running Fire Insights can be configured under a Load Balancer.

In this case an external database has to be used for Fire Insights. All of the Fire Servers under the Load Balancer would be connecting to the same database instance.

There are additional configurations needed for each Fire Server in such a scenario.

application.properties
----------------------

Add the following parameter in application.properties of each Fire Server. This is to enable it to know its IP address.

.. list-table:: 
   :widths: 10 30 20
   :header-rows: 1

   * - Parameter
     - Description 
     - Value
   * - spring.application.name
     - unique application name
     - fire-1
   * - clustermode.enable
     - make it true if using more than one Fire machine
     - true
   * - fire-machine-ip
     - machine ip details to understand where Fire is running
     - Machine-ip  
  
  
