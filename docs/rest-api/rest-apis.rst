
Sparkflows Rest API
=========

::

[ Base URL: 159.223.140.122:8080/ ]
http://159.223.140.122:8080/v2/api-docs?group=fire
Sparkflows REST API Documentation
Terms of service


Sparkflows License Version 1.0

about-controller
++++++

About Controller

::
    
    GET /api/v1/app/release-info getBuildReleaseInfo
    
    
analysis-flow-trigger-controller
+++++++++

Analysis Flow Trigger Controller

::

    GET /api/v1/workflow-triggers getAllAnalysisflowTriggers  
    POST /api/v1/workflow-triggers createAnalysisflowTrigger  
    GET /api/v1/workflow-triggers/{analysisworkflowTriggerId} getAnalysisflowTriggerDetails
    DELETE /api/v1/workflow-triggers/{analysisWorkflowTriggerId} deleteAnalysisflowTriggerById
    

application-connection-controller
++++++++++++++++++++++++
Application Connection Controller

::
  
    POST /api/v1/connections Create a connection  
    DELETE /api/v1/connections/{appConnectionId} deleteApplicationConnection
    GET /api/v1/connections/{connectionId} Get connection details by connectionId  
    GET /api/v1/connections/{connectionId}/tables getTables
    PUT /api/v1/connections/{id} Update a connection details
    GET /api/v1/connections/categories/{category} getAllConnections 
    GET /api/v1/connections/global getGlobalConnections  
    GET /api/v1/connections/loggedInUser getConnectionsForLoggedInUser
    GET /api/v1/connections/manage/access getConnectionsPermissions
    GET /api/v1/connections/name/{connectionName}/isUnique isUniqueConnectionName
    GET /api/v1/connections/projects/{projectId} Get all connections by projectId
    POST /api/v1/connections/test testConnection
    
auth-permission-controller
++++++++++++++++++
Auth Permission Controller

::

    GET /api/v1/user-permissions Get User permissions
    
auth-user-group-controller
+++++++++++

Operations pertaining to User Group in Sparkflows
::

    GET /api/groups/user Get logged in User group
    GET /api/v1/groups/{id} Get User by Group Id
    GET /api/v1/groups/user/{id} Get Group by User Id
    
auth-user-role-controller
++++++++++++++

Operations pertaining to User Role in Sparkflows
::

    GET /api/v1/roles/user/{id} Get Role by User Id
    
auto-ml-controller
+++++++++++

Auto ML Controller
::

    GET /api/v1/auto-ml getAutoMlList
    POST /api/v1/auto-ml configureAutoMl
    PUT /api/v1/auto-ml updateAutoMl
    GET /api/v1/auto-ml/{autoMlId} getAutoMlDetails
    DELETE /api/v1/auto-ml/{autoMlId} deletAutoMl
    GET /api/v1/auto-ml/project/{projectId} getAutoMlListOfProject
    POST /api/v1/auto-ml/start/{autoMlId} startAutoMl

auto-ml-executions-controller
++++++++++++++++++

Auto ML Executions Controller
::

    GET /api/v1/auto-ml/execution/{autoMlExecutionId} getAutoMlExecutionsByExecutionId
    POST /api/v1/auto-ml/execution/{autoMlExecutionId}/autoMl setAutoMlExecutionsIsFavoriteOrNot
    POST /api/v1/auto-ml/execution/{executionId}/autoMl/{autoMlId} saveAutoMlExecutions
    POST /api/v1/auto-ml/execution/comment addCommentToAutoMlExecution
    GET /api/v1/auto-ml/executions/{autoMlId} getAutoMlExecutions
    
aws-controller
++++++++++++

Aws Controller
::

    GET /api/v1/aws/roles getAwsRoles
    
conf-property-controller
++++++++++++++++

Operations pertaining to Conf Property in Sparkflows
::

    GET /api/v1/configs/app Get Application Configuration property
    GET /api/v1/configurations Get configurations
    POST /api/v1/configurations Save/Update configurations
    GET /api/v1/configurations/infer Infer configurations
    GET /api/v1/configurations/kafka Get kafka configuration
    GET /api/v1/configurations/uiSettings Get Configuration property of ui settings
    GET /api/v1/main/modules-enabled Get Configuration property of modules
    GET /api/v1/main/sso-conf Get Configuration property of sso

credential-store-controller
+++++++++++++

