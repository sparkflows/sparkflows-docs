Update/Upgrade Sparkflows in HPE EzUA
=====

This document provides detailed instructions on how to update Sparkflows in HPE UA.

Step 1 : Access the Frameworks in HPE UA
---------------------------------------------
#. Navigate to the Frameworks section in the HPE UA platform.

Step 2 : Remove the Existing Sparkflows Framework
------------------------------------------------
#. Go to the **Analytics** tab.
#. Delete the installed Sparkflows framework.
#. Wait for 3-4 minutes to allow UA to clean up the Pods associated with Sparkflows.

   .. figure:: ../../_assets/hpe/sflowsonua-tools-n-frameworks.png
      :width: 60%
      :alt: Sparkflows On UA

Step 3 : Add a New Framework
-------------------------------
#. Click on **Add New Framework**.
#. Provide the basic details such as Name, Version, Description, Sparkflows Icon (upload from the pictures window).

   .. figure:: ../../_assets/hpe/sflowsonua-framework-import.png
      :width: 60%
      :alt: Sparkflows On UA

Step 4 : Select the Latest Sparkflows Chart Version
-----------------------------------------------------
#. Choose the latest Sparkflows chart version, which is **0.1.32** (as of now).
#. Enter the namespace as **sparkflows**.

   .. figure:: ../../_assets/hpe/sflowsonua-framework-chart1.png
      :width: 60%
      :alt: Sparkflows On UA

Step 5 : Configure the Release Name and Options
-----------------------------------------------
#. Set the Release Name to **fire-v72** and uncheck all the available options.

   .. figure:: ../../_assets/hpe/sflowsonua-framework-chart2.png
      :width: 60%
      :alt: Sparkflows On UA

Step 6 : Update the Version in the Chart Configuration
----------------------------------------------------------
#. Click **Next**.
#. In the chart configuration, update the version of the image to the latest one.

   .. figure:: ../../_assets/hpe/sflowsonua-framework-values.png
      :width: 60%
      :alt: Sparkflows On UA
