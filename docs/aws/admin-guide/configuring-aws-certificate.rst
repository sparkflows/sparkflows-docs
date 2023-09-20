Configure HTTPS
================

Fire Insights can be configured with HTTPS on AWS, when running on EC2 instance.

With AWS Certificate Manager (ACM) you can provision and manage SSL or TLS certificates for your AWS based websites and applications. You can use ACM to create or import and then manage a certificate.

Prerequisite
--------

You need to have:

1. AWS account with required access to the resources.
2. Registered Domain names.
3. Load Balancer.
4. Route 53.

Register Domain Names
------------------

A fully qualified domain name (FQDN) is the unique name of an organization or individual on the internet followed by a top-level domain extension such as .com or .org. If you do not already have a registered domain name, you can register one through Amazon Route 53.

When you want to get a new domain name, such as the example.com  as part of the URL http://example.com, you can register it with Amazon Route 53.

For more details, visit : https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html


AWS Certificate Manager (ACM)
----------------

This service is for enterprise customers who need a secure web presence using TLS. ACM certificates are deployed through Elastic Load Balancing, Amazon CloudFront, Amazon API Gateway, and other integrated AWS services. The most common application of this kind is a secure public website with significant traffic requirements.

Request a certificate by filling the details given below::


    Domain names : Fully qualified domain name
    Validation method : Select a method for validating domain ownership
    Key algorithm : Key algorithm

.. figure:: ../../_assets/aws/aws-certificate/request_certificate.PNG
   :alt: aws
   :width: 65%
   
.. figure:: ../../_assets/aws/aws-certificate/request_details_1.PNG
   :alt: aws
   :width: 65%  
   
.. figure:: ../../_assets/aws/aws-certificate/request_details_2.PNG
   :alt: aws
   :width: 65%   
   
.. figure:: ../../_assets/aws/aws-certificate/request_details_3.PNG
   :alt: aws
   :width: 65%      

Create a Load Balancer
------

Create a Load Balancer and configure target group with Fire Insights running on that instance.

.. figure:: ../../_assets/aws/aws-certificate/load_blanacer.PNG
   :alt: aws
   :width: 65%

.. figure:: ../../_assets/aws/aws-certificate/load_app.PNG
   :alt: aws
   :width: 55%
   
.. figure:: ../../_assets/aws/aws-certificate/load_confugurations.PNG
   :alt: aws
   :width: 55%  
   
.. figure:: ../../_assets/aws/aws-certificate/load_configuration_1.PNG
   :alt: aws
   :width: 55%    
   
.. figure:: ../../_assets/aws/aws-certificate/load_target.PNG
   :alt: aws
   :width: 55%   
   
.. figure:: ../../_assets/aws/aws-certificate/load_target_configure.PNG
   :alt: aws
   :width: 55%  
   
.. figure:: ../../_assets/aws/aws-certificate/load_target_instance.PNG
   :alt: aws
   :width: 55%     

Create a record and map to the Load Balancer
-----------------------------------
 
Go to Route 53 to create a record and map to the Load Balancer.

.. figure:: ../../_assets/aws/aws-certificate/load_record.PNG
   :alt: aws
   :width: 55% 
   
.. figure:: ../../_assets/aws/aws-certificate/load_record1.PNG
   :alt: aws
   :width: 55%    
   
Once the above steps get successfully updated, you can login to the Domain name with ``HTTPS`` and  be able to access Fire Insights application running on the target instance.

.. note:: Above steps are verified with Fire Insights running on HTTPS(443) on port 8443 which is provided by default.
