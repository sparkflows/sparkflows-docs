Hashing TF
=========== 

Maps a sequence of terms to term frequencies using the hashing trick.

Input
--------------
It takes in a DataFrame as input and transforms it to another DataFrame

Output
--------------
A new column is added to the input DataFrame containing hashing of the bag of words into a feature vector

Type
--------- 

ml-transformer

Class
--------- 

fire.nodes.ml.NodeHashingTF

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
        - Contains sets of terms. In text processing, a 'set of terms' might be a bag of words
      * - outputCol
        - Output Column
        - Output column name


Details
-------


Term frequency-inverse document frequency (TF-IDF) is a feature vectorization method widely used in text mining to reflect the importance of a term to a document in the corpus. 
Denote a term by t, a document by d, and the corpus by D. Term frequency TF(t,d) is the number of times that term t appears in document d, while document frequency DF(t,D) is the number of documents that contains term t.
If we only use term frequency to measure the importance, it is very easy to over-emphasize terms that appear very often but carry little information about the document, e.g., “a”, “the”, and “of”. If a term appears very often across the corpus, it means it doesn’t carry special information about a particular document.

More at Spark MLlib/ML docs page : https://spark.apache.org/docs/3.2.1/mllib-feature-extraction.html#tf-idf


Examples
-------


The below example is available at : https://spark.apache.org/docs/3.2.1/mllib-feature-extraction.html#tf-idf
+++++++++++++++

import org.apache.spark.mllib.feature.{HashingTF, IDF}
import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.rdd.RDD

// Load documents (one per line).
val documents: RDD[Seq[String]] = sc.textFile("data/mllib/kmeans_data.txt")
  .map(_.split(" ").toSeq)

val hashingTF = new HashingTF()
val tf: RDD[Vector] = hashingTF.transform(documents)

// While applying HashingTF only needs a single pass to the data, applying IDF needs two passes:
// First to compute the IDF vector and second to scale the term frequencies by IDF.
tf.cache()
val idf = new IDF().fit(tf)
val tfidf: RDD[Vector] = idf.transform(tf)

// spark.mllib IDF implementation provides an option for ignoring terms which occur in less than
// a minimum number of documents. In such cases, the IDF for these terms is set to 0.
// This feature can be used by passing the minDocFreq value to the IDF constructor.
val idfIgnore = new IDF(minDocFreq = 2).fit(tf)
val tfidfIgnore: RDD[Vector] = idfIgnore.transform(tf)
