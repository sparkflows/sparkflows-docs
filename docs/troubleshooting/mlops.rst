MLOps 
=================
This document explains some of the common issues and corresponding resolutions related to MLOps.

1. Deployment Error: 'TypeError' with 6 Arguments Given
-------------------

**Problem**
+++++++++

Getting Exception : 'TypeError: _send_request() takes 5 positional arguments but 6 were given` when trying to deploy the model.

**Solution**
++++++++

Upgrade boto3 on Sparkflows machine and the MLflow machine: ::

 pip install --upgrade boto3

