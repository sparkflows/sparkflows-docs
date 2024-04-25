Pre-requisites
=====

This document outlines the essential infrastructure prerequisites needed to run notebooks end-to-end from the Fire Insights UI.

- **Running Kubernetes Cluster**: Ensure that your Kubernetes cluster is operational and accessible from the Fire Insights application environment. Verify that all necessary components are up and running within the Kubernetes cluster.

- **Accessible Kubernetes Configuration Path**: Confirm that the Kubernetes configuration path is accessible from Fire Insights. This includes verifying the path to the Kubernetes configuration file (typically located at **~/.kube/config** or specified by the KUBECONFIG environment variable) and ensuring that Fire Insights has appropriate permissions to access this file. Test connectivity to the Kubernetes cluster using the configured path to ensure seamless integration with Fire Insights.
