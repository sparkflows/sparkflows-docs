Installing Fire Insights with Rancher
==========================

This document captures the steps for installing Fire Insights.

Below are the steps:

 * Install Rancher with RKE
 * Install Minio
 * Install Apache Spark
 * Install Apache HIVE
 * Install Jupyter
 * Install Fire Insights
  
Linux OS requirements for Rancher
--------------

RKE runs on almost any Linux OS with Docker installed.

* Each node in the RKE cluster must have SSH user, that is part of the docker group.
* Swap should be disabled on any worker nodes
- Following sysctl settings must be applied::

   net.bridge.bridge-nf-call-iptables=1  
  
  
Install RKE and Rancher
--------------

Below are the steps for installing Rancher Kubernetes Edition (RKE) and Rancher ( Cluster Manager )

* Install docker on all the nodes using the below rancher script for docker::

   curl https://releases.rancher.com/install-docker/20.10.sh | sh

* You will need to edit(or create) **/etc/docker/daemon.json** to include the following::
   
   cat <<EOF | sudo tee /etc/docker/daemon.json
   {
    "group": "docker"
   }
   EOF
   
* Restart the docker daemon with the above changes::
   
   sudo systemctl restart docker
   
* Add the SSH user to the docker group, this can't be the root user::

   usermod -aG docker <user_name>
  
* To verify that the user is configured , log out of the node and login with your SSH user::

   ssh <user_name>@node
   $ docker ps
   CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS
 
