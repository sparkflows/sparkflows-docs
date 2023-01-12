Assume Role Configurations
=======

Following steps are required to create a role for S3 bucket access and assume the Role from Fire Insights.

1. Create a Role:

Login to AWS Console which has sufficient privilege to create a role with name ''assume-role-bucket1''.

2. Create Inline Policy:

"Create an ''inline policy'' which has access to S3 policy which in turn has access to the different buckets e.g. ''assume-role-bucket1'' & ''assume-role-bucket2'' and then attach it to the role."

::

    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": [
                "s3:GetBucketLocation",
                "s3:ListAllMyBuckets"
            ],
            "Resource": "*",
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:List*",
                "s3:GetObject*",
                "s3:PutObject*",
                "s3:GetBucketAcl"
            ],
            "Resource": [
                "arn:aws:s3:::assume-role-bucket1",
                "arn:aws:s3:::assume-role-bucket1/*",
                "arn:aws:s3:::assume-role-bucket2",
                "arn:aws:s3:::assume-role-bucket2/*"
            ],
            "Effect": "Allow"
        },
        {
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucket",
                "s3:DeleteBucketPolicy",
                "s3:DeleteBucketWebsite",
                "s3:PutAccelerateConfiguration",
                "s3:PutBucketAcl",
                "s3:PutBucketCORS",
                "s3:PutBucketLogging",
                "s3:PutBucketPolicy",
                "s3:PutBucketRequestPayment",
                "s3:PutBucketTagging",
                "s3:PutBucketVersioning",
                "s3:PutBucketWebsite",
                "s3:PutReplicationConfiguration"
            ],
            "Resource": "*",
            "Effect": "Deny"
        }
    ]
  }


3. In the trust relationship of that role, allow the AWS Resources role (ecsTaskExecutionRole) to assume the policy in the “assume-role-bucket1” role:

::

    {
	"Version": "2012-10-17",
	"Statement": [
		{
			"Effect": "Allow",
			"Principal": {
				"AWS": [
					"arn:aws:iam::<account-id>:role/ecsTaskExecutionRole"
									
				]
			},
			"Action": "sts:AssumeRole"
		}
	]
   }

.. note:: **ecsTaskExecutionRole** is attached with a policy to access ECS resources. 

4. Now, the policy ''assume_role_bucket1'' needs to be attached to the ''EMR_EC2_DefaultRole'' role, added for EMR resources, so that it gets access to the above role while submitting the job on ''EMR Cluster or EMR Livy''.


.. note:: Make sure to change ARN value to an exact value.
