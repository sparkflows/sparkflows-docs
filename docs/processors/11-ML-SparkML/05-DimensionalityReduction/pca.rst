PCA
=========== 

Trains a model to project vectors to a low-dimensional space using PCA.

Input
--------------
This takes in a DataFrame as input

Output
--------------
The output DataFrame is a projection of the vectors in the incoming DataFrame to a low-dimensional space using PCA

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodePCA

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - inputCol
        - Input Column
        - The input column name
      * - outputCol
        - Output Column
        - The output column name
      * - k
        - K
        - The number of principal components


Details
-------


Principal component analysis (PCA) is a statistical method to find a rotation such that the first coordinate has the largest variance possible, and each succeeding coordinate in turn has the largest variance possible. 
The columns of the rotation matrix are called principal components.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/2.0.0/mllib-dimensionality-reduction.html#principal-component-analysis-pca


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/mllib-dimensionality-reduction.html#principal-component-analysis-pca
+++++++++++++++

import org.apache.spark.mllib.linalg.Matrix
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.linalg.distributed.RowMatrix

val data = Array(
  Vectors.sparse(5, Seq((1, 1.0), (3, 7.0))),
  Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
  Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0))

val dataRDD = sc.parallelize(data, 2)

val mat: RowMatrix = new RowMatrix(dataRDD)

// Compute the top 4 principal components.
// Principal components are stored in a local dense matrix.
val pc: Matrix = mat.computePrincipalComponents(4)

// Project the rows to the linear space spanned by the top 4 principal components.
val projected: RowMatrix = mat.multiply(pc)
