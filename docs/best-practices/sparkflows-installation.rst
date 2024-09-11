Sparkflows Installation
=======================

Installation on Kubernetes
--------------------------

**1. Persistent Storage**

- **Use Persistent Volume Claims (PVC)**: When installing Sparkflows, ensure that you make use of PVCs to manage storage which ensures that data persists even if the pod restarts. You can find an example of a PVC in our documentation here: https://docs.sparkflows.io/en/latest/aws/admin-guide/aws-eks/deployment.html#step-1-create-a-persistent-volume

**2. Pod Affinity and Anti-affinity**

- **Distribute workloads intelligently:** Use pod affinity and anti-affinity rules to control how pods are placed across nodes to achieve better resource utilization and fault tolerance.

- **Avoid single points of failure:** Ensure that your pods are spread across different nodes, regions, or availability zones to prevent a single failure from affecting your entire application.

**3. Resource Requests and Limits**

- **Set resource requests and limits:** Define CPU and memory requests and limits for each pod to ensure efficient resource allocation and prevent overloading nodes. Here's an example deployement manifest having resource requests and limits: https://docs.sparkflows.io/en/latest/aws/admin-guide/aws-eks/deployment.html#step-2-create-sparkflows-service-deployment

**4. Namespace Management**

- **Use namespaces to separate environments:** Organize resources by using namespaces for different environments (e.g., development, staging, production) to avoid conflicts and manage resource allocation.

**5. ConfigMaps and Secrets Management**

- **Store configuration in ConfigMaps:** Keep your application’s configuration outside of the container image in ConfigMaps, allowing for easier updates without rebuilding images.

- **Use Secrets for sensitive data:** Store sensitive information like API keys, passwords, or certificates in Secrets. Use encryption for added security.