Credential Store Controller
::

    GET /api/v1/credentialStores Get All CredentialStore details
    POST /api/v1/credentialStores Create CredentialStore
    PUT /api/v1/credentialStores Update CredentialStore details
    DELETE /api/v1/credentialStores/{credentialStoreId} delete CredentialStore details
    GET /api/v1/credentialStores/{id} Get CredentialStore details by id
    POST /api/v1/credentialStores/testDetails Test CredentialStore details

custom-processor-controller
++++++++++

Custom Processor Controller
::

    GET /api/v1/processor/export/{customProcessorIds} Get Custom Processor for export
    GET /api/v1/processors Get custom processor
    POST /api/v1/processors Create custom processor
    GET /api/v1/processors/{customProcessorId} Get custom processor by id
    DELETE /api/v1/processors/{customProcessorId} deleteCustomProcessor
    POST /api/v1/processors/datasets/{datasetId} Test custom processor
    POST /api/v1/processors/import Import custom processor
    GET  /api/v1/processors/names getCustomProcessorByName

dashboard-controller
+++++++++++

Operations pertaining to Dashboards in Sparkflows
::

    GET /api/v1/dashboards Get all the dashborads
    POST /api/v1/dashboards Create dashboard
    PUT /api/v1/dashboards/{dashboardId} update dashboard
    DELETE /api/v1/dashboards/{dashboardId} Delete dashboard
    GET /api/v1/dashboards/{id} Get dashboard by Id
    GET /api/v1/dashboards/all Get all Dashboards
    GET /api/v1/dashboards/categories getAllDashboardCategories
    GET /api/v1/dashboards/results Get dashboard results
    
data-quality-controller
++++++++

Data Quality Controller
::

    DELETE /api/v1/dataQuality Delete Data Quality Records by dataQuality ids
    GET /api/v1/dataQuality/summary Api for data-quality summary
    POST /api/v1/summaryWorkflow/{projectId}/{datasetUuid} Create summary workflow
    GET /api/vi/data-quality/validation/{dataQualityUuid} api for get data validation by dataQualityUuid
    GET /api/vi/dataQuality api for get all data quality
    GET /api/vi/dataQuality/{dataQualityUuid} api for get data quality by dataQualityUuid
    GET /api/vi/dataQuality/counts api for getting the data quality record counts
    POST /api/vi/executeSummaryWorkflow/{projectId}/{datasetUuid} Api for creating and executing dataset summary workflow

data-set-controller
++++++++

Operations pertaining to Datasets in Sparkflows
::

    GET /api/v1/datasets Get all datasets
    POST /api/v1/datasets Create Dataset
    DELETE /api/v1/datasets Delete Dataset
    GET /api/v1/datasets/{datasetId} Get Dataset by Id
    POST /api/v1/datasets/{datasetId}/{datasetName}/clone clone the dataset
    GET /api/v1/datasets/categories getAllDatasetCategories
    GET /api/v1/datasets/count Get Dataset Count
    GET /api/v1/datasets/hive/sample-data Get sample data from given DB and Table
    GET /api/v1/datasets/latest Get Latest Five Datasets
    GET /api/v1/datasets/list/export Get Datasets for export
    GET /api/v1/datasets/projects/{projectId} Get Datasets by project Id
    GET /api/v1/datasets/read-options Get Read Options of Datasets
    POST /api/v1/datasets/sample-data Returns sample data
    POST /api/v1/datasets/schema Returns schema of the files in the given path using the given delimiter
    GET /api/v1/datasets/users Get user owned and shared datasets

databricks-controller
+++++++

Databricks Controller
::

    GET /api/v1/databricks/clusters getClusterInfo
    GET /api/v1/databricks/clusters/restart restartDatabricksClusters
    POST /api/v1/databricks/command executeDatabricksDDLCommand
    GET /api/v1/databricks/database/{dbName}/table/{table} getTableColumnsInfo
    GET /api/v1/databricks/database/{dbName}/tables getAllDatabases
    GET /api/v1/databricks/database/{dbName}/tables/{tableName}/sample-data getSampleData
    GET /api/v1/databricks/database/list getAllDatabases
    GET /api/v1/databricks/jobs/runs getRunDetailsByRunId
    GET /api/v1/databricks/notebooks/jobs getDatabricksNotebooksJob
    POST /api/v1/databricks/notebooks/jobs/execute executeDatabricksNotebooksJob
    GET /api/v1/databricks/query/history getQueryHistoryOfLoggedInUser
    GET /api/v1/dbfs getDatabricksFileSystem
    DELETE /api/v1/dbfs/delete Delete DBFS files via It's Paths
    GET /api/v1/dbfs/directory getDatabricksFileSystemInDir
    GET /api/v1/dbfs/fileContent getDbfsFileContent
    GET /api/v1/dbfs/files/download download dbfs file
    POST /api/v1/dbfs/files/upload uploadDbfsFile
    POST /api/v1/dbfs/mkdir createDbfsDir
    POST /api/v1/dbfs/renameOrMove/file moveOrRenameFile
 
