PyCaret AutoML Classification
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.pycaret.NodePyCaretAutoMLClassification

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - response_column
        - Target Column
        - The label column for model fitting
      * - include_algos
        - Include Algos
        - By default all algos will be selected, 'lr','knn','nb','dt','svm','rbfsvm','gpc','mlp','ridge', 'rf', 'qda','ada', 'gbc' ,'lda','et' ,'xgboost','lightgbm','catboost'
      * - top_n_model
        - Top N Models
        - Number of top_n models to select for leaderboard.
      * - imputation_type
        - Imputation Type
        - The type of imputation to use. Can be either 'simple' or 'iterative'.
      * - iterative_imputation_iters
        - Iterative Imputation Iters
        - Number of iterations. Ignored when imputation_typ is not 'iterative'.
      * - categorical_features
        - Categorical Features
        - It takes a list of strings with column names that are categorical.
      * - categorical_imputation
        - Categorical Imputation
        - Missing values in categorical features are imputed with a constant 'not_available'value. The other available option is 'mode'.
      * - categorical_iterative_imputer
        - Categorical Iterative Imputer
        - Estimator for iterative imputation of missing values in categorical features.
      * - high_cardinality_features
        - High Cardinality Features
        - When categorical features contains many levels, it can be compressed into fewer levels using this parameter. It takes a list of strings with column names that are categorical.
      * - high_cardinality_method
        - High Cardinality Method
        - Categorical features with high cardinality are replaced with the frequency ofvalues in each level occurring in the training dataset. Other available method is clustering which trains the K-Means clustering algorithm on the statistical attribute of the training data and replaces the original value of feature with the cluster label
      * - numeric_features
        - Numeric Features
        - If the inferred data types are not correct or the silent param is set to True, numeric_features param can be used to overwrite or define the data types.
      * - numeric_imputation
        - Numeric Imputation
        - Missing values in numeric features are imputed with 'mean' value of the feature in the training dataset. The other available option is 'median' or 'zero'.
      * - numeric_iterative_imputer
        - Numeric Iterative Imputer
        - Estimator for iterative imputation of missing values in numeric features.
      * - date_features
        - Date Features
        - If the inferred data types are not correct or the silent param is set to True, date_features param can be used to overwrite or define the data types. It takes a list of strings with column names that are DateTime.
      * - ignore_features
        - Ignore Features
        - ignore_features param can be used to ignore features during model training. It takes a list of strings with column names that are to be ignored.
      * - normalize
        - Normalize
        - When set to True, it transforms the numeric features by scaling them to a given range.
      * - normalize_method
        - Normalize Method
        - Defines the method for scaling.
      * - transformation
        - Transformation
        - When set to True, it transforms the numeric features by scaling them to a given range.
      * - transformation_method
        - Transformation Method
        - Defines the method for transformation.
      * - handle_unknown_categorical
        - Handle Unknown Categorical
        - When set to True, unknown categorical levels in unseen data are replaced by the most or least frequent level as learned in the training dataset. 
      * - unknown_categorical_method
        - Unknown Categorical Method
        - Method used to replace unknown categorical levels in unseen data.
      * - pca
        - PCA
        - When set to True, dimensionality reduction is applied to project the data into a lower dimensional space using the method defined in ``pca_method`` parameter.
      * - pca_method
        - PCA Method
        - Method used to replace unknown categorical levels in unseen data.
      * - ignore_low_variance
        - Ignore Low Variance
        - When set to True, all categorical features with insignificant variances are removed from the data.
      * - combine_rare_levels
        - Combine Rare Levels
        - When set to True, frequency percentile for levels in categorical features below a certain threshold is combined into a single level.
      * - rare_level_threshold
        - Rare Level Threshold
        - Percentile distribution below which rare categories are combined. Ignored when combine_rare_levels is not True.
      * - remove_outliers
        - Remove Outliers
        - When set to True, outliers from the training data are removed using the Singular Value Decomposition.
      * - outliers_threshold
        - Outliers Threshold
        - The percentage outliers to be removed from the training dataset. Ignored when  ``remove_outliers`` is not True.
      * - remove_multicollinearity
        - Remove Multicollinearity
        - When set to True, features with the inter-correlations higher than the defined threshold are removed. When two features are highly correlated with each other,  the feature that is less correlated with the target variable is removed. Only considers numeric features.
      * - multicollinearity_threshold
        - Multicollinearity Threshold
        - Threshold for correlated features. Ignored when ``remove_multicollinearity`` is not True.
      * - remove_perfect_collinearity
        - Remove Perfect Collinearity
        - When set to True, perfect collinearity (features with correlation = 1) is removed from the dataset, when two features are 100% correlated, one of it is randomly removed from the dataset.
      * - path
        - Path
        - Model Save Path.




