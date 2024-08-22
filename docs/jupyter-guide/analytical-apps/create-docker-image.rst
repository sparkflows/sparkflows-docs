Create Docker image with the Jupyter notebook 
================

Create a Docker image containing user-created notebooks, data, and required dependencies.

Refer to the `Dockerfile and other details <https://github.com/sparkflows/fire-tools/tree/main/jupyter-docker>`_ to get more details.

Below are the Docker commands used to build the image and push it to Docker Hub, making it accessible for pulling:
::

    Docker Build command - docker build -t username/repo:tagname 

    Docker Push command - docker push username/repo:tagname


.. note:: Ensure that you replace **username/repo** and **tagname** with the actual names. Take note of the image name, which will be used in the next steps when creating a Jupyter connection in Fire Insights.
