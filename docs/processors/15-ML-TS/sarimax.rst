Sarimax
=========== 

Seasonal Autoregressive Integrated Moving Average, SARIMA or Seasonal ARIMA, is an extension of ARIMA that explicitly supports univariate time series data with a seasonal component.

Type
--------- 

ml-estimator

Class
--------- 

fire.nodes.ts.NodeStatsModelSarimax

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - index_column
        - Index ColumnName
        - name of the index column.
      * - endog_index_name_column_name
        - IndexesColumnName
        - example:1959:1981, consump
      * - exog_index_name_column_name
        - IndexsColumnName
        - example:1959:1981, m2
      * - order
        - Order
        - p,d,q values.P: Trend autoregression order, d: Trend difference order, q: Trend moving average order.
      * - seasonal_order
        - SeasonalOrder
        - P,D,Q,m values.P: Seasonal autoregressive order, D: Seasonal difference order, Q: Seasonal moving average order, m: The number of time steps for a single seasonal period.
      * - trend
        - Trend
        - 
      * - measurement_error
        - MeasurementError
        - 
      * - time_varying_regression
        - TimeVaryingRegression
        - 
      * - mle_regression
        - MleRegression
        - 
      * - simple_differencing
        - SimpleDifferencing
        - 
      * - enforce_stationarity
        - EnforceStationarity
        - 
      * - enforce_invertibility
        - EnforceInvertibility
        - 
      * - hamilton_representation
        - HamiltonRepresentation
        - 
      * - concentrate_scale
        - ConcentrateScale
        - 
      * - trend_offset
        - TrendOffset
        - 
      * - use_exact_diffuse
        - UseExactDiffuse
        - 
      * - fit
        - Fit
      * - transformed
        - Transformed
        - 
      * - includes_fixed
        - IncludesFixed
        - 
      * - cov_type
        - CovType
        - 
      * - method
        - Method
        - 
      * - maxiter
        - Maxiter
        - 
      * - full_output
        - FullOutput
        - 
      * - optim_score
        - OptimScore
        - The method by which the score vector is calculated. like harvey, approx
      * - optim_complex_step
        - OptimComplexStep
        - 
      * - optim_hessian
        - OptimHessian
        - The method by which the Hessian is numerically approximated. opg, oim & approx




