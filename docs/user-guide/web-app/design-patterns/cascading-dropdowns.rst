Cascading Dropdowns
===========
Fire enables you to create cascading dropdowns in analytical app using javascript code in select component. It involves a hierarchical relationship between two or more dropdown (or select) fields, where the options in a second dropdown are determined by the selection made in the first dropdown, and so on.

Follow the steps given below to enable cascading dropdowns in your analytical apps.

Step 1 : Add and Configure Select Component
-------------

#. Open **Edit analytics app** page.
#. Expand the **General** tab and add **Select** component using drag-and-drop method.

   **Note :** In our example, this component is used to select the country.
#. In the Select component window, open **Data** tab to :
   
   * Select **DATA SOURCE TYPE** as **Raw JSON**.
   * Add the below JSON in the **DATA SOURCE RAW JSON** box : 

      ::

        [
            {
              "id": "'India'",
              "label": "'India'",
              "state": [
                {
                  "id": "'Maharashtra'",
                  "label": "'Maharashtra'",
                  "city": [
                    "'Mumbai'",
                    "'Nagpur'"
                  ]
                },
                {
                  "id": "'Karnataka'",
                  "label": "'Karnataka'",
                  "city": [
                    "'Bengaluru'"
                  ]
                }
              ]
            },
            {
              "id": "'USA'",
              "label": "'USA'",
              "state": [
                {
                  "id": "'California'",
                  "label": "'California'",
                  "city": [
                    "'California City'",
                    "'Los Angeles'"
                  ]
                },
                {
                  "id": "'New York'",
                  "label": "'New York'",
                  "city": [
                    "'New York City'"
                  ]
                }
              ]
            }
          ]                                                                                                                                                                              

   * Click on **Save** to save the settings.

      .. figure:: ../../../_assets/web-app/cascading-dropdowns/select-settings.png
         :alt: cascading dropdowns
         :width: 65%

Step 2 : Add and Configure 2nd Select Component
--------------

#. Add second select component using drag-and-drop method.
   
   **Note :** In this component state data will come depending upon selected country in the first select component.
#. In the Select component window, open **Data** tab to :

   * Select **DATA SOURCE TYPE** as **Raw JSON**. 
   * Click on the **Calculated Value** option and add the below javascript logic in **JavaScript** box : 

      ::

          component.clearOnRefresh = true
          component.redrawOn = 'selectCountry'
          if(data.selectCountry && data.selectCountry.length > 0 && data.selectCountry[0].state){
          var stateList = [];
          var labels = "";
          for(var i =0 ;i < data.selectCountry.length;i++) {
          let state = data.selectCountry[i].state
          stateList = i==0 ? state:stateList.concat(state);
          labels = i==0 ? data.selectCountry[i].label : labels+ ","+ data.selectCountry[i].label;
          }
          component.data.json = stateList;
          data.selectCountry = labels;
          }else if(data.selectCountry && data.selectCountry.state){
          component.data.json = data.selectCountry.state.sort((a, b) => a.label.toLowerCase() < b.label.toLowerCase() ? -1 : 1)
          data.selectCountry = data.selectCountry.label
          }

      
     **Note :** selectState is API property name of the above component.

   * Click on **Save** to save the settings.

      .. figure:: ../../../_assets/web-app/cascading-dropdowns/javascript-logic-1.png
         :alt: cascading dropdowns
         :width: 65%

Step 3 : Add and Configure Another Select Component
------------

#. Add second select component using drag-and-drop method.
   
   **Note :** In this component city data will come depending upon selected state in the second select component.
#. In the Select component window, open **Data** tab to :

   * Select **DATA SOURCE TYPE** as **Raw JSON**. 
   * Click on the **Calculated Value** option and add the below javascript logic in **JavaScript** box : 

      ::

              component.clearOnRefresh = true
              component.redrawOn = 'selectState'
              if(data.selectState && data.selectState.length > 0 && data.selectState[0].city){
              var cityList = [];
              var labels = "";
              for(var i =0 ;i < data.selectState.length;i++) {
              let city = data.selectState[i].city
              cityList = i==0 ? city:cityList.concat(city);
              labels = i==0 ? data.selectState[i].label :labels+ ","+ data.selectState[i].label;
              }
              component.data.json = cityList;
              data.selectState = labels;
              }else if(data.selectState && data.selectState.city){
              component.data.json = data.selectState.city
              data.selectState = data.selectState.label
              }

            

     **Note :** selectState is API property name of the above component.

   * Click on **Save** to save the settings.
     
      .. figure:: ../../../_assets/web-app/cascading-dropdowns/javascript-logic-2.png
         :alt: cascading dropdowns
         :width: 65%






