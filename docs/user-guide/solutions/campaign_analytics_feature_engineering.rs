Feature Engineering
===================

Sparkflows Feature Engineering Processors
^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Imputation:
Filling in missing data with statistical measures like mean, median, mode, or a constant value.

- Handling Outliers:
Identifying and managing extreme values which differ significantly from most of the data.

- Binning:
Grouping continuous variables into discrete bins or categories.

- Log Transform:
Applying logarithmic transformation to reduce the skewness of the variable distribution.

- One-Hot Encoding:
Converting categorical variables into a form that could be provided to machine learning algorithms.

- Label Encoding:
Converting each value in a categorical column into a number.

- Scaling:
Standardizing the range of independent variables or features of data.

- Normalization:
Adjusting values measured on different scales to a notionally common scale.

- Feature Split:
Splitting one feature into multiple features based on some logical or observed pattern.

- Date/Time Features:
Extracting parts of date-time like day, month, year, hour, minute, second, weekday, etc., and creating new features.

- Text Mining:
Deriving meaningful information from text sources and creating new features (e.g., TF-IDF, count vectorization).

- Polynomial Features:
Creating new features by considering non-linear relationships of the variables.

- Interaction Features:
Creating new features by combining two or more features.

- Aggregation:
Aggregating features at a higher level (e.g., customer level, daily level) by using statistical measures (mean, sum, max, min, etc.).

- Frequency Encoding:
Replacing categorical variables with the frequency of each category.

- Target Encoding:
Replacing a categorical value with the mean of the target variable for that value.

.. figure:: ../../../_assets/tutorials/solutions/campaign_analytics/campaign_analytics_feature_engineering_v1.png
   :alt: Feature Engineering
   :width: 75%

