Update/Upgrade Sparkflows in HPE EzUA
=====

This document explains in detail the steps involved in updating Sparkflows on HPE UA.

#. Navigate to the frameworks in UA

#. Click on the Analytics tab and delete the installed sparkflows framework. Wait for 3-4 minutes for UA to clean up the Pods of Sparkflows

   .. figure:: ../../_assets/hpe/sflowsonua-tools-n-frameworks.png
      :width: 60%
      :alt: Sparkflows On UA

#. Click on Add new framework, and provide the basic details - Name, version, description and sparkflows icon(upload from pictures window)

   .. figure:: ../../_assets/hpe/sflowsonua-framework-import.png
      :width: 60%
      :alt: Sparkflows On UA

#. Choose the latest Sparkflows chart version which is 0.1.32 (as of now), enter the namespace as sparkflows. 

   .. figure:: ../../_assets/hpe/sflowsonua-framework-chart1.png
      :width: 60%
      :alt: Sparkflows On UA

#. Set the release name is **fire-v72** and uncheck all the options

   .. figure:: ../../_assets/hpe/sflowsonua-framework-chart2.png
      :width: 60%
      :alt: Sparkflows On UA

#. Click next and update the version of the image in the Chart configuration. 

   .. figure:: ../../_assets/hpe/sflowsonua-framework-values.png
      :width: 60%
      :alt: Sparkflows On UA
