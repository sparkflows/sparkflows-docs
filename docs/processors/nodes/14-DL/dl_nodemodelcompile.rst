Keras Model Compile
=========== 



Type
--------- 

transform

Class
--------- 

fire.nodes.dl.NodeModelCompile

Fields
--------- 

.. list-table::
      :widths: 10 5 10
      :header-rows: 1

      * - Name
        - Title
        - Description
      * - optimizer
        - Optimizer
        - name of optimizer
      * - loss
        - Loss
        - String (name of objective function), objective function or `tf.losses.Loss` instance
      * - metrics
        - Metrics
        - List of metrics to be evaluated by the model during trainin and testing
      * - loss_weights
        - LossWeights
        - Optional list or dictionary specifying scalar coefficients (Python floats) to weight the loss contributions of different model outputs.
      * - sample_weight_mode
        - SampleWeightMode
        - 
      * - weighted_metrics
        - WeightedMetrics
        - List of metrics to be evaluated and weighted by sample_weight or class_weight during training and testing.
      * - target_tensors
        - TargetTensors
        - 




