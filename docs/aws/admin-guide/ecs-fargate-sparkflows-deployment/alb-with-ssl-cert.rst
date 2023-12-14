Configure SSL with Load Balancer for ECS Deployment
====================================================
Follow the steps below to create a self-signed certificate, upload the certificate to ACM, and use it with the new load balancer to route the request to the ECS service.

Step 1 : Create self-signed certificate into ACM
------------------
#. Login to one of the EC2 Server and verify if you've the openssl installed in your EC2 server: ::

    $ openssl version
    OpenSSL 1.0.2k-fips  26 Jan 2017


#. Create an RSA private key to create your certificate signing request (CSR). 
   
   To create your private key, use the openssl genrsa command::

    $ openssl genrsa 2048 > privatekey.pem
    Generating RSA private key, 2048 bit long modulus
    .................................................................................................+++
    ..........+++
    e is 65537 (0x10001)

#. Verify the `privatekey.pem` created by the above command: ::

    $ cat privatekey.pem
    -----BEGIN RSA PRIVATE KEY-----
    MIIEowIBAAKCAQEAtpKersNCj+nMTzz4iq4/a3bBvXI7zNL/EpAdLjBLJXwvU8WM
    UPlxq0C8ifY45PRG1w294akcUDx4nNxBQ1AXftVuWtELlaosN3w1QEc11j3Cm4xX
    ................................................................
    ................................................................
    ................................................................
    ................................................................
    AgSeDu5yjK6uGsxBBnM+dmp7Q6cvneKVFhuhADTwbp5IFqtegzoJ
    -----END RSA PRIVATE KEY-----

#. Create a CSR file. A CSR is a file you send to a certificate authority (CA) to apply for a digital server certificate. 

   To create a CSR, use the openssl req command: ::

    openssl req -new -key privatekey.pem -out csr.pem
    You are about to be asked to enter information that will be incorporated
    into your certificate request.
    What you are about to enter is what is called a Distinguished Name or a DN.
    There are quite a few fields but you can leave some blank
    For some fields there will be a default value,
    If you enter '.', the field will be left blank.
    -----
    Country Name (2 letter code) [XX]:US
    State or Province Name (full name) []:CA
    Locality Name (eg, city) [Default City]:San Francisco
    Organization Name (eg, company) [Default Company Ltd]:Sparkflows Inc
    Organizational Unit Name (eg, section) []:ENG
    Common Name (eg, your name or your server's hostname) []:test.sparkflows.net
    Email Address []:test@sparkflows.io

    Please enter the following 'extra' attributes
    to be sent with your certificate request
    A challenge password []:Any@123
    An optional company name []:

#. Create a signing request. You can submit the signing request to a third party for signing, or sign it yourself for development and testing. Self-signed certificates can also be used for backend HTTPS between a load balancer and EC2 instances.

#. Sign the certificate. To sign the certificate, use the openssl x509 command. The following example uses the private key from the previous step (privatekey.pem) and the signing request (csr.pem) to create a public certificate named public.crt that is valid for 365 days. ::

     openssl x509 -req -days 365 -in csr.pem -signkey privatekey.pem -out public.crt

   **Note:** Keep the private key and public certificate for later use. You can discard the signing request. Always store the private key in a secure location and avoid adding it to your source code.

Step 2 : Import the self-signed certificate into the ACM
---------------------
#. Open the **AWS Certificate manager** in the console, and click on **Import certificate** as shown below:

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/import-certificate.png
      :alt: aws
      :width: 60%
   
   Once you've added the certificate, it will show up as **imported** type:

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/list-certificates.png
      :alt: aws
      :width: 60%

Step 3 : Create an ECS service
--------------------
#. Navigate to the **ECS service** in the AWS console, select the cluster where you want to create a service and click on **Create** and you'll be presented with a Create Service form as shown below.

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/create-ecs-service.png
      :alt: aws
      :width: 60%

#. Provide the deployment configuration for the service:

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/deployment-config.png
      :alt: aws
      :width: 60%

#. Provide the load balancer configuration. Here you can select the ACM certificate that we imported in the first step OR you can use an existing certificate managed by ACM or IAM.

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/configure-load-balancer.png
      :alt: aws
      :width: 60%

#. Provide the target group configuration as shown below in the image.
   
   **Note:**We'll be modifying the below target group configuration for healthcheck rules, once the service is created.

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/configure-target-group.png
      :alt: aws
      :width: 60%
   
   Finally, click on **Create** button to create the service.

Step 4 : Configure the Health Check for Target Group
--------
#. Navigate to the target group created in the previous step and update the health check config, to have the status code as 200,302.

   .. figure:: ../../../_assets/aws/ecs-fargate-sparkflows-deployment/health-check-tg.png
      :alt: aws
      :width: 60%

Step 5 : Configure the Security group for the ECS Service
--------
#. Navigate to the **ECS Service Networking** tab, click on the **security group** and update the **inbound rules**, to accept connections from the security group of the load balancer. 

   Once this is done, wait for 2-3 minutes for the service to be up and reach a healthy state. 

   Once the service is stable and the target group is healthy, you can navigate to the **https://<alb-host-name/** to view the login page.
