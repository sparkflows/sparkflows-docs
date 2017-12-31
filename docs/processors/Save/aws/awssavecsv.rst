
S3SaveCSV
^^^^^^ 

Saves the DataFrame into the specified S3 location in CSV Format

type

transform

nodeClass

fire.nodes.save.aws.NodeS3SaveCSV

Fields

+--------------------+-----------------------+----------------------------------------------------------+
| Name               | Title                 | Description                                              |
+====================+=======================+==========================================================+
| path               | Path                  | Path where to save the CSV files                         |
+--------------------+-----------------------+----------------------------------------------------------+
| awsAccessKeyId     | AWS Access Key Id     | AWS Access Key Id                                        |
+--------------------+-----------------------+----------------------------------------------------------+
| awsSecretAccessKey | AWS Secret Access Key | AWS Secret Access Key                                    |
+--------------------+-----------------------+----------------------------------------------------------+
| saveMode           | Save Mode             | Whether to Append, Overwrite or Error if the path Exists |
+--------------------+-----------------------+----------------------------------------------------------+