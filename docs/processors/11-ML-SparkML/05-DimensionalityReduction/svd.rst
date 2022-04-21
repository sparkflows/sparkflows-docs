SVD
=========== 

Type
--------- 

transform

Class
--------- 

fire.nodes.ml.NodeSVD

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - columnName
        - Column Name
      * - k
        - k


Details
-------


Singular value decomposition (SVD) factorizes a matrix into three matrices: U, Σ, and V such that

A=UΣVT,

where

U is an orthonormal matrix, whose columns are called left singular vectors,
Σ is a diagonal matrix with non-negative diagonals in descending order, whose diagonals are called singular values,
V is an orthonormal matrix, whose columns are called right singular vectors

More details are available at: https://spark.apache.org/docs/2.0.0/mllib-dimensionality-reduction.html#singular-value-decomposition-svd


Examples
-------


The below example is available at : https://spark.apache.org/docs/2.0.0/mllib-dimensionality-reduction.html#singular-value-decomposition-svd
+++++++++++++++

import org.apache.spark.mllib.linalg.Matrix
import org.apache.spark.mllib.linalg.SingularValueDecomposition
import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.mllib.linalg.distributed.RowMatrix

val data = Array(
  Vectors.sparse(5, Seq((1, 1.0), (3, 7.0))),
  Vectors.dense(2.0, 0.0, 3.0, 4.0, 5.0),
  Vectors.dense(4.0, 0.0, 0.0, 6.0, 7.0))

val dataRDD = sc.parallelize(data, 2)

val mat: RowMatrix = new RowMatrix(dataRDD)

// Compute the top 5 singular values and corresponding singular vectors.
val svd: SingularValueDecomposition[RowMatrix, Matrix] = mat.computeSVD(5, computeU = true)
val U: RowMatrix = svd.U  // The U factor is a RowMatrix.
val s: Vector = svd.s  // The singular values are stored in a local dense vector.
val V: Matrix = svd.V  // The V factor is a local dense matrix.
