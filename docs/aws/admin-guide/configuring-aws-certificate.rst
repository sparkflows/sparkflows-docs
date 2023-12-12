Configure HTTPS
================

Fire Insights can be configured with HTTPS on AWS, when running on EC2 instance.

With AWS Certificate Manager (ACM) you can provision and manage SSL or TLS certificates for your AWS based websites and applications. 

You can use ACM to create or import and then manage a certificate.

This document describes the steps needed to configure HTTPS. Below is a brief outline of the steps involved in the process :

#. Pre-requisites
#. Register Domain Names
#. Get Certificate from ACM
#. Create a Load Balancer
#. Create a Record and Map to the Load Balancer
#. Login to Access Fire Insights Application

Step 1 : Pre-requisites
--------

You need to have the following before stepping into the process of configuration :

#. AWS account with required access to the resources
#. Registered Domain names
#. Load Balancer
#. Route 53

Step 2 : Register Domain Names
------------------

#. **Understanding FQDN :**

   A fully qualified domain name (FQDN) is the unique name of an organization or individual on the internet followed by a top-level domain extension such as .com or .org. 

#. **Getting a Domain Name :**

   If you don't have a domain name yet, you can easily register one through **Amazon Route 53**.

   If you want to get a new domain name, such as the example.com as part of the URL http://example.com, you can register it with Amazon Route 53.

   For more details, visit `Amazon Route 53 Registrar Guide <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/registrar.html>`_


Step 3 : Get Certificate from ACM
----------------
#. **Understanding AWS Certificate Manager (ACM) :**

   This service is for enterprise customers who need a secure web presence using TLS. ACM certificates are deployed through Elastic Load Balancing, Amazon CloudFront, Amazon API Gateway, and other integrated AWS services. The most common application of this kind is a secure public website with significant traffic requirements.

#. **Filling Details to Request Certificate :**
 
   You can request a certificate by filling the details given below::


    Domain names : Fully qualified domain name
    Validation method : Select a method for validating domain ownership
    Key algorithm : Key algorithm

* **Select Certificate Type as Public Certificate :**

  .. figure:: ../../_assets/aws/aws-certificate/request_certificate.PNG
      :alt: aws
      :width: 65%

* **Enter the Domain Name (FQDN) :**

  .. figure:: ../../_assets/aws/aws-certificate/request_details_1.PNG
      :alt: aws
      :width: 65%  

* **Select Validation Method as DNS Validation :**

  .. figure:: ../../_assets/aws/aws-certificate/request_details_2.PNG
      :alt: aws
      :width: 65%   

* **Select appropriate Key Algorithm and Add Tags :**

  .. figure:: ../../_assets/aws/aws-certificate/request_details_3.PNG
      :alt: aws
      :width: 65%      

Step 4 : Create a Load Balancer
------

#. **Create a Load Balancer and Configure Target Group with Fire Insights running on that Instance :**

   .. figure:: ../../_assets/aws/aws-certificate/load_blanacer.PNG
      :alt: aws
      :width: 65%

   .. figure:: ../../_assets/aws/aws-certificate/load_app.PNG
      :alt: aws
      :width: 55%

* **Create Security Group, Target group and Configure Listener Settings :**   
  
  .. figure:: ../../_assets/aws/aws-certificate/load_confugurations.PNG
     :alt: aws
     :width: 55% 

  .. figure:: ../../_assets/aws/aws-certificate/load_configuration_1.PNG
      :alt: aws
      :width: 55%    

* **Create, Configure and Register Target Group Settings :**
   
  .. figure:: ../../_assets/aws/aws-certificate/load_target.PNG
      :alt: aws
      :width: 55%   
   
  .. figure:: ../../_assets/aws/aws-certificate/load_target_configure.PNG
      :alt: aws
      :width: 55%  
   
  .. figure:: ../../_assets/aws/aws-certificate/load_target_instance.PNG
      :alt: aws
      :width: 55%     

Step 5 : Create a Record and Map to the Load Balancer
-----------------------------------
 
#. **Go to Route 53 to Create a Record and Map to the Load Balancer :**

   .. figure:: ../../_assets/aws/aws-certificate/load_record.PNG
      :alt: aws
      :width: 55% 
   
   .. figure:: ../../_assets/aws/aws-certificate/load_record1.PNG
      :alt: aws
      :width: 55%    

Step 6 : Login to Access Fire Insights Application
-----------------
Once the above steps get successfully updated, you can login to the Domain name with **HTTPS** and be able to access Fire Insights application running on the target instance.

.. note:: Above steps are verified with Fire Insights running on HTTPS(443) on port 8443 which is provided by default.