dataset-hierarchy-controller 
++++++++++

Dataset Hierarchy Controller
::

    POST /api/v1/hierarchy createDatasetHierarchy
    PUT /api/v1/hierarchy updateDatasetHierarchy
    DELETE /api/v1/hierarchy/{datasetHierarchyId} deleteDatasetHierarchy
    GET /api/v1/hierarchy/datasets/{datasetUuid} getDatasetHierarchy

datasource-controller
++++++++++++

Datasource Controller
::

    GET /api/v1/datasource/metrics getDatasourceConnectionPoolInfo

diagnostics-controller
++++++++++++++

Diagnostics Controller
::
 
    GET /api/v1/getDiagnostics Get all diagnostics

event-controller
++++++++++

Event Controller
::

    DELETE /api/v1/events/{days} deleteEventsByDays
    GET /api/v1/events/project getProjectEvents
    GET /api/v1/events/search listAllEvents
    GET /api/v1/operations/events/total getTotalEventCountByAllUsers
    GET /api/vi/events/counts api for getting the Event record counts

fire-access-token-controller
+++++++++=

Fire Access Token Controller
::

    GET /api/v1/tokens getFireAccessTokens
    POST /api/v1/tokens generateToken
    GET /api/v1/tokens/{id} getFireAccessTokenDetails
    DELETE /api/v1/tokens/{id} deleteFireAccessTokenById

git-integration-controller
++++++++

Git Integration Controller
::

    POST /api/v1/git/branch/create createBranch
    GET /api/v1/git/branches getBranchList
    GET /api/v1/git/clone cloneFromGit
    GET /api/v1/git/credentials getCredentials
    POST /api/v1/git/credentials Update Git Credentials
    POST /api/v1/git/link linkProject
    GET /api/v1/git/linkedProjects linkedProjects
    GET /api/v1/git/projectList getProjectListInGit
    POST /api/v1/git/projects/unlink unLinkProjects
    POST /api/v1/git/push/project/{projectId} pushProjectToGit
    POST /api/v1/git/push/workflow pushWorkflowToGit
    POST /api/v1/git/push/workflows pushWorkflowsToGit
    POST /api/v1/git/push/workflowVersion pushWorkflowVersionToGit
    GET /api/v1/git/workflow/headCommitAndLatest/{workflowId} headCommitAndlatestchangesOfWorkflowJson
    GET /api/v1/git/workflow/status/{projectId} getUncheckedWorkflowList

glue-controller
+++++++++++

Glue Controller
::

    GET /api/v1/glue/connections/{connectionId}/jobs/{jobName} getJobDetails
    GET /api/v1/glue/jobs/run/{jobName} getJobRun
    
group-admin-controller
++++++++

Operations pertaining to Group in Sparkflows
::

    GET /api/groups/{groupId} Get Group by Id
    GET /api/v1/groups Get all Groups
    POST /api/v1/groups Create Group
    DELETE /api/v1/groups/{groupId} Delete Group

hdfs-controller
+++++++

Operations pertaining to HDFS in Sparkflows
::

    GET /api/v1/hdfs Returns list of all the files on hdfs in the users home directory
    GET /api/v1/hdfs/configurations Get HDFS Configurations
    POST /api/v1/hdfs/dir/create Create HDFS directory
    GET /api/v1/hdfs/dir/files Returns list of files in HDFS in the specified directory for download from folder
    GET /api/v1/hdfs/dir/open Returns list of files in HDFS in the specified directory
    GET /api/v1/hdfs/files Returns list of all the files on hdfs in the users home directory in sorted order
    DELETE /api/v1/hdfs/files/delete Delete HDFS files via It's Paths
    GET /api/v1/hdfs/files/download download hdfs file
    GET /api/v1/hdfs/files/move Move HDFS File
    POST /api/v1/hdfs/files/moves Move HDFS File
    GET /api/v1/hdfs/files/open Accepts HDFS file path and returns first X bytes of content
    GET /api/v1/hdfs/files/permissions/change Change file permissions of HDFS File
    GET /api/v1/hdfs/files/rename Rename HDFS File
    POST /api/v1/hdfs/files/upload Uploads file
    GET /api/v1/hdfs/user/home-dir Returns path of user's home directory

