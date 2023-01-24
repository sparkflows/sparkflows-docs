Fire-Insight Setup in AWS

* Install Fire-Insight

  * Option 1: Install AMI
  
    - Prerequisites: 
    - Installation Steps: <Link to the User docs>
    
  * Option 2: Install in Linux VM
  
    - Prerequisites: Create Security Group with proper access
    - Installation Steps: <Link to the User docs>
    
* Login to Fire-Insight  

    - Test if a Sample Project can be created and workflow can be executed
    - If we need to enable pyspark , then 
      set module.workflowType = both

* Create S3 Bucket fire-insight-bucket1
    
    - <Screenshot>

* Create AWS EC2 Role for Fire Insight

  - Show the Screenshot 
  - Create the Role fire-insight-role without specifying any Policy and Trust
  - <Link to the User docs>
  
* Add policy to the Role for S3-Bucket-Access 
  - Create fire-insight-policy
  - <Link to the User docs>

* Login to Fire-Insight as Admin
  - Specify the s3 bucket path in AWS Configuration
  - Test the Bucket Access
  
* Steps to load sample data in Bucket
   - AWS 
   - Databricks 
   
* Steps to create the certificate for https access
   - <Link to the User docs>

* Steps to setup EMR Access
  - <Link to the User docs>
