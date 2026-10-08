Sparkflows Configuration
===========================

In order to scale out, multiple machines running Sparkflows can be configured under a load balancer.

In this case an external database has to be used for Sparkflows. All of the Fire servers under the load balancer would be connecting to the same database instance.

There are additional configurations needed for each Fire server in such a scenario.

application.properties
----------------------

Add the following parameters in application.properties of each Fire server. This is to enable it to know its IP address.
Restart Sparkflows server after making the changes.

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
  
  
