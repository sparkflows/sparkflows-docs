
MultiLayerPerceptron
========== 

It supports creation of full connected neural network.

Type
---------- 

ml-estimator

Class
---------- 

fire.nodes.ml.NodeMultilayerPerceptron

Fields
---------- 

+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| Name          | Title                                     | Description                                                               |
+===============+===========================================+===========================================================================+
| featuresCol   | Features Column                           | Features column of type vectorUDT for model fitting                       |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| labelCol      | Label Column                              | The label column for model fitting                                        |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| predictionCol | Prediction Columns                        | The prediction column created during model scoring.                       |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| layers        | Layers - comma separated list of integers | The integer array specifying the number of activation units in each layer |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| maxIter       | Max number of iterations                  | Number of iterations to train the Neural network                          |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| blockSize     | Block Size                                | Block size                                                                |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+
| seed          | Seed                                      | The initial seed to initialise the neural network.                        |
+---------------+-------------------------------------------+---------------------------------------------------------------------------+