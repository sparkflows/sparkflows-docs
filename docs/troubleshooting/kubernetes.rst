Kubernetes
=======

This document contains details on troubleshooting Kubernetes.

1. Insufficient memory, Insufficient cpu. preemption: 0/4 nodes are available
-------------------------------------

**Problem**
++++++

Kubernetes is unable to schedule the Sparkflows pod due to unavailable resources requested for the container.

**Solution**
++++++

Check the available resources on the cluster nodes, using the below command.

::

    $ kubectl top node k8s-wrk01.abcorp.com
      NAME                              CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
      k8s-wrk01.abcorp.com               1555m        5%     50848Mi         44%

Based on the availability of the worker resources you can adjust the resource requested by the container as configured in the `deployment.yaml. <https://github.com/sparkflows/fire-tools/blob/main/kubernetes/deployment.yaml>`_

::

    ...
          resources:
            requests:
              memory: "8Gi"
              cpu: "4000m"
            limits:
              memory: "32Gi"
              cpu: "12000m"
    ...

.. note:: You can check version support from the official `Delta Documentation. <https://docs.delta.io/latest/releases.html>`_

     




