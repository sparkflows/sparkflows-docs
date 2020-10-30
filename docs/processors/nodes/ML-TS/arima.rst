ARIMA
=========== 



Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ts.NodeAutoARIMA

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - y
        - Y
        - The time-series to which to fit the ARIMA estimator
      * - seasonal
        - Seasonal
        - Whether to fit a seasonal ARIMA. Default is True
      * - stepwise
        - Stepwise
        - Whether to use the stepwise algorithm to identify the optimal model parameters. 
      * - trace
        - Trace
        - Whether to print status on the fits.
      * - suppress_warnings
        - Suppress Warnings
        - If suppress_warnings is True, all of the warnings coming from ARIMA will be squelched.
      * - error_action
        - Error Action
        - If unable to fit an ARIMA for whatever reason, this controls the error-handling behavior. One of (warn, raise, ignore)
      * - scoring
        - Scoring
        - The metric to use for scoring the out-of-sample data. One of (mse, mae)
      * - n_periods
        - Forecast
        - Int number of periods to forecast forward.