* Before installing the RKE, make sure you have configured the Outbound and inbound rules for all the nodes in the cluster, as per the Rancher [docs](https://rancher.com/docs/rke/latest/en/os/#ports)

* Your SSH server system-wide configuration file, located at **/etc/ssh/sshd_config**, must include this line that allows TCP forwarding::

   AllowTcpForwarding yes
   
* Download the RKE binary from the github [release](https://github.com/rancher/rke/#latest-release) page, copy the binary to a folder in $PATH , make it executable and rename it to **rke**.
* Confirm that RKE is now executable by running the following command::

   $ rke --version
   
* RKE uses a cluster configuration file, referred to as **cluster.yml** to determine what nodes will be in the cluster and how to deploy Kubernetes. In this example we will be creating 4 node cluster. Below is the cluster.yml that will be used
.. code-block:: yml

   nodes:
     - address: <ip-addr-1>
       port: "22"
       internal_address: ""
       role:
         - controlplane
         - worker
         - etcd
       hostname_override: "n1.k8s"
       user: sparkflows
       docker_socket: /var/run/docker.sock
       ssh_key: ""
       ssh_key_path: ~/.ssh/key.pem
       ssh_cert: ""
       ssh_cert_path: ""
       labels: {}
       taints: []
     - address: <ip-addr-2>
       port: "22"
       internal_address: ""
       role:
         - worker
       hostname_override: "n2.k8s"
       user: sparkflows
       docker_socket: /var/run/docker.sock
       ssh_key: ""
       ssh_key_path: ~/.ssh/key.pem
       ssh_cert: ""
       ssh_cert_path: ""
       labels: {}
       taints: []
     - address: <ip-addr-3>
       port: "22"
       internal_address: ""
       role:
         - worker
       hostname_override: "n3.k8s"
       user: sparkflows
       docker_socket: /var/run/docker.sock
       ssh_key: ""
       ssh_key_path: ~/.ssh/key.pem
       ssh_cert: ""
       ssh_cert_path: ""
       labels: {}
       taints: []
     - address: <ip-addr-4>
       port: "22"
       internal_address: ""
       role:
        - worker
       hostname_override: "n4.k8s"
       user: sparkflows
       docker_socket: /var/run/docker.sock
       ssh_key: ""
       ssh_key_path: ~/.ssh/key.pem
       ssh_cert: ""
       ssh_cert_path: ""
       labels: {}
       taints: []
   services:
     etcd:
       image: ""
       extra_args: {}
       extra_binds: []
       extra_env: []
       win_extra_args: {}
       win_extra_binds: []
       win_extra_env: []
       external_urls: []
       ca_cert: ""
       cert: ""
       key: ""
       path: ""
       uid: 0
       gid: 0
       snapshot: null
       retention: ""
       creation: ""
       backup_config: null
     kube-api:
       image: ""
       extra_args: {}
       extra_binds: []
       extra_env: []
       win_extra_args: {}
       win_extra_binds: []
       win_extra_env: []
       service_cluster_ip_range: 10.43.0.0/16
       service_node_port_range: ""
       pod_security_policy: false
       always_pull_images: false
       secrets_encryption_config: null
       audit_log: null
       admission_configuration: null
       event_rate_limit: null
     kube-controller:
       image: ""
       extra_args:
         cluster-signing-cert-file: "/etc/kubernetes/ssl/kube-ca.pem"
         cluster-signing-key-file: "/etc/kubernetes/ssl/kube-ca-key.pem"
       extra_binds: []
       extra_env: []
       win_extra_args: {}
       win_extra_binds: []
       win_extra_env: []
       cluster_cidr: 10.42.0.0/16
       service_cluster_ip_range: 10.43.0.0/16
     scheduler:
       image: ""
       extra_args: {}
       extra_binds: []
       extra_env: []
       win_extra_args: {}
       win_extra_binds: []
       win_extra_env: []
     kubelet:
       image: ""
       extra_args: {}
       extra_binds:
         - "/mnt:/mnt"
       extra_env: []
       win_extra_args: {}
       win_extra_binds: []
       win_extra_env: []
       cluster_domain: cluster.local
       infra_container_image: ""
       cluster_dns_server: 10.43.0.10
       fail_swap_on: false
       generate_serving_certificate: false
     kubeproxy:
       image: ""
       extra_args: {}
       extra_binds: []
       extra_env: []
       win_extra_args: {}
       win_extra_binds: []
       win_extra_env: []
   network:
     plugin: canal
     options: {}
     mtu: 0
     node_selector: {}
     update_strategy: null
     tolerations: []
   authentication:
     strategy: x509
     sans: []
     webhook: null
   addons: ""
   addons_include: []
   system_images:
     etcd: rancher/mirrored-coreos-etcd:v3.4.15-rancher1
     alpine: rancher/rke-tools:v0.1.78
     nginx_proxy: rancher/rke-tools:v0.1.78
     cert_downloader: rancher/rke-tools:v0.1.78
     kubernetes_services_sidecar: rancher/rke-tools:v0.1.78
     kubedns: rancher/mirrored-k8s-dns-kube-dns:1.15.10
     dnsmasq: rancher/mirrored-k8s-dns-dnsmasq-nanny:1.15.10
     kubedns_sidecar: rancher/mirrored-k8s-dns-sidecar:1.15.10
     kubedns_autoscaler: rancher/mirrored-cluster-proportional-autoscaler:1.8.1
     coredns: rancher/mirrored-coredns-coredns:1.8.0
     coredns_autoscaler: rancher/mirrored-cluster-proportional-autoscaler:1.8.1
     nodelocal: rancher/mirrored-k8s-dns-node-cache:1.15.13
     kubernetes: rancher/hyperkube:v1.20.10-rancher1
     flannel: rancher/mirrored-coreos-flannel:v0.13.0
     flannel_cni: rancher/flannel-cni:v0.3.0-rancher6
     calico_node: rancher/mirrored-calico-node:v3.17.2
     calico_cni: rancher/mirrored-calico-cni:v3.17.2
     calico_controllers: rancher/mirrored-calico-kube-controllers:v3.17.2
     calico_ctl: rancher/mirrored-calico-ctl:v3.17.2
     calico_flexvol: rancher/mirrored-calico-pod2daemon-flexvol:v3.17.2
     canal_node: rancher/mirrored-calico-node:v3.17.2
     canal_cni: rancher/mirrored-calico-cni:v3.17.2
     canal_controllers: rancher/mirrored-calico-kube-controllers:v3.17.2
     canal_flannel: rancher/coreos-flannel:v0.13.0-rancher1
     canal_flexvol: rancher/mirrored-calico-pod2daemon-flexvol:v3.17.2
     weave_node: weaveworks/weave-kube:2.8.1
     weave_cni: weaveworks/weave-npc:2.8.1
     pod_infra_container: rancher/mirrored-pause:3.2
     ingress: rancher/nginx-ingress-controller:nginx-0.43.0-rancher3
     ingress_backend: rancher/mirrored-nginx-ingress-controller-defaultbackend:1.5-rancher1
     metrics_server: rancher/mirrored-metrics-server:v0.4.1
     windows_pod_infra_container: rancher/kubelet-pause:v0.1.6
     aci_cni_deploy_container: noiro/cnideploy:5.1.1.0.1ae238a
     aci_host_container: noiro/aci-containers-host:5.1.1.0.1ae238a
     aci_opflex_container: noiro/opflex:5.1.1.0.1ae238a
     aci_mcast_container: noiro/opflex:5.1.1.0.1ae238a
     aci_ovs_container: noiro/openvswitch:5.1.1.0.1ae238a
     aci_controller_container: noiro/aci-containers-controller:5.1.1.0.1ae238a
     aci_gbp_server_container: noiro/gbp-server:5.1.1.0.1ae238a
     aci_opflex_server_container: noiro/opflex-server:5.1.1.0.1ae238a
   ssh_key_path: ~/.ssh/id_rsa
   ssh_cert_path: ""
   ssh_agent_auth: false
   authorization:
     mode: rbac
    options: {}
   ignore_docker_version: null
   kubernetes_version: ""
   private_registries: []
   ingress:
     provider: "nginx"
     options:
       use-forwarded-headers: 'true'
     node_selector: {}
     extra_args: {}
     dns_policy: ""
     extra_envs: []
     extra_volumes: []
     extra_volume_mounts: []
     update_strategy: null
     http_port: 0
     https_port: 0
     network_mode: ""
     tolerations: []
     default_backend: null
     default_http_backend_priority_class_name: ""
     nginx_ingress_controller_priority_class_name: ""
   cluster_name: ""
   cloud_provider:
     name: ""
   prefix_path: ""
   win_prefix_path: ""
   addon_job_timeout: 0
   bastion_host:
     address: ""
     port: ""
     user: ""
     ssh_key: ""
     ssh_key_path: ""
     ssh_cert: ""
     ssh_cert_path: ""
   monitoring:
     provider: ""
     options: {}
     node_selector: {}
     update_strategy: null
     replicas: null
     tolerations: []
     metrics_server_priority_class_name: ""
   restore:
     restore: false
     snapshot_name: ""
   rotate_encryption_key: false
   dns: null
 
 
With this configuration in place, make sure you've created **/mnt** directory on all nodes, as this will be used for mounting the volume on all the containers that will be running the kubernetes services. Also replace the <ip-addr> with the appropriate IP address for each of the VM, and create a single private key.pem file which will be used to ssh into the cluster.
 
Now run the below command to install kubernetes::
 
   rke up
   
 


Install Minio
--------------

Below are the steps for installing Minio on the Kubernetes cluster.


Install Spark
--------------

Below are the steps for installing Apache Spark.

Install HIVE
--------------

Below are the steps for installing HIVE.

Install Jupyter
--------------

Below are the steps for installing Jupyter.

Install Fire Insights
--------------

Below are the steps for installing Fire Insights.
