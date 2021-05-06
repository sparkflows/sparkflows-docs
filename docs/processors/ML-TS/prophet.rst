Prophet
=========== 



Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ts.NodeProphet

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - ds
        - DS Column
        - Date or DateTime variable
      * - y
        - Y
        - Target Variable
      * - growth
        - Growth
        - linear or logistic to specify a linear or logistic trend
      * - yearly_seasonality
        - Yearly Seasonality
        - Fit yearly seasonality.
      * - weekly_seasonality
        - Weekly Seasonality
        - Fit weekly seasonality.
      * - daily_seasonality
        - Daily Seasonality
        - Fit daily seasonality.
      * - seasonality_mode
        - Seasonality Mode
        - additive(default) or multiplicative
      * - interval_width
        - Interval Width
        - Float, width of the uncertainty intervals provided for the forecast
      * - future Data
        - Future Data
      * - future_period
        - Future Period
        - Int number of periods to forecast forward.
      * - frequency
        - frequency
        - Any valid frequency for pd.date_range, such as 'D' or 'M'.
      * - include_history
        - Include History
        - Boolean to include the historical dates in the dataframe for predictions




