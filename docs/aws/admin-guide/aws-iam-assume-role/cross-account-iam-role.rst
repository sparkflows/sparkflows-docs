Cross Account IAM Role
=======
Cross-account access in AWS refers to the ability for an AWS user or role in one AWS account to access resources in another AWS account. This can be accomplished using AWS Identity and Access Management (IAM) roles, AWS Resource Access Manager (RAM), or AWS Organizations. With IAM roles, you can create a role in one account that can be assumed by a user in another account. This allows you to delegate access to AWS resources in one account to users in another account.

Below we outline on how to manage this in Sparkflows.

If a Sparkflows instance on ``ECS/EC2/EMR`` and AWS ``S3`` are in two different accounts, then a cross-account role is required for the Sparkflows instance to access the ``S3`` and the other resources in different accounts. The way to grant access to a bucket is to allow an account to assume a role in another account.

Consider AWS Account A with account ID ``deployment-acct-id`` and AWS Account B with account ID ``bucket-owner-acct-id``. Account A has a Sparkflows instance running and Account B has a bucket ``s3-bucket-name``.

The steps to configure Account A to use the AWS AssumeRole action to access S3 files in ``s3-bucket-name`` as a role in Account B. To enable this access you perform configuration in Account A and Account B and add the role in Sparkflows.

**1. In Account A, create role MyRoleA and attach policies**

1. Create a role named ``MyRoleA`` in ``Account A``. The Instance Profile ARN is::

    arn:aws:iam::<deployment-acct-id>:instance-profile/MyRoleA.


2. Create a policy that says that a role in ``Account A`` can assume ``MyRoleB`` in ``Account B``. Attach it to ``MyRoleA``. Click add inline policy and paste in the policy::


    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "Stmt1487884001000",
          "Effect": "Allow",
          "Action": [
            "sts:AssumeRole"
          ],
          "Resource": [
            "arn:aws:iam::<bucket-owner-acct-id>:role/MyRoleB"
          ]
        }
      ]
    }


3. Update the policy by adding the below statement for ``Account A`` role used to run the Sparkflows on EC2/EMR/ECS, adding the ``iam:PassRole action to MyRoleA``::


    {
          "Effect": "Allow",
          "Action": "iam:PassRole",
          "Resource": [
            "arn:aws:iam::<deployment-acct-id>:role/MyRoleA"
          ]
     }


**2. In Account B, create role MyRoleB and attach policies**

1. Create a role named ``MyRoleB``. The Role ARN is::

    arn:aws:iam::<bucket-owner-acct-id>:role/MyRoleB.


2. Edit the trust relationship of role ``MyRoleB`` to allow a role ``MyRoleA`` in ``Account A`` to assume a role in ``Account B``. Select IAM > Roles > MyRoleB > Trust relationships > Edit trust relationship and enter::
    
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "arn:aws:iam::<deployment-acct-id>:role/MyRoleA"
            ]
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
3. Create a bucket policy for the bucket ``s3-bucket-name``. Select S3 > ``s3-bucket-name`` > Permissions > Bucket Policy. Include the role (Principal) ``MyRoleB`` in the bucket policy::

    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": [
                "arn:aws:iam::<bucket-owner-acct-id>:role/MyRoleB"
            ]
          },
          "Action": [
            "s3:GetBucketLocation",
            "s3:ListBucket"
          ],
          "Resource": "arn:aws:s3:::<s3-bucket-name>"
        },
        {
          "Effect": "Allow",
          "Principal": {
              "AWS": [
                  "arn:aws:iam::<bucket-owner-acct-id>:role/MyRoleB"
              ]
          },
          "Action": [
            "s3:PutObject",
            "s3:PutObjectAcl",
            "s3:GetObject",
            "s3:DeleteObject"
          ],
          "Resource": "arn:aws:s3:::<s3-bucket-name>/*"
        }
      ]
    }

**3. Add MyRoleA to the Sparkflows user group**

 Now from the Sparkflows users in the group can access the S3 resources in another account i.e  ``Account B``.

