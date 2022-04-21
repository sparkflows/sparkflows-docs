Sklearn Polynomial
=========== 

Polynomial regression is a special case of linear regression, where generate a new feature matrix consisting of all polynomial combinations of the features with degree less than or equal to the specified degree.

Type
--------- 

transform

Class
--------- 

fire.nodes.sklearn.NodeSklearnPolynomial

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - targetCol
        - Target Column
        - The label column for model fitting
      * - degree
        - Degree
        - The degree of the polynomial features. Default = 2.
      * - interactiononly
        - Interaction Only
        - If true, only interaction features are produced: features that are products of at most ``degree`` *distinct* input features (so not``x[1] ** 2``, ``x[0] * x[2] ** 3``, etc.)
      * - includebias
        - Include Bias
        - True (default), then include a bias column, the feature in which all polynomial powers are zero.




