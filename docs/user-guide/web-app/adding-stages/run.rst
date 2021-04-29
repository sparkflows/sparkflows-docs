Run Stage
======================

- In run stage we will execute the notebook with all parameters added in the App.

- Let's first add title in page if needed with "html element" component like below.

   .. figure:: ../../_assets/web-app/add-stage-run-title.PNG
      :alt: web-app
      :width: 60%
   

-  Now, let's add column component in the bottom and divide it into two columns for adding the ``back`` and ``run`` buttons.

-  Add back button in first column to go to back stage and perform actions depending upon event. Set its event name as ``back``.

-  Add next button in second column to go to next stage and perform actions depending upon event. Set its add event name as ``execute``. We can also can add CUSTOM CSS CLASS like          float-right, float-left etc

   .. figure:: ../../_assets/web-app/add-stage-run-runbtn.PNG
      :alt: web-app
      :width: 60%
   

   .. figure:: ../../_assets/web-app/add-stage-run-buttons.PNG
      :alt: web-app
      :width: 60%
   

Click on "DONE" or "SAVE" to save added components for that stage
