Sparkflows Installation
=======================

Installation on Kubernetes
--------------------------

When installing Sparkflows on Kubernetes, do ensure that the Sparkflows Pod is configured with a PersistentVolume.

Otherwise, on restarting the POD, critical data would be lost.
