AWS Network Load balancers
==========================

It Explains about Creating Network Load balancer in AWS and Configuring it VM running with Fire Insights.

Below are steps involved in Creating Network Load balancer in AWS.

* Login with AWS Console and search for load balancer with EC2 feature.

.. figure:: ..//_assets/loadbalancer/loadbalncer_search.PNG
   :alt: Load balancers
   :align: center
   :width: 60%

* Create Load Balancer & select Network Load Balancer.

.. figure:: ..//_assets/loadbalancer/loadbalancer_create.PNG
   :alt: Load balancers
   :align: center
   :width: 60%
   
* Configure Load balancer
 
::
 
    Add Name
    Scheme : internet-facing
    IP address type : ipv4
    Listeners
    Load Balancer Protocol : TCP  Port: 443
    Availability Zones
    VPC : select VPC where application vm is running.
    Availability Zones : select the specific zone.

