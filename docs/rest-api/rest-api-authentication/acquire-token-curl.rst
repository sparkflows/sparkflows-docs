Acquire Token 
==================

Tokens can be acquired from Fire Insights Application. They would then be used in making the subsequent curl requests.

Below are steps for Generating Access Token in Fire Insights:

1. Login to Fire Insights Application and enable configuration for generating tokens.

Once Login to Fire Insights Application as Administrator user, go to Configurations page and enable below parameters

::

    module.enableTokenGeneration : true

.. figure:: ../../_assets/rest-api/configuration.PNG
   :alt: rest-api
   :width: 60%

2. Once the configuration is enabled, go to ``User Profile``, it will take you to ``PROFILE & SETTINGS`` page which has Generate Access Token tab.

.. figure:: ../../_assets/rest-api/token_page.PNG
   :alt: rest-api
   :width: 60%

3. Click on ``GENERATE ACCESS TOKEN`` tab, It will pop up a new windows with below informations.

::

    TOKEN EXPIRATION DURATION (DAYS) : Number of Days for Token Expirations
    DESCRIPTION : Descriptions for Token Generated

.. figure:: ../../_assets/rest-api/generate_token_page.PNG
   :alt: rest-api
   :width: 60%
   
4. Once done with above informations, Click on ``GENERATE`` tab which will create a new token.

.. figure:: ../../_assets/rest-api/token_copy.PNG
   :alt: rest-api
   :width: 60%
   
5. You can copy the token generated and press ok to see the token created in the list and it can be used in making the subsequent curl requests.

.. figure:: ../../_assets/rest-api/token_list.PNG
   :alt: rest-api
   :width: 60%

.. note::  Make sure that Access Token Generated for user should have sufficient privilege.
