
Word2Vec
^^^^^^ 

Transforms vectors of words into vectors of numeric codes for the purpose of further processing by NLP or machine learning algorithms.

type

ml-transformer

nodeClass

fire.nodes.ml.NodeWord2Vec

Fields

+----------------------+-------------------+-----------------------------------------+
| Name                 | Title             | Description                             |
+======================+===================+=========================================+
| inputCol             | Input Column      | Contains sequences of words             |
+----------------------+-------------------+-----------------------------------------+
| inputColStringArrCol | Text Array Column | The text array column which is produced |
+----------------------+-------------------+-----------------------------------------+
| outputCol            | Output Column     | Output column name                      |
+----------------------+-------------------+-----------------------------------------+
| vectorSize           | Vector Size       | Vector Size                             |
+----------------------+-------------------+-----------------------------------------+
| minCount             | Min Count         | Min Count                               |
+----------------------+-------------------+-----------------------------------------+