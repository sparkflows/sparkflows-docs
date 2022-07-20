Assume Role Configurations
=======

Below are steps on how to create a role with S3 Bucket access and assume the Role from Fire Insights.

1. Create a Role

Login to AWS Console which have sufficient privilege to create a role with name ''assume-role-bucket1''

2. Create inline Policy

Create inline policy which have access of s3 specific bucket say ''assume-role-bucket1'' and attach to the role.

3. User must have permissions to assume assume-role-bucket1.

::

    {
  "Version": "2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Action": "sts:AssumeRole",
    "Resource": "arn:aws:iam::<account-1-id>:role/assume-role-bucket1"
  }
}

4. "assume-role-bucket1" Role trust policy must allow User to assume "assume-role-bucket1" Role.

::

    {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<account-1-id>:user/User"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}

5. Now, you can easily assume a role, use its temporary creds to access s3 Bucket using Fire Insights.


