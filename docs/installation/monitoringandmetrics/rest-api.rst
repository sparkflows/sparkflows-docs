Swagger REST API's
=========

Fire Insights enable you to use Swagger REST API'S.

It can be accessible only when admin provide privilge to access it.

Below are steps:

1. Enable Swagger inside ``application.properties``

Do this by adding the line below to application.properties
::

    swagger.enable=true

2. Enable it from Configurations page

Once the above configurations is updated and Fire server got restarted, Login to Fire Insights application and enable below configurations.

.. figure:: ../../_assets/installation/metrics/swagger.PNG
   :alt: metrics
   :width: 60%

3. Now you can access Swagger REST API'S using below url

Login to below url:

::

    https://localhost:port/swagger-ui.html
    
.. figure:: ../../_assets/installation/metrics/ui.PNG
   :alt: metrics
   :width: 60%    
    
.. note::  Make sure to change localhost with respective ip or domain name and the port on which Fire Insights is running.    

