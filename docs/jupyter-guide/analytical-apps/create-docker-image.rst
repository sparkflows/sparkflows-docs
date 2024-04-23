Create Docker image with user created notebook
================

Build the image with notebooks, data and required dependencies.

Docker details `Dockerfile and other details <https://github.com/sparkflows/fire-tools/tree/main/jupyter-docker>`_ to get more details.

Below are the Docker Command being used to build image and push to Docker hub which will be accessible to pull image:

::

    build: docker build -t username/repo:tagname .
    push: docker push username/repo:tagname


.. note:: Make sure to ``username/repo`` & ``tagname`` with actual name and make note of image name, which would be used in next steps while creating Jupyter connection in Sparkflows.
