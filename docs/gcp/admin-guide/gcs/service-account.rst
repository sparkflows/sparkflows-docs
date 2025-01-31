Service Account
======

This guide provides step-by-step instructions for creating a Service Account in GCP. The Service Account will be used to authenticate and access GCP resources, such as Google Storage from Fire Insights.

Prerequisites
----

#. Google Cloud Project.
#. IAM permissions to create/manage service accounts and assign roles.
#. API access (for required services).
#. Service Account Key (optional but necessary for external authentication).
#. IAM roles to define the permissions of the service account.

Steps to Set Up a Service Account with GCS Access:
----

#. Create a Service Account in GCP:

   #. Go to the Google Cloud Console: https://console.cloud.google.com/.

   #. Select the project where you want to create the service account.

   #. Navigate to IAM & Admin > Service Accounts in the Google Cloud Console.

   #. Click on the Create Service Account button.

   #. In the Create service account form:

      #. Service account name: Give the service account a meaningful name (e.g., databricks-gcs-access).
      #. Service account ID: This will be auto-generated based on the name.
      #. Description: (Optional) You can provide a description for this service account.
  
   #. Click Create.

#. Assign the Service Account Permissions:

   Once the service account is created, you need to assign it the necessary permissions for accessing Google Cloud Storage (GCS).

   #. In the Grant this service account access section:

      #. Role: Choose a role that grants access to GCS. The most common roles for GCS are:
      #. Storage Object Viewer: Grants read access to GCS objects.
      #. Storage Object Creator: Grants write access to GCS.
      #. Storage Object Admin: Grants full access to GCS objects (read/write).
      #. Storage Admin: Full access to GCS, including bucket-level operations (creation, deletion, etc.).

   #. Select the appropriate role (for example, Storage Object Admin for full access).

   #. Click Continue.

#. Create the Service Account Key:

   To authenticate the service account programmatically, you'll need to create a key file (typically in JSON format).

   #. After assigning the role, click Done to finish the service account creation process.
   #. Find the newly created service account in the Service Accounts list.
   #. Click the three vertical dots (menu) next to the service account and select Create Key.
   #. Select JSON as the key type.
   #. Click Create to download the JSON key file to your machine. Save this file securely, as it contains the credentials needed to authenticate the service account.

#. Set Up GCS Access in Your Application:

   After creating the service account and downloading the key file, you'll use the credentials in your application to authenticate and access GCS.


