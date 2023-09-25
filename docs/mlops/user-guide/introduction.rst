Introduction
======

Sparkflows saves all the models trained in its model repository by default. It also captures all the training and validation metrics. The model artifacts are saved on disk or in blob storage by Sparkflows.

These models can be served as one of the two options:

#. **Offline Model Serving**
    
    * Usually used for batch scoring
    * Used for bulk prediction
    * Has high throughput

#. **Online Model Serving**
    
    * Usually used for scoring streaming data 
    * Has Low latency
    * Involves Real time model serving
    * Used to score relatively smaller number of rows of data





