Working With Dashboards
=======================

Sparkflows allows you to create Dashboards.

Processors in Sparkflows can output data in Tables, Charts, Maps and simple strings. Dashboards allow combining the output of various processors into one User Interface.

For example we might want to output a chart of number of bike rentals per hour, another by per day and another map displaying the total number of bike rentals per city for the day. Dashboards can combine all these into one view.
 
Creating Dashboards
--------------------
 
  * For creating Dashboards, drag and drop the required processors from the workflows into the Dashboard Canvas.
  * When the corresponding workflows are run, the output is stored by Fire into the relational store. These get displayed into the Dashboard.
 
Editing Dashboards
------------------
 
  * Editing dashboards is like creating dashboards, except that you click the edit button to edit the corresponding Dashboard.
 
.. figure:: ../../_assets/user-guide/editing-dashboards.png
   :alt: Sparkflows Editing Dashboards
   :align: center
   :width: 60%
   
Viewing Dashboards
------------------

  * Once a Dashboard has been created you can view it, by clicking on the View button.
  
.. figure:: ../_assets/user-guide/dashboard-view.png
   :alt: Sparkflows Dashboard
   :align: center  
   :width: 60%
   
Streaming Dashboards
---------------------
 
  * Fire allows you to create Streaming Workflows.
  * Streaming workflows have a mini-batch duration - say 30 seconds.
  * In this case, the output in the Dashboards get updated every 30 seconds as new data comes in.



