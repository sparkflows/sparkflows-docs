ARIMA
=========== 

AutoARIMA

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
      * - start_p
        - start_p
        - The starting value of p, the order (or number of time lags) of the auto-regressive (“AR”) model. Must be a positive integer.
      * - d
        - d
        - The order of first-differencing. If None (by default), the value will automatically be selected based on the results of the test.
      * - start_q
        - start_q
        - The starting value of q, the order of the moving-average (“MA”) model. Must be a positive integer.
      * - max_p
        - max_p
        - The maximum value of p, inclusive. Must be a positive integer greater than or equal to start_p.
      * - max_d
        - max_d
        - The maximum value of d, or the maximum number of non-seasonal differences. Must be a positive integer greater than or equal to d.
      * - max_q
        - max_q
        - The maximum value of q, inclusive. Must be a positive integer greater than start_q.
      * - start_P
        - start_P
        - The starting value of P, the order of the auto-regressive portion of the seasonal model.
      * - D
        - D
        - The order of the seasonal differencing. If None (by default, the value will automatically be selected based on the results of the seasonal_test. Must be a positive integer or None.
      * - start_Q
        - start_Q
        - The starting value of Q, the order of the moving-average portion of the seasonal model.
      * - max_P
        - max_P
        - The maximum value of P, inclusive. Must be a positive integer greater than start_P.
      * - max_D
        - max_D
        - The maximum value of D. Must be a positive integer greater than D.
      * - max_Q
        - max_Q
        - The maximum value of Q, inclusive. Must be a positive integer greater than start_Q.
      * - max_order
        - max_order
        - If the sum of p and q is >= max_order, a model will not be fit with those parameters, but will progress to the next combination. Default is 5. If max_order is None, it means there are no constraints on maximum order.
      * - m
        - m
        - The period for seasonal differencing, m refers to the number of periods in each season.
      * - information_criterion
        - Information Criterion
        - The information criterion used to select the best ARIMA model.
      * - stationary
        - stationary
        - Whether the time-series is stationary and d should be set to zero.
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