help-controller
++++++

Help Controller
GET
/api/v1/helps/{contentType}
getHelpContent
hive-controller
Operations pertaining to Hive in Sparkflows
POST
/api/v1/hive/command/execute
Execute HIVE Command
GET
/api/v1/hive/databases
Get all Hive Databases
GET
/api/v1/hive/tables
Get all Hive Tables for given db
icon-controller
Icon Controller
GET
/api/v1/icons
getIcons
interactive-dashboard-controller
Operations pertaining to Interactive Dashboards
GET
/api/v1/i-dashboards
Get all the interactive dashboards
POST
/api/v1/i-dashboards
Create interactive dashboard
PUT
/api/v1/i-dashboards/{dashboardId}
Update interactive dashboard
DELETE
/api/v1/i-dashboards/{dashboardId}
Delete interactive dashboard
GET
/api/v1/i-dashboards/{id}
Get interactive dashboard by Id
POST
/api/v1/i-dashboards/chart-data
Get Chart Data
GET
/api/v1/i-dashboards/datasets
Get all the Interactive Datasets
GET
/api/v1/i-dashboards/datasets/uuid/{uuid}
Get Interactive Dataset by uuid
POST
/api/v1/i-dashboards/filter
Filter Request
PUT
/api/v1/i-dashboardsarranged/{dashboardId}
Update interactive dashboard
POST
/api/v2/i-dashboards
Create or update interactive dashboards
PUT
/api/v2/i-dashboards
Create or update interactive dashboards
GET
/api/v2/i-dashboards/{dashboardId}
getArrangedInteractiveDashobardDetails
DELETE
/api/v2/i-dashboards/{dashboardId}
deleteInteractiveDashobard
GET
/api/v2/i-dashboards/projects/{projectId}
getArrangedInteractiveDashobards
ldap-config-controller
Ldap Config Controller
GET
/api/ldapConfigurations
Api To Get the Ldap Configuration
POST
/api/testLdapConnection
Api To Test the Ldap Connection
PUT
/api/updateLdapConfigurations
Api To Update the Ldap configurations
logs-controller
Logs Controller
GET
/api/fireLogs
View logs of fire
GET
/api/fireServer/exceptions/logs
View logs of fire server
GET
/api/fireServerLogs
View logs of fire server
GET
/api/pysparkLogs
View pyspark server log
GET
/api/search/logs/{logName}/{searchString}
Search logs
main-controller
Operations pertaining to Main Ctrl in Sparkflows
GET
/api/v1/main/about
Get Sparkflows details
GET
/api/v1/main/databricks-enabled/{name}
Get Configuration property of databricks by Name
metrics-controller
Metrics Controller
GET
/api/v1/metrics/summary/{analysisFlowId}
Gets the workflow metrics summary. It includes all users' workflow executions
GET
/api/v1/metrics/summary/{analysisFlowId}/time/{timeFilter}
Gets the workflow executions summary by time/date filter. It includes all users' workflow executions
GET
/api/v1/workflow/metrics/{workflowExecutionId}
Get job execution metrics for the given workflow execution id
GET
/api/v1/workflow/metrics/getAllMetricsOfEachWorkflow/{workflowId}
Get all execution metrics for the given workflow id
model-controller
Model Controller
DELETE
/api/v1/mlmodel/delete/{analysisFlowId}
Delete output model of job executions by workflow id
GET
/api/v1/mlmodel/getFeatureImportanceByModelUuid/{modelUuid}
Get feature importance by model uuid
GET
/api/v1/mlmodel/getMlDetailByModelUuid/{modelUuid}
Get model detail by model uuid
GET
/api/v1/mlmodel/getMLModelFeatures/{modelUuid}
Get the features of given model uuid
GET
/api/v1/mlmodel/getTestMetricsByModelUuid/{modelUuid}
Get test metrics from output model evaluation by model uuid
GET
/api/v1/mlmodel/getTrainMetricsByModelUuid/{modelUuid}
Get train metrics by model uuid
GET
/api/v1/mlmodel/model_Summary_analysisflow/{analysisFlowId}
Get output model summary by analysisFlowId
GET
/api/v1/mlmodel/model_Summary_analysisflow/{analysisFlowId}/time/{timeFilter}
Get output model summary by time/date filter
GET
/api/v1/mlmodel/model_Summary/{modelUuid}
Get output model summary by model uuid
GET
/api/v1/mlmodel/outputModel
Get all output model
GET
/api/v1/mlmodel/outputModel/{analysisflowExecutionId}
Get output model of job executions
GET
/api/v1/mlmodel/outputModel/{modelId}/download/{fileType}
zipDownload
GET
/api/v1/mlmodel/outputModelByAnalysisFlowId/{analysisFlowId}
Get all output model of job executions by workflow id
GET
/api/v1/mlmodel/outputModelByApplicationId/{applicationId}
Get output model of job executions by application id
GET
/api/v1/mlmodel/outputModelByModelUuid/{modelUuid}
Get output model by model uuid
GET
/api/v1/mlmodel/OutputModelEvaluationByModelUuid/{modelUuid}
Get output model evaluation by model uuid
GET
/api/v1/mlmodel/OutputModels
Get output model list
GET
/api/v1/mlmodel/OutputModels/fileInfo
getFileInfo
GET
/api/v1/mlmodel/OutputModelsById/{modelId}
Get output model list by id
GET
/api/v1/mlmodel/summary
Gets the model executions summary
POST
/api/v1/mlmodel/updateModel/{modelId}
Update model
node-controller
Operations pertaining to processors in Sparkflows
operations-controller
Operations Controller
pipeline-controller
Operations pertaining to Pipeline in Fire
pipeline-execute-controller
Pipeline Execute Controller
pipeline-node-controller
Pipeline Node Controller
pipeline-scheduler-controller
Pipeline Scheduler Controller
project-controller
Project Controller
project-discussion-controller
Project Discussion Controller
GET
/api/v1/getProjectDiscussions/{projectId}
Get All Project Discussions By ProjectId
POST
/api/v1/projectDiscussion
Create Discussion For Project
DELETE
/api/v1/projectDiscussion/{discussionId}
Delete discussion from Project
project-overview-controller
Project Overview Controller
GET
/api/v1/projectOverview/counts/{projectId}
getProjectElementInfo
project-permission-controller
Project Permission Controller
GET
/api/v1/groups/projects/{projectId}
getGroupByprojectId
POST
/api/v1/project-permissions
saveShareProjectInfo
GET
/api/v1/project-permissions/{projectPermissionId}
Get project-permission details by id
DELETE
/api/v1/project-permissions/{projectPermissionId}
deleteProjectPermission
GET
/api/v1/project-permissions/projects/{projectId}
Get project permissions by projectId
GET
/api/v1/project-permissions/projects/{projectId}/groups/{groupId}
getProjectPerByProjectIdAndGroupId
properties-controller
Properties Controller
GET
/api/v1/user/swagger/enabled
getSwaggerStatus
POST
/api/v1/user/swagger/status/{enableSwagger}
setSwaggerStatus
recommendation-controller
Recommendation Controller
GET
/api/v1/recommendations/nodes
Gets recommended node mapping list
GET
/api/v1/recommendations/nodes/refresh
Refresh node mapping list
role-admin-controller
Operations pertaining to Role in Sparkflows
GET
/api/v1/permissions
Get all Permissions
GET
/api/v1/role-permissions/roles/{id}
Get Role Permissions by Role Id
GET
/api/v1/role-permissons/roles/{id}
Get Role Permissions by Role Id
GET
/api/v1/roles
Get user Roles
POST
/api/v1/roles
Create Role
GET
/api/v1/roles/{id}
Get Role Name by Id
DELETE
/api/v1/roles/{id}
Delete Role by Role Name
run-time-statistics-controller
Run Time Statistics Controller
GET
/api/v1/runTimeStatistics
Get Run time statistics
s-3-controller
Operations pertaining to S3 bucket in Sparkflows
GET
/api/v1/aws-s3/directory/create
Create directory in s3
DELETE
/api/v1/aws-s3/file
Delete file from s3
GET
/api/v1/aws-s3/file/rename
Rename folder/file of s3
DELETE
/api/v1/aws-s3/folder
Delete folder from s3
GET
/api/v1/aws/home-dir
Returns value of aws home directory
GET
/api/v1/s3-buckets/aws-config-available
return true or false to make it sure that aws s3 is configured at aws cli level
GET
/api/v1/s3-buckets/configs
Returns list of buckets in S3 by reading access key and secret key from configuration
GET
/api/v1/s3-buckets/fileContent
Returns content of a file of s3
GET
/api/v1/s3-buckets/name/{bucketName}
Returns list of files in S3 bucket directory
POST
/api/v1/s3-buckets/uploadFile
Upload file to s3
search-controller
Controller for searching workflows, datasets and dashboard by name
GET
/api/v1/search/{searchType}/{searchItem}
Search workflows, dataset and dashboard by name.
snowflake-controller
Snowflake Controller
POST
/api/v1/snowflake/command
executeSnowflakeDDLCommand
GET
/api/v1/snowflake/database/{dbName}/table/{table}
getTableColumnsInfo
GET
/api/v1/snowflake/database/{dbName}/tables
getDatabaseTables
GET
/api/v1/snowflake/database/{dbName}/tables/{tableName}/sample-data
getSampleData
GET
/api/v1/snowflake/database/list
get snowflake database list
GET
/api/v1/snowflake/schema/{dbName}/list
getAllSchema
GET
/api/v1/snowflake/warehouse/list
getAllWarehouse
user-admin-controller
Operations pertaining to Admin in Sparkflows
GET
/api/users/ldap/{username}
Add LDAP user
GET
/api/v1/configurations/ldap/enable
Get LDAP configuration
PUT
/api/v1/user/currentConnection/{connectionId}
set the user current connection
PUT
/api/v1/user/currentProject/{projectId}
set the user current project
GET
/api/v1/user/isAdmin/isSuperuser
Check user is admin/ superuser
GET
/api/v1/users
Get list of Users
POST
/api/v1/users
Create User
PUT
/api/v1/users
Update User
GET
/api/v1/users/{id}
Get user by user Id
DELETE
/api/v1/users/{id}
Delete User by user id
GET
/api/v1/users/{name}/validate
Validates user Name
GET
/api/v1/users/basicInfo
Get list of Users
GET
/api/v1/users/configurations
Get Configurations
GET
/api/v1/users/password/change
change password
POST
/api/v1/users/password/verify
verifies password
PUT
/api/v1/users/profile
update user basic profile (firstName, LastName, and email only
GET
/api/v1/users/UsageStatistics
Get Usage Statistics
GET
/api/v1/users/user-info
Get current logged-In User
web-app-controller
Web App Controller
GET
/api/v1/webApps
getWebApps
POST
/api/v1/webApps
createWebApp
PUT
/api/v1/webApps
updateWebApp
POST
/api/v1/webApps/{uuid}/userInputs
saveInput
GET
/api/v1/webApps/{webAppId}
getWebAppDetails
PUT
/api/v1/webApps/{webAppId}
changeWebAppStatus
DELETE
/api/v1/webApps/{webAppId}
deleteWebApp
GET
/api/v1/webApps/{webAppId}/by/condition
getWebAppDetailsByCondition
POST
/api/v1/webApps/{webAppId}/generateUuid
Generate uuid of app
POST
/api/v1/webApps/{webAppId}/nextStage
getNextStage
POST
/api/v1/webApps/{webAppId}/saveUuid
Save uuid of app
GET
/api/v1/webApps/{webAppId}/stage
getWebAppStageDetails
POST
/api/v1/webApps/{webAppId}/stage
addWebAppStage
DELETE
/api/v1/webApps/{webAppId}/stage/{stageId}
deleteWebAppStage
POST
/api/v1/webApps/{webAppId}/stage/details
addWebAppStageDetails
POST
/api/v1/webApps/browseFile/uuidExists
Webapp exists with uuid present in browse json file
POST
/api/v1/webApps/dbfs/upload/file
uploadFile
GET
/api/v1/webApps/execution/{executionId}
getWebappExecutionById
POST
/api/v1/webApps/import
Import analytic app
GET
/api/v1/webApps/polls/{uuid}/userInputs
pollUserInput
DELETE
/api/v1/webApps/project/{projectId}
deleteAllWebappsByProjectId
POST
/api/v1/webApps/showHideApps
show hide apps
PUT
/api/v1/webApps/stage
updateStage
POST
/api/v1/webApps/updateWfParameters/{wfId}
updateWfParameters
POST
/api/v1/webApps/upgrade
Upgrade analytic app
GET
/api/v1/webApps/uuidExists
does same uuid of app exists in project
web-app-version-controller
Web App Version Controller
GET
/api/v1/webappVersions/{webVersionId}
getWebAppDetailsByWebVersionId
GET
/api/v1/webappVersions/webApps/{webAppId}
getWebAppVersionsByWebAppId
wizard-controller
Operations pertaining to wizard in Fire
GET
/api/v1/wizards/actions
Returns actions
POST
/api/v1/wizards/convert-workflow
Convert WizardWorkflow to Workflow
GET
/api/v1/wizards/queries
Returns queries
GET
/api/v1/wizards/sections
Returns sections
POST
/api/v1/wizards/workflow/create
Create Workflow from workflow-wizard
workflow-controller
Operations allow interacting with workflows in Sparkflows
GET
/api/v1/apps/example-datasets-and-workflows/load
load Example datasets and workflows of Applications
GET
/api/v1/getAllCleaningWorkflows/{datasetUuid}
Get all cleaning workflows
GET
/api/v1/ibm-file
writes all the workflows to IBM file
POST
/api/v1/nodes/{nodeId}/schema/input
Retrieve schema of a node
POST
/api/v1/nodes/{nodeId}/schema/output
retrieve output schema of a node
DELETE
/api/v1/workflow/trash
Move selected workflow to trash
DELETE
/api/v1/workflow/trash/{workflowId}
Move workflow to trash
GET
/api/v1/workflows
Get all the workflows for a given project in desc order with detailed information'
POST
/api/v1/workflows
create a workflow
PUT
/api/v1/workflows
update a workflow
GET
/api/v1/workflows/{id}
Get workflow details by id
DELETE
/api/v1/workflows/{workflowId}
delete the workflow
POST
/api/v1/workflows/{workflowId}/{workflowName}/clone
clone the workflow
GET
/api/v1/workflows/{workflowId}/copy
Api for copying the workflow
GET
/api/v1/workflows/{workflowId}/lock
lock the workflow
GET
/api/v1/workflows/{workflowId}/unlock
Unlock the workflow
PUT
/api/v1/workflows/{workflowId}/uuid/{uuid}
updateUuid
GET
/api/v1/workflows/all
Get all workflows
POST
/api/v1/workflows/beautify
Beautify workflow
GET
/api/v1/workflows/count
Get Workflow Count
GET
/api/v1/workflows/dashboard
Get all the workflows of a project in desc order with basic information'
DELETE
/api/v1/workflows/emptyTrash
empty wfs from trash
GET
/api/v1/workflows/execution-enable
Get the value of execute enabled value of Configurations
GET
/api/v1/workflows/export/{id}
Get workflow content to export
POST
/api/v1/workflows/generatePysparkCode
Generate Pyspark Code
GET
/api/v1/workflows/latest
Get Latest WorkFlows
GET
/api/v1/workflows/list/export
Get Workflows for export
GET
/api/v1/workflows/name/{name}
Get workflow by Name
POST
/api/v1/workflows/nodes/{nodeId}/execute
Execute workflow's node
GET
/api/v1/workflows/nodes/state/inconsistent
Return the list of nodes that are in an inconsistent state - mainly with regard to schema
PUT
/api/v1/workflows/restore
Restore selected trashed wfs'
PUT
/api/v1/workflows/restore/{workflowId}
Restore trashed wfs'
GET
/api/v1/workflows/trashed
Get trashed workflows for a given project in desc order with detailed information'
GET
/api/v1/workflows/users/logged-in
Get workflows owned and shared with logged-in user
GET
/api/v1/workflows/uuid/{uuid}
Get workflow by uuid
POST
/api/v1/workflows/validateCode
Api for syntax checking of pyspark code
GET
/api/v1/workflows/versions
Retrieve the workflow versions
GET
/api/v1/workflows/wfName/{id}
Get workflow name by id
GET
/api/v1/workflows/workflowExecutions/{jobId}
Get workflow using jobId
workflow-execute-controller
Operations allow execution with workflows
GET
/api/v1/execute/access/{workflowId}
checkWorkflowExecuteAccessForWebApp
POST
/api/v1/lib-jars
Returns the list of jar files under the fire-user-lib directory
GET
/api/v1/spark-configs
Returns the Spark Configuration for the username
POST
/api/v1/spark-job/messages
Consume the message sent from YarnRestWorkflowContext
POST
/api/v1/workflow-execution/{workflowExecutionId}/kill
Kills the execution of workflow
POST
/api/v1/workflow-execution/{workflowExecutionId}/stop
Stops the execution of workflow
POST
/api/v1/workflow-executions/kill
Kills the execution of workflow
POST
/api/v1/workflow-executions/stop
Stops workflow executions
POST
/api/v1/workflow/execute
Executes the workflow
workflow-executions-controller
Workflow Executions Controller
GET
/api/v1/cleaning-workflow-execution/{datasetUuid}
Get all Cleaning Workflow Execution
GET
/api/v1/last/workflow-execution/{workflowId}
Get last execution of workflow
GET
/api/v1/refreshTop10DatabricksJobStaus
Refresh top 10 databricks executions status
GET
/api/v1/summary-workflow-execution/{datasetUuid}
Get all Summary Workflow Execution
GET
/api/v1/update-status-workflow-execution/{wfeId}
Update status of Workflow Execution
GET
/api/v1/workflow-executions
Gets the workflow executions - Status - 0: RUNNING, 1 : STOPPED, 2 : COMPLETED, 3 : FAILED, 4: STARTING, 5: STOP, 6: KILLED, 7: STOPPING, 8: TIMEOUT, 9: PENDING, 10: SKIPPED
DELETE
/api/v1/workflow-executions
Delete Selected Workflow Executions
GET
/api/v1/workflow-executions/{parentExecutionId}
Get the nested workflow execution list
GET
/api/v1/workflow-executions/{workflowExecutionId}/logs/view
View logs for the workflow execution
GET
/api/v1/workflow-executions/{workflowExecutionId}/status
Get status by Workflow Execution Id
DELETE
/api/v1/workflow-executions/application/{applicationId}/days/{days}
Delete older Workflow Executions of application
GET
/api/v1/workflow-executions/application/count
Get Aplications' Workflow Execution count - Status - 0: RUNNING, 1 : STOPPED, 2 : COMPLETED, 3 : FAILED, 4: STARTING, 5: STOP, 6: KILLED
GET
/api/v1/workflow-executions/applications/{applicationId}/environments
Get Workflow environment list
GET
/api/v1/workflow-executions/applications/{applicationId}/jobs/{jobId}
Get Job details
GET
/api/v1/workflow-executions/applications/{applicationId}/stages
Get Workflow execution stage list
GET
/api/v1/workflow-executions/applications/{applicationId}/stages/jobs/{jobId}
Get Workflow execution stage details
GET
/api/v1/workflow-executions/count
Get Workflow Execution count - Status - 0: RUNNING, 1 : STOPPED, 2 : COMPLETED, 3 : FAILED, 4: STARTING, 5: STOP, 6: KILLED
DELETE
/api/v1/workflow-executions/days/{days}
Delete Workflow Executions by days
GET
/api/v1/workflow-executions/executors/applications/{applicationId}
Get Workflow executer list
GET
/api/v1/workflow-executions/jobs/applications/{applicationId}
Get Workflow execution job list
GET
/api/v1/workflow-executions/latest
Gets latest five workflow executions
GET
/api/v1/workflow-executions/projects/{projectId}
Gets latest five workflow executions of a project
GET
/api/v1/workflow-executions/status/{status}
Gets the status of Workflow Execution
GET
/api/v1/workflow-executions/summary
Gets the workflow executions summary. It includes all users' workflow executions
GET
/api/v1/workflow-executions/summary/all
API to get summary by date, status and duration
GET
/api/v1/workflow-executions/summary/date
API to get execution summary by date
GET
/api/v1/workflow-executions/tasks/count
Get Executed Task Count
POST
/api/v1/workflow-executions/update-status
Update status of selected Workflow Executions
GET
/api/v1/workflow-executions/workflows/{workflowId}
Lists the workflow executions for a given workflow
GET
/api/v1/workflowExecution/{workflowExecutionId}
Get Workflow Execution by workflowExecutionId
GET
/api/v1/worklow-executions/applications/{applicationId}/workflow-sqls
Get Workflow sql list
workflow-executions-result-controller
Operations allow accessing workflow execution results in Sparkflows
GET
/api/v1/execution-results/workflow-executions/{analysisFlowExecutionId}/resultType/{type}
View the workflow execution result
GET
/api/v1/execution-results/workflows/{workflowId}/nodes/{nodeId}/latest
View the latest execution result of workflow
workflow-scheduler-controller
Analysis Flow Scheduler in Sparkflows
POST
/api/v1/workflow-schedules
Schedule new Workflow
GET
/api/v1/workflow-schedules-list/{workflowId}
Get workflow Schedules list by workflow id
DELETE
/api/v1/workflow-schedules/{id}
Delete scheduled Workflow
GET
/api/v1/workflow-schedules/{workflow-scheduleId}
getWorklowScheduleDetails
GET
/api/v1/workflow-schedules/projects/{projectId}/workflows/{workflowId}
Get list of all Workflows Scheduled respect to project
yarn-controller
Yarn Controller
GET
/api/v1/viewYarnApplication/{applicationId}
View YARN application
GET
/api/v1/yarn/applicationList
Get YARN Jobs
Models

