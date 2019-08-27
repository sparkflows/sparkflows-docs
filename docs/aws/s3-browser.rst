S3 Browser
==========

Fire Insights allows browsing the files in S3.

Configue AWS access key and password
-----------------------------------

Run ``aws configure`` to configure your credentials on the machine on which Fire Insights is running.

Install aws cli
---------------

- http://docs.aws.amazon.com/cli/latest/userguide/installing.html
- pip install awscli --upgrade --user
 
   
Configure AWS
-------------

- aws configure
  - It would ask for 
    - AWS Access Key
    - AWS Secret Access Key
    - Default Region Name : Just enter
    - Default Output Format : Just enter
    
.. figure:: ../_assets/tutorials/awscli/AWS2.PNG
   :alt: awscli
   :align: center  
   
Access S3 in fire-ui
---------------------

Go to Fire-UI page and Dropdown databrowser there we have S3 Browser as a option

.. figure:: ../_assets/tutorials/awscli/AWS3.PNG
   :alt: awscli
   :align: center
   
- Click on AWS s3 then we will get File available in it.

Protecting Data Using Server Side Encryption
--------------

Data encryption settings on S3 buckets: https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html


.. figure:: ../_assets/tutorials/awscli/AWS4.PNG
   :alt: awscli
   :align: center
   
   
REFERENCE NOTES
-----

1. You'll need create a user with programmatic access by following the steps here (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

 

2. Next, you'll create an IAM policy that defines what this user has access to in your AWS account.  It's important to only grant this user minimal access within your account. See this documentation for how to create IAM policies (https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html).

 

3. Finally, you'll create an access key and secret key for this user (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_CreateAccessKey).

*Note* It's important to regularly rotate your access and secret keys. See this documentation for more information (https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#rotating_access_keys_console)

