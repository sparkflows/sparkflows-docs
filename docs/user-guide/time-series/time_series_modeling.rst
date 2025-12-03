Time Series Modeling
--------------------
Time series modeling is the process of using statistical and machine learning methods to analyze and forecast future values of a time series. Time series data has a temporal ordering, meaning that the data points are ordered by time, this allows to capture patterns and dependencies between observations that happen over time.

Sparkflows provides a number of cutting edge algoirthms as Processors for Time Series Modeling. These include:

.. list-table::
   :widths: 10 40
   :header-rows: 1

   * - Models
     - Description
   * - Prophet
     - Prophet is a procedure for forecasting time series data based on an additive model where non-linear trends are fit with yearly, weekly, and daily seasonality, plus holiday effects. It works best with time series that have strong seasonal effects and several seasons of historical data. Prophet is robust to missing data and shifts in the trend, and typically handles outliers well. More details can be found at: https://facebook.github.io/prophet/

   * - ARIMA
     - ARIMA is a model used for predicting future trends on a time series data. The Sparkflows integrates the python wrapper of R's best package `auto.arima`. One can use Sparkflows processors to model univariate as well as multivaraite data. The Sparkflows porcessors can figure out the hyper-parameters via grid search to give the user best values of (p,q,d,P,Q,D) based on optimizing for AIC/BIC. This reduces the overhead of the user to manually find these parameteres which at time can be challenging. More details can be found at: https://alkaline-ml.com/pmdarima/about.html#about

   * - SARIMAX
     - SARIMAX is a statistical model for time series data that combines the strengths of the Seasonal AutoRegressive Integrated Moving Average (SARIMA) model and the eXogenous (X) factor model. It is commonly used to model time series data that exhibits both seasonality and autoregressive dependencies. The SARIMAX model is particularly useful for forecasting future values in a time series, as it can account for both the past values in the series and the periodic patterns that may exist.The SARIMAX model is an extension of the ARIMA model, which is used to model time series data that exhibit autoregressive dependencies. Sparkflows integrates with the state of art SARIMAX library available in statsmodels package. SARIMAX can be used to build models on univariate as well as multivaraite data. More details can be found at: https://www.statsmodels.org/dev/generated/statsmodels.tsa.statespace.sarimax.SARIMAX.html#statsmodels.tsa.statespace.sarimax.SARIMAX

   * - VAR
     - VAR, or Vector Autoregression, is a statistical model used to describe the linear interdependence between multiple time series. It is a multivariate extension of the univariate autoregressive model, and can be used to analyze the dynamic relationships between multiple variables over time. VAR models are widely used in economics, finance, and other fields. Sparkflows integrates with the state of art VAR library available in statsmodels package. More details can be found at: https://www.statsmodels.org/dev/vector_ar.html
     
   * - XGBoost
     - XGBoost is gradient boosting algorithm which can be used to model time series data after computing features like lags, moving averages, time based features among others. It is also known as regularized boosting technique - seeks a goot bias-variant trade-off to reduce overfitting allows cross-validation at each iteration of the boosting process and thus, it is easy to get the exact optimum number of boosting iterations in a single run. More details can be found at:  https://xgboost.readthedocs.io/en/stable/


   * - LSTM
     - Long Short-Term Memory (LSTM) is a type of recurrent neural network (RNN) that is trained using Backpropagation Through Time (BPTT) and can learn long-term dependencies. LSTM networks are well-suited to classifying, processing and making predictions based on time series data, since there can be lags of unknown duration between important events in a time series. LSTMs are composed of a cell, input gate, forget gate, and output gate. The cell remembers values over arbitrary time intervals and the three gates regulate the flow of information into and out of the cell. They are particularly useful for tasks that require the network to remember and use information from long periods of time in the past. More details can be found at:  https://www.tensorflow.org/tutorials/structured_data/time_series

Prophet
=======

Below is the sample workflow which uses Prophet processor in Sparkflows.

The workflow reads the AirPassengers dataset & uses Prophet processor for forecasting of univariate time series data and finally prints the result.


   .. figure:: ../../_assets/ml_userguide/fbprophet.png
      :alt: ml_userguide
      :width: 65%


Prophet processor Configuration:

   .. figure:: ../../_assets/ml_userguide/fbprophet_processor.PNG
      :alt: ml_userguide
      :width: 65%
   
   .. figure:: ../../_assets/ml_userguide/fbprophet_processor2.PNG
      :alt: ml_userguide
      :width: 65%


Results from ``Prophet`` model after training the model:  

   .. figure:: ../../_assets/ml_userguide/fbprophet_result.png
      :alt: ml_userguide
      :width: 65%

ARIMA
=====

Below is the sample workflow which uses ARIMA processor in Sparkflows.

The workflow reads the AirPassengers dataset & uses ARIMA processor which Forecasts the airline passengers count, generates a new column with unique index/value for each row in dataset and prints the result.

   .. figure:: ../../_assets/ml_userguide/arima_wf.png
      :alt: ml_userguide
      :width: 65%
   
ARIMA processor Configuration:

   .. figure:: ../../_assets/ml_userguide/arima_configuration.PNG
      :alt: ml_userguide
      :width: 65%
   
Result from ``ARIMA`` model after training the model:     

   .. figure:: ../../_assets/ml_userguide/arima_result.PNG
      :alt: ml_userguide
      :width: 65%


H2OXGBoost
==========

Below is the sample workflow which uses H2OXGBoost processor in Sparkflows.

The workflow reads the UCI Credit Card dataset & uses H2OXGBoost processor which is a supervised learning algorithm on tabular data and save the model in S3 location. Rich features like lag, moving average among others can be computed and added to the baseline model.

   .. figure:: ../../_assets/ml_userguide/xgBoost.PNG
      :alt: ml_userguide
      :width: 65%

H2OXGBoost processor Configuration:

   .. figure:: ../../_assets/ml_userguide/xgBoost_config.PNG
      :alt: ml_userguide
      :width: 65%

H2OMojoSave processor Configuration:

   .. figure:: ../../_assets/ml_userguide/h2o_ml.PNG
      :alt: ml_userguide
      :width: 65%

On successful completion of the job, the model gets saved to specified locations. You can view the model at the specified location.

   .. figure:: ../../_assets/ml_userguide/h2o_output.png
      :alt: ml_userguide
      :width: 65%

   .. figure:: ../../_assets/ml_userguide/modellocation.PNG
      :alt: ml_userguide
      :width: 65%


