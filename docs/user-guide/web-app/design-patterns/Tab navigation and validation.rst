Tab Validation During Navigation
=============================

Tabs component allows creating tabs for grouping different sets of components. To switch between tabs, there is a navigation bar with tab buttons, each of which opens an appropriate tab with a set group of components. Only one tab at a time displays in a rendered form. User can also use buttons to go next tab or previous tab. These buttons also show error message about required fields.

- Add tab component. Property name should be ``tabs``.

      .. figure:: ../../_assets/web-app/tab-navigation/tab.PNG
            :alt: tab
            :width: 80%
      
- Add navigation buttons for go to next or back tab.

      .. figure:: ../../_assets/web-app/tab-navigation/tab-navigate-buttons.PNG
            :alt: tab
            :width: 80%
      
- Next button event should be ``nextTab`` and back button event should be ``backTab``.

      .. figure:: ../../_assets/web-app/tab-navigation/nextTab-button.PNG
            :alt: tab
            :width: 70%
      
- On running analytics app. After clicking nextTab button, user will get required field error message.

      .. figure:: ../../_assets/web-app/tab-navigation/navigate-error.PNG
            :alt: tab
            :width: 80%
      
- Add button on last tab to navigate to next stage. Button event should be ``next``  and checked ``show validations``, if you want to validate whole form.

      .. figure:: ../../_assets/web-app/tab-navigation/nextStage-button.PNG
            :alt: tab
            :width: 75%
      
- Clicking on next stage button will check whole form validity and errors will show if any.

      .. figure:: ../../_assets/web-app/tab-navigation/showValidationonNext.PNG
            :alt: tab
            :width: 80%
      
      
