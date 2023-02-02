Route 53 
==========

This page explains the steps for configuring "Route 53" with network load balancer.


Login to AWS console and type "R 53" in search box
--------

Sign in to the AWS Management Console and open the Route 53 console at https://console.aws.amazon.com/route53/


.. figure:: ../..//_assets/loadbalancer/loadbalancer_route.PNG
   :alt: Load balancers
   :width: 60%

Get started with R 53 Dashboard
--------

:: 
 
    Register a domain.
    
.. figure:: ../..//_assets/loadbalancer/loadbalancer_getstarted.PNG
   :alt: Load balancers
   :width: 60%    

Hosted zone
-------

Create hosted zone.

.. figure:: ../..//_assets/loadbalancer/loadbalancer-hosted.PNG
   :alt: Load balancers
   :width: 60% 
   
Create records
------

Create records and Registered Network load balancer to it.

::

    Value/Route traffic to : Alias to Network LB
    Select Zone
    By default load balancer domain name should be populated.
    Record type : A -Routes traffic to IPV4 address and some aws resources.
    Routing policy : Simple Routing
    
.. figure:: ../..//_assets/loadbalancer/loadbalancer_records.PNG
   :alt: Load balancers
   :width: 60%     

.. figure:: ../..//_assets/loadbalancer/loadbalancer_alias.PNG
   :alt: Load balancers
   :width: 60%  
