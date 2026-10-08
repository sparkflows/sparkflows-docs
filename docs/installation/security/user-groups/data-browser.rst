Data Browser
===================

Content in the **Data Browser** is displayed based on the **User Group** of the logged in **User**. It is applicable to while browsing File System or S3 locations.

Single Group Assignment
-----------------

When a **User** is assigned to a single **User Group** in the **Sparkflows** then the content of the **Data Browser** is updated as per the **AWS Role ARN** of the **Group**.

**AWS Role ARN** would define the **S3 locations** that the users of the group can browse and view.

Multiple Group Assignment
-------------------

When a **User** is assigned to multiple **User Groups** in the **Sparkflows** then the content of the **Data Browser** is updated as per the **Group** having **ID** value of **1**.
