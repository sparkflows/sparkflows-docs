
Sparkflows REST API’S
=========

Sparkflows enable you to use Swagger REST API’S.

Documentation
+++++

  - Reference guide : https://docs.sparkflows.io/en/latest/installation/monitoringandmetrics/rest-api.html


::

[ Base URL: localhost:8080/ ]
http://localhost:8080/v2/api-docs?group=fire
Sparkflows REST API Documentation
Terms of service


Sparkflows License Version 1.0

about-controller
++++++

About Controller

::
    
    # getBuildReleaseInfo
    
    
    GET /api/v1/app/release-info 
    
    
analysis-flow-trigger-controller
+++++++++

Analysis Flow Trigger Controller

::

    # getAllAnalysisflowTriggers
    
    GET /api/v1/workflow-triggers 
    
    # createAnalysisflowTrigger
    
    POST /api/v1/workflow-triggers 
    
    # getAnalysisflowTriggerDetails
    
    GET /api/v1/workflow-triggers/{analysisworkflowTriggerId} 
    
    # deleteAnalysisflowTriggerById
    
    DELETE /api/v1/workflow-triggers/{analysisWorkflowTriggerId} 
    

application-connection-controller
++++++++++++++++++++++++
Application Connection Controller

::
  
    # Create a connection
    
    POST /api/v1/connections 
    
    # deleteApplicationConnection
    
    DELETE /api/v1/connections/{appConnectionId} 
    
    # Get connection details by connectionId
    
    GET /api/v1/connections/{connectionId} 
    
    # getTables
    
    GET /api/v1/connections/{connectionId}/tables 
    
    # Update a connection details
    
    PUT /api/v1/connections/{id} 
    
    # getAllConnections
    
    GET /api/v1/connections/categories/{category} 
    
    # getGlobalConnections
    
    GET /api/v1/connections/global 
    
    # getConnectionsForLoggedInUser
    
    GET /api/v1/connections/loggedInUser 
    
    # getConnectionsPermissions
    
    GET /api/v1/connections/manage/access 
    
    # isUniqueConnectionName
    
    GET /api/v1/connections/name/{connectionName}/isUnique 
    
    # Get all connections by projectId
    
    GET /api/v1/connections/projects/{projectId} 
    
    # testConnection
    
    POST /api/v1/connections/test 
    
auth-permission-controller
++++++++++++++++++
Auth Permission Controller

::

    # Get User permissions
    
    GET /api/v1/user-permissions 
    
auth-user-group-controller
+++++++++++

Operations pertaining to User Group in Sparkflows
::

    # Get logged in User group
    
    GET /api/groups/user 
    
    # Get User by Group Id
    
    GET /api/v1/groups/{id} 
    
    # Get Group by User Id
    
    GET /api/v1/groups/user/{id} 
    
auth-user-role-controller
++++++++++++++

Operations pertaining to User Role in Sparkflows
::

    # Get Role by User Id
    
    GET /api/v1/roles/user/{id} 
    
auto-ml-controller
+++++++++++

Auto ML Controller
::

    # getAutoMlList
    
    GET /api/v1/auto-ml 
    
    # configureAutoMl
    
    POST /api/v1/auto-ml 
    
    # updateAutoMl
    
    PUT /api/v1/auto-ml 
    
    # getAutoMlDetails
    
    GET /api/v1/auto-ml/{autoMlId} 
    
    # deletAutoMl
    
    DELETE /api/v1/auto-ml/{autoMlId} 
    
    # getAutoMlListOfProject
    
    GET /api/v1/auto-ml/project/{projectId} 
    
    # startAutoMl
    
    POST /api/v1/auto-ml/start/{autoMlId} 

auto-ml-executions-controller
++++++++++++++++++

Auto ML Executions Controller
::

    # getAutoMlExecutionsByExecutionId
    
    GET /api/v1/auto-ml/execution/{autoMlExecutionId} 
    
    # setAutoMlExecutionsIsFavoriteOrNot
    
    POST /api/v1/auto-ml/execution/{autoMlExecutionId}/autoMl 
    
    # saveAutoMlExecutions
    
    POST /api/v1/auto-ml/execution/{executionId}/autoMl/{autoMlId} 
    
    # addCommentToAutoMlExecution
    
    POST /api/v1/auto-ml/execution/comment 
    
    # getAutoMlExecutions
    
    GET /api/v1/auto-ml/executions/{autoMlId} 
    
aws-controller
++++++++++++

Aws Controller
::

    # getAwsRoles
    
    GET /api/v1/aws/roles 
    
conf-property-controller
++++++++++++++++

Operations pertaining to Conf Property in Sparkflows
::

    # Get Application Configuration property
    
    GET /api/v1/configs/app 
    
    # Get configurations
    
    GET /api/v1/configurations 
    
    # Save/Update configurations
    
    POST /api/v1/configurations 
    
    # Infer configurations
    
    GET /api/v1/configurations/infer 
    
    # Get kafka configuration
    
    GET /api/v1/configurations/kafka 
    
    # Get Configuration property of ui settings
    
    GET /api/v1/configurations/uiSettings 
    
    # Get Configuration property of modules
    
    GET /api/v1/main/modules-enabled 
    
    # Get Configuration property of sso
    
    GET /api/v1/main/sso-conf 

credential-store-controller
+++++++++++++

Credential Store Controller
::

    # Get All CredentialStore details
    
    GET /api/v1/credentialStores 
    
    # Create CredentialStore
    
    POST /api/v1/credentialStores 
    
    # Update CredentialStore details
    
    PUT /api/v1/credentialStores 
    
    # delete CredentialStore details
    
    DELETE /api/v1/credentialStores/{credentialStoreId} 
    
    # Get CredentialStore details by id
    
    GET /api/v1/credentialStores/{id} 
    
    # Test CredentialStore details
    
    POST /api/v1/credentialStores/testDetails 

custom-processor-controller
++++++++++

Custom Processor Controller
::

    # Get Custom Processor for export
    
    GET /api/v1/processor/export/{customProcessorIds} 
    
    # Get custom processor
    
    GET /api/v1/processors 
    
    # Create custom processor
    
    POST /api/v1/processors 
    
    # Get custom processor by id
    
    GET /api/v1/processors/{customProcessorId} 
    
    # deleteCustomProcessor
    
    DELETE /api/v1/processors/{customProcessorId} 
    
    # Test custom processor
    
    POST /api/v1/processors/datasets/{datasetId} 
    
    # Import custom processor
    
    POST /api/v1/processors/import 
    
    # getCustomProcessorByName
    
    GET  /api/v1/processors/names 

dashboard-controller
+++++++++++

Operations pertaining to Dashboards in Sparkflows
::

    # Get all the dashborads
    
    GET /api/v1/dashboards 
    
    # Create dashboard
    
    POST /api/v1/dashboards 
    
    # update dashboard
    
    PUT /api/v1/dashboards/{dashboardId} 
    
    # Delete dashboard
    
    DELETE /api/v1/dashboards/{dashboardId} 
    
    # Get dashboard by Id
    
    GET /api/v1/dashboards/{id} 
    
    # Get all Dashboards
    
    GET /api/v1/dashboards/all 
    
    # getAllDashboardCategories
    
    GET /api/v1/dashboards/categories 
    
    # Get dashboard results
    
    GET /api/v1/dashboards/results 
    
data-quality-controller
++++++++

Data Quality Controller
::

    # Delete Data Quality Records by dataQuality ids
    
    DELETE /api/v1/dataQuality 
    
    # Api for data-quality summary
    
    GET /api/v1/dataQuality/summary 
    
    # Create summary workflow
    
    POST /api/v1/summaryWorkflow/{projectId}/{datasetUuid} 
    
    # api for get data validation by dataQualityUuid
    
    GET /api/vi/data-quality/validation/{dataQualityUuid} 
    
    # api for get all data quality
    
    GET /api/vi/dataQuality 
    
    # api for get data quality by dataQualityUuid
    
    GET /api/vi/dataQuality/{dataQualityUuid} 
    
    # api for getting the data quality record counts
    
    GET /api/vi/dataQuality/counts 
    
    # Api for creating and executing dataset summary workflow
    
    POST /api/vi/executeSummaryWorkflow/{projectId}/{datasetUuid} 

data-set-controller
++++++++

Operations pertaining to Datasets in Sparkflows
::

    # Get all datasets
    
    GET /api/v1/datasets 
    
    # Create Dataset
    
    POST /api/v1/datasets 
    
    # Delete Dataset
    
    DELETE /api/v1/datasets 
    
    # Get Dataset by Id
    
    GET /api/v1/datasets/{datasetId} 
    
    # clone the dataset
    
    POST /api/v1/datasets/{datasetId}/{datasetName}/clone 
    
    # getAllDatasetCategories
    
    GET /api/v1/datasets/categories 
    
    # Get Dataset Count
    
    GET /api/v1/datasets/count 
    
    # Get sample data from given DB and Table
    
    GET /api/v1/datasets/hive/sample-data 
    
    # Get Latest Five Datasets
    
    GET /api/v1/datasets/latest 
    
    # Get Latest Five Datasets
    
    GET /api/v1/datasets/list/export 
    
    # Get Datasets by project Id
    
    GET /api/v1/datasets/projects/{projectId} 
    
    # Get Read Options of Datasets
    
    GET /api/v1/datasets/read-options 
    
    # Returns sample data
    
    POST /api/v1/datasets/sample-data 
    
    # schema of the files in the given path using the given delimiter
    
    POST /api/v1/datasets/schema Returns 
    
    # Get user owned and shared datasets
    
    GET /api/v1/datasets/users 

databricks-controller
+++++++

Databricks Controller
::

    # getClusterInfo
    
    GET /api/v1/databricks/clusters 
    
    # restartDatabricksClusters
    
    GET /api/v1/databricks/clusters/restart 
    
    # executeDatabricksDDLCommand
    
    POST /api/v1/databricks/command 
    
    # getTableColumnsInfo
    
    GET /api/v1/databricks/database/{dbName}/table/{table} 
    
    # getAllDatabases
    
    GET /api/v1/databricks/database/{dbName}/tables 
    
    # getSampleData
    
    GET /api/v1/databricks/database/{dbName}/tables/{tableName}/sample-data 
    
    # getAllDatabases
    
    GET /api/v1/databricks/database/list 
    
    # getRunDetailsByRunId
    
    GET /api/v1/databricks/jobs/runs 
    
    # getDatabricksNotebooksJob
    
    GET /api/v1/databricks/notebooks/jobs 
    
    # executeDatabricksNotebooksJob
    
    POST /api/v1/databricks/notebooks/jobs/execute 
    
    # getQueryHistoryOfLoggedInUser
    
    GET /api/v1/databricks/query/history 
    
    # getDatabricksFileSystem
    
    GET /api/v1/dbfs 
    
    # Delete DBFS files via It's Paths
    
    DELETE /api/v1/dbfs/delete 
    
    # getDatabricksFileSystemInDir
    
    GET /api/v1/dbfs/directory 
    
    # getDbfsFileContent
    
    GET /api/v1/dbfs/fileContent 
    
    # download dbfs file
    
    GET /api/v1/dbfs/files/download 
    
    # uploadDbfsFile
    
    POST /api/v1/dbfs/files/upload 
    
    # createDbfsDir
    
    POST /api/v1/dbfs/mkdir 
    
    # moveOrRenameFile
    
    POST /api/v1/dbfs/renameOrMove/file 
 
dataset-hierarchy-controller 
++++++++++

Dataset Hierarchy Controller
::

    # createDatasetHierarchy
    
    POST /api/v1/hierarchy 
    
    # updateDatasetHierarchy
    
    PUT /api/v1/hierarchy 
    
    # deleteDatasetHierarchy
    
    DELETE /api/v1/hierarchy/{datasetHierarchyId} 
    
    # getDatasetHierarchy
    
    GET /api/v1/hierarchy/datasets/{datasetUuid} 

datasource-controller
++++++++++++

Datasource Controller
::

    # getDatasourceConnectionPoolInfo
    
    GET /api/v1/datasource/metrics 

diagnostics-controller
++++++++++++++

Diagnostics Controller
::
 
    # Get all diagnostics
    
    GET /api/v1/getDiagnostics 

event-controller
++++++++++

Event Controller
::

    # deleteEventsByDays
    
    DELETE /api/v1/events/{days} 
    
    # getProjectEvents
    
    GET /api/v1/events/project 
    
    # listAllEvents
    
    GET /api/v1/events/search 
    
    # getTotalEventCountByAllUsers
    
    GET /api/v1/operations/events/total 
    
    # api for getting the Event record counts
    
    GET /api/vi/events/counts 

fire-access-token-controller
+++++++++

Fire Access Token Controller
::

    # getFireAccessTokens
    
    GET /api/v1/tokens 
    
    # generateToken
    
    POST /api/v1/tokens 
    
    # getFireAccessTokenDetails
    
    GET /api/v1/tokens/{id} 
    
    # deleteFireAccessTokenById
    
    DELETE /api/v1/tokens/{id} 

git-integration-controller
++++++++

Git Integration Controller
::

    # createBranch
    
    POST /api/v1/git/branch/create 
    
    # getBranchList
    
    GET /api/v1/git/branches 
    
    # cloneFromGit
    
    GET /api/v1/git/clone 
    
    # getCredentials
    
    GET /api/v1/git/credentials 
    
    # Update Git Credentials
    
    POST /api/v1/git/credentials 
    
    # linkProject
    
    POST /api/v1/git/link 
    
    # linkedProjects
    
    GET /api/v1/git/linkedProjects 
    
    # getProjectListInGit
    
    GET /api/v1/git/projectList 
    
    # unLinkProjects
    
    POST /api/v1/git/projects/unlink 
    
    # pushProjectToGit
    
    POST /api/v1/git/push/project/{projectId} 
    
    # pushWorkflowToGit
    
    POST /api/v1/git/push/workflow 
    
    # pushWorkflowsToGit
    
    POST /api/v1/git/push/workflows 
    
    # pushWorkflowVersionToGit
    
    POST /api/v1/git/push/workflowVersion 
    
    # headCommitAndlatestchangesOfWorkflowJson
    
    GET /api/v1/git/workflow/headCommitAndLatest/{workflowId} 
    
    # getUncheckedWorkflowList
    
    GET /api/v1/git/workflow/status/{projectId} 

glue-controller
+++++++++++

Glue Controller
::

    # getJobDetails
    
    GET /api/v1/glue/connections/{connectionId}/jobs/{jobName} 
    
    # getJobRun
    
    GET /api/v1/glue/jobs/run/{jobName} 
    
group-admin-controller
++++++++

Operations pertaining to Group in Sparkflows
::

    # Get Group by Id
    
    GET /api/groups/{groupId} 
    
    # Get all Groups
    
    GET /api/v1/groups 
    
    # Create Group
    
    POST /api/v1/groups 
    
    # Delete Group
    
    DELETE /api/v1/groups/{groupId} 

hdfs-controller
+++++++

Operations pertaining to HDFS in Sparkflows
::

    # Returns list of all the files on hdfs in the users home directory
    
    GET /api/v1/hdfs 
    
    # Get HDFS Configurations
    
    GET /api/v1/hdfs/configurations 
    
    # Create HDFS directory
    
    POST /api/v1/hdfs/dir/create 
    
    # Returns list of files in HDFS in the specified directory for download from folder
    
    GET /api/v1/hdfs/dir/files 
    
    # Returns list of files in HDFS in the specified directory
    
    GET /api/v1/hdfs/dir/open 
    
    # Returns list of all the files on hdfs in the users home directory in sorted order
    
    GET /api/v1/hdfs/files 
    
    # Delete HDFS files via It's Paths
    
    DELETE /api/v1/hdfs/files/delete 
    
    # download hdfs file
    
    GET /api/v1/hdfs/files/download 
    
    # Move HDFS File
    
    GET /api/v1/hdfs/files/move 
    
    # Move HDFS File
    
    POST /api/v1/hdfs/files/moves 
    
    # Accepts HDFS file path and returns first X bytes of content
    
    GET /api/v1/hdfs/files/open 
    
    # Change file permissions of HDFS File
    
    GET /api/v1/hdfs/files/permissions/change 
    
    # Rename HDFS File
    
    GET /api/v1/hdfs/files/rename 
    
    # Uploads file
    
    POST /api/v1/hdfs/files/upload 
    
    # Returns path of user's home directory
    
    GET /api/v1/hdfs/user/home-dir 

help-controller
++++++

Help Controller
::

    # getHelpContent
    
    GET /api/v1/helps/{contentType} 

hive-controller
+++++++++

Operations pertaining to Hive in Sparkflows
::

    # Execute HIVE Command
    
    POST /api/v1/hive/command/execute 
    
    # Get all Hive Databases
    
    GET /api/v1/hive/databases 
    
    # Get all Hive Tables for given db
    
    GET /api/v1/hive/tables 

icon-controller
++++

Icon Controller
::

    # getIcons
    
    GET /api/v1/icons 
    
interactive-dashboard-controller
++++++

Operations pertaining to Interactive Dashboards
::

    GET /api/v1/i-dashboards Get all the interactive dashboards
    POST /api/v1/i-dashboards Create interactive dashboard
    PUT /api/v1/i-dashboards/{dashboardId} Update interactive dashboard
    DELETE /api/v1/i-dashboards/{dashboardId} Delete interactive dashboard
    GET /api/v1/i-dashboards/{id} Get interactive dashboard by Id
    POST /api/v1/i-dashboards/chart-data Get Chart Data
    GET /api/v1/i-dashboards/datasets Get all the Interactive Datasets
    GET /api/v1/i-dashboards/datasets/uuid/{uuid} Get Interactive Dataset by uuid
    POST /api/v1/i-dashboards/filter Filter Request
    PUT /api/v1/i-dashboardsarranged/{dashboardId} Update interactive dashboard
    POST /api/v2/i-dashboards Create or update interactive dashboards
    PUT /api/v2/i-dashboards Create or update interactive dashboards
    GET /api/v2/i-dashboards/{dashboardId} getArrangedInteractiveDashobardDetails
    DELETE /api/v2/i-dashboards/{dashboardId} deleteInteractiveDashobard
    GET /api/v2/i-dashboards/projects/{projectId} getArrangedInteractiveDashobards

ldap-config-controller
+++++++++

Ldap Config Controller
::

    GET /api/ldapConfigurations Api To Get the Ldap Configuration
    POST /api/testLdapConnection Api To Test the Ldap Connection
    PUT /api/updateLdapConfigurations Api To Update the Ldap configurations

logs-controller
++++++

Logs Controller
::

    GET /api/fireLogs View logs of fire
    GET /api/fireServer/exceptions/logs View logs of fire server
    GET /api/fireServerLogs View logs of fire server
    GET /api/pysparkLogs View pyspark server log
    GET /api/search/logs/{logName}/{searchString} Search logs

main-controller
+++++++++++

Operations pertaining to Main Ctrl in Sparkflows
::

    GET /api/v1/main/about Get Sparkflows details
    GET /api/v1/main/databricks-enabled/{name} Get Configuration property of databricks by Name

metrics-controller
++++

Metrics Controller
::

    GET /api/v1/metrics/summary/{analysisFlowId} Gets the workflow metrics summary. It includes all users' workflow executions
    GET /api/v1/metrics/summary/{analysisFlowId}/time/{timeFilter} Gets the workflow executions summary by time/date filter. It includes all users' workflow executions
    GET /api/v1/workflow/metrics/{workflowExecutionId} Get job execution metrics for the given workflow execution id
    GET /api/v1/workflow/metrics/getAllMetricsOfEachWorkflow/{workflowId} Get all execution metrics for the given workflow id

model-controller
++++++++++

Model Controller
::

    DELETE /api/v1/mlmodel/delete/{analysisFlowId} Delete output model of job executions by workflow id
    GET /api/v1/mlmodel/getFeatureImportanceByModelUuid/{modelUuid} Get feature importance by model uuid
    GET /api/v1/mlmodel/getMlDetailByModelUuid/{modelUuid} Get model detail by model uuid
    GET /api/v1/mlmodel/getMLModelFeatures/{modelUuid} Get the features of given model uuid
    GET /api/v1/mlmodel/getTestMetricsByModelUuid/{modelUuid} Get test metrics from output model evaluation by model uuid
    GET /api/v1/mlmodel/getTrainMetricsByModelUuid/{modelUuid} Get train metrics by model uuid
    GET /api/v1/mlmodel/model_Summary_analysisflow/{analysisFlowId} Get output model summary by analysisFlowId
    GET /api/v1/mlmodel/model_Summary_analysisflow/{analysisFlowId}/time/{timeFilter} Get output model summary by time/date filter
    GET /api/v1/mlmodel/model_Summary/{modelUuid} Get output model summary by model uuid
    GET /api/v1/mlmodel/outputModel Get all output model
    GET /api/v1/mlmodel/outputModel/{analysisflowExecutionId} Get output model of job executions
    GET /api/v1/mlmodel/outputModel/{modelId}/download/{fileType} zipDownload
    GET /api/v1/mlmodel/outputModelByAnalysisFlowId/{analysisFlowId} Get all output model of job executions by workflow id
    GET /api/v1/mlmodel/outputModelByApplicationId/{applicationId} Get output model of job executions by application id
    GET /api/v1/mlmodel/outputModelByModelUuid/{modelUuid} Get output model by model uuid
    GET /api/v1/mlmodel/OutputModelEvaluationByModelUuid/{modelUuid} Get output model evaluation by model uuid
    GET /api/v1/mlmodel/OutputModels Get output model list
    GET /api/v1/mlmodel/OutputModels/fileInfo getFileInfo
    GET /api/v1/mlmodel/OutputModelsById/{modelId} Get output model list by id
    GET /api/v1/mlmodel/summary Gets the model executions summary
    POST /api/v1/mlmodel/updateModel/{modelId} Update model

node-controller
++++++++++++++++

Operations pertaining to processors in Sparkflows
::

    GET /api/v1/node-rules Returns list of node rules
    GET /api/v1/nodes Gets list of available processors by engine or leave it blank for all processors.
    GET /api/v1/nodes/count Get Node Count
    GET /api/v1/nodes/names/{name} Return processor details by name
    GET /api/v2/nodes Gets list of available processors by engine or leave it blank for all processors.

operations-controller
++++++++++

Operations Controller
::
    
    DELETE /api/v1/operations/workflows/deleteAllExecutions deleteAllExecutions
    DELETE /api/v1/operations/workflows/executions delete older workflow executions and its results.
    GET /api/v1/operations/workflows/executions/count Get Workflow execution counts
    GET /api/v1/operations/workflows/executions/count/days/{days} getTotalWorkflowExecutionCountByOlderDays
    GET /api/v1/operations/workflows/executions/results/count Get workflow execution results count
    GET /api/v1/operations/workflows/executions/total getTotalWorkflowExecutionCountByAllUsers

pipeline-controller
+++++++++++
Operations pertaining to Pipeline in Fire
::

    GET /api/retrievePipelineVersions Retrieve the pipeline versions
    POST /api/v1/pipelines/import importPipeline

pipeline-execute-controller
++++++++++

Pipeline Execute Controller
::

    GET /api/executePipeline Execute the pipeline
    GET /api/v1/pipeline/executions/project/{projectId} getPipelineExecutionListByProjectId
    GET /api/v1/pipelines/execution/{pipelineExecutionId} getPipelineExecutionDetailsById
    DELETE /api/v1/pipelines/execution/{pipelineExecutionId} deletePipelineExecutionById
    GET /api/v1/pipelines/execution/{pipelineExecutionId}/airflow/refreshStatus refreshStatusByAirflow
    GET /api/v1/pipelines/execution/{pipelineExecutionId}/refreshStatus refreshPipelineStatus
    GET /api/v1/pipelines/execution/logs getLogs
    GET /api/v1/pipelines/execution/task getTaskDetails

pipeline-node-controller
+++++++++++++

Pipeline Node Controller
::

    GET /api/v1/pipelines/nodes getAllPipelineNodes
    GET /api/v1/pipelines/nodes/{name} getPipelineNodeByName

pipeline-scheduler-controller
++++++++++++

Pipeline Scheduler Controller
::

    POST /api/v1/pipeline-schedules Schedule new pipeline
    PUT /api/v1/pipeline-schedules Update Scheduled pipeline
    GET /api/v1/pipeline-schedules/{pipelineScheduleId} getPipelineScheduleDetails
    DELETE /api/v1/pipeline-schedules/{pipelineScheduleId} Delete scheduled pipeline
    GET /api/v1/pipeline-schedules/list/{pipelineId} Get pipeline Schedules list by pipeline id

project-controller
++++++++++

Project Controller
::

    GET /api/v1/apps/example-datasets-and-workflows/reload Reload Example datasets and workflows of Applications
    GET /api/v1/apps/existing/sampleProject Get Available Sample Projects
    DELETE /api/v1/apps/sampleProject Delete Existing Sample Projects
    GET /api/v1/project/info Get id and name detail of logged in user projects
    GET /api/v1/project/isOwner/{projectId} isProjectOwner
    GET /api/v1/projects getAllUserProjects
    POST /api/v1/projects createProject
    GET /api/v1/projects/{projectId} Get project details by project id
    PUT /api/v1/projects/{projectId} updateProject
    DELETE /api/v1/projects/{projectId} deleteProject
    POST /api/v1/projects/{projectId}/generateUuid Generate uuid of project
    PUT /api/v1/projects/{projectId}/tags updateProjectTag
    GET /api/v1/projects/connections/{connectionId} Get all projects by connectionId
    GET /api/v1/projects/count applicationsCount
    POST /api/v1/projects/generateUuid Generate uuid of project by project name
    POST /api/v1/projects/import importProjects
    POST /api/v1/projects/importFromGit importProjectsFromGit
    POST /api/v1/projects/multiple/import import multiple project
    GET /api/v1/projects/name/{projectName} Get project details by project name
    GET /api/v1/projects/users/logged-in Get projects of logged in user (user's own and shared with him) projects
    GET /api/v1/projects/uuidExists does same uuid exists in any project
    GET /api/v1/reload/selected/sampleProject/{selectedProjectId} Reload Selected Sample Projects

project-discussion-controller
++++++++

Project Discussion Controller
::

    GET /api/v1/getProjectDiscussions/{projectId} Get All Project Discussions By ProjectId
    POST /api/v1/projectDiscussion Create Discussion For Project
    DELETE /api/v1/projectDiscussion/{discussionId} Delete discussion from Project

project-overview-controller
++++++++++++

Project Overview Controller
::

    GET /api/v1/projectOverview/counts/{projectId} getProjectElementInfo

project-permission-controller
+++++++++

Project Permission Controller
::

    GET /api/v1/groups/projects/{projectId} getGroupByprojectId
    POST /api/v1/project-permissions saveShareProjectInfo
    GET /api/v1/project-permissions/{projectPermissionId} Get project-permission details by id
    DELETE /api/v1/project-permissions/{projectPermissionId} deleteProjectPermission
    GET /api/v1/project-permissions/projects/{projectId} Get project permissions by projectId
    GET /api/v1/project-permissions/projects/{projectId}/groups/{groupId} getProjectPerByProjectIdAndGroupId

properties-controller
+++++++

Properties Controller
::

    GET /api/v1/user/swagger/enabled getSwaggerStatus
    POST /api/v1/user/swagger/status/{enableSwagger} setSwaggerStatus

recommendation-controller
++++++++++

Recommendation Controller
::

    GET /api/v1/recommendations/nodes Gets recommended node mapping list
    GET /api/v1/recommendations/nodes/refresh Refresh node mapping list

role-admin-controller
++++++++++

Operations pertaining to Role in Sparkflows
::

    GET /api/v1/permissions Get all Permissions
    GET /api/v1/role-permissions/roles/{id} Get Role Permissions by Role Id
    GET /api/v1/role-permissons/roles/{id} Get Role Permissions by Role Id
    GET /api/v1/roles Get user Roles
    POST /api/v1/roles Create Role
    GET /api/v1/roles/{id} Get Role Name by Id
    DELETE /api/v1/roles/{id} Delete Role by Role Name

run-time-statistics-controller
+++++++++++++++++++

Run Time Statistics Controller
::

    GET /api/v1/runTimeStatistics Get Run time statistics

s-3-controller
++++++++

Operations pertaining to S3 bucket in Sparkflows
::

    GET /api/v1/aws-s3/directory/create Create directory in s3
    DELETE /api/v1/aws-s3/file Delete file from s3
    GET /api/v1/aws-s3/file/rename Rename folder/file of s3
    DELETE /api/v1/aws-s3/folder Delete folder from s3
    GET /api/v1/aws/home-dir Returns value of aws home directory
    GET /api/v1/s3-buckets/aws-config-available return true or false to make it sure that aws s3 is configured at aws cli level
    GET /api/v1/s3-buckets/configs Returns list of buckets in S3 by reading access key and secret key from configuration
    GET /api/v1/s3-buckets/fileContent Returns content of a file of s3
    GET /api/v1/s3-buckets/name/{bucketName} Returns list of files in S3 bucket directory
    POST /api/v1/s3-buckets/uploadFile Upload file to s3

search-controller
++++++++

Controller for searching workflows, datasets and dashboard by name
::

    GET /api/v1/search/{searchType}/{searchItem} Search workflows, dataset and dashboard by name.

snowflake-controller
+++++++++

Snowflake Controller
::

    POST /api/v1/snowflake/command executeSnowflakeDDLCommand
    GET /api/v1/snowflake/database/{dbName}/table/{table} getTableColumnsInfo
    GET /api/v1/snowflake/database/{dbName}/tables getDatabaseTables
    GET /api/v1/snowflake/database/{dbName}/tables/{tableName}/sample-data getSampleData
    GET /api/v1/snowflake/database/list get snowflake database list
    GET /api/v1/snowflake/schema/{dbName}/list getAllSchema
    GET /api/v1/snowflake/warehouse/list getAllWarehouse

user-admin-controller
+++++++++++

Operations pertaining to Admin in Sparkflows
::

    GET /api/users/ldap/{username} Add LDAP user
    GET /api/v1/configurations/ldap/enable Get LDAP configuration
    PUT /api/v1/user/currentConnection/{connectionId} set the user current connection
    PUT /api/v1/user/currentProject/{projectId} set the user current project
    GET /api/v1/user/isAdmin/isSuperuser Check user is admin/ superuser
    GET /api/v1/users Get list of Users
    POST /api/v1/users Create User
    PUT /api/v1/users Update User
    GET /api/v1/users/{id} Get user by user Id
    DELETE /api/v1/users/{id} Delete User by user id
    GET /api/v1/users/{name}/validate Validates user Name
    GET /api/v1/users/basicInfo Get list of Users
    GET /api/v1/users/configurations Get Configurations
    GET /api/v1/users/password/change change password
    POST /api/v1/users/password/verify verifies password
    PUT /api/v1/users/profile update user basic profile (firstName, LastName, and email only
    GET /api/v1/users/UsageStatistics Get Usage Statistics
    GET /api/v1/users/user-info Get current logged-In User

web-app-controller
++++++++

Web App Controller
::

    GET /api/v1/webApps getWebApps
    POST /api/v1/webApps createWebApp
    PUT /api/v1/webApps updateWebApp
    POST /api/v1/webApps/{uuid}/userInputs saveInput 
    GET /api/v1/webApps/{webAppId} getWebAppDetails
    PUT /api/v1/webApps/{webAppId} changeWebAppStatus
    DELETE /api/v1/webApps/{webAppId} deleteWebApp
    GET /api/v1/webApps/{webAppId}/by/condition getWebAppDetailsByCondition
    POST /api/v1/webApps/{webAppId}/generateUuid Generate uuid of app
    POST /api/v1/webApps/{webAppId}/nextStage getNextStage
    POST /api/v1/webApps/{webAppId}/saveUuid Save uuid of app
    GET /api/v1/webApps/{webAppId}/stage getWebAppStageDetails
    POST /api/v1/webApps/{webAppId}/stage addWebAppStage
    DELETE /api/v1/webApps/{webAppId}/stage/{stageId} deleteWebAppStage
    POST /api/v1/webApps/{webAppId}/stage/details addWebAppStageDetails 
    POST /api/v1/webApps/browseFile/uuidExists Webapp exists with uuid present in browse json file
    POST /api/v1/webApps/dbfs/upload/file uploadFile
    GET /api/v1/webApps/execution/{executionId} getWebappExecutionById
    POST /api/v1/webApps/import Import analytic app
    GET /api/v1/webApps/polls/{uuid}/userInputs pollUserInput
    DELETE /api/v1/webApps/project/{projectId} deleteAllWebappsByProjectId
    POST /api/v1/webApps/showHideApps show hide apps
    PUT /api/v1/webApps/stage updateStage
    POST /api/v1/webApps/updateWfParameters/{wfId} updateWfParameters
    POST /api/v1/webApps/upgrade Upgrade analytic app
    GET /api/v1/webApps/uuidExists does same uuid of app exists in project

web-app-version-controller
++++++++++

Web App Version Controller
::

    GET /api/v1/webappVersions/{webVersionId} getWebAppDetailsByWebVersionId
    GET /api/v1/webappVersions/webApps/{webAppId} getWebAppVersionsByWebAppId

wizard-controller
++++++++++++

Operations pertaining to wizard in Fire
::

    GET /api/v1/wizards/actions Returns actions
    POST /api/v1/wizards/convert-workflow Convert WizardWorkflow to Workflow
    GET /api/v1/wizards/queries Returns queries
    GET /api/v1/wizards/sections Returns sections
    POST /api/v1/wizards/workflow/create Create Workflow from workflow-wizard

workflow-controller
++++++++++++

Operations allow interacting with workflows in Sparkflows
::

    GET /api/v1/apps/example-datasets-and-workflows/load load Example datasets and workflows of Applications
    GET /api/v1/getAllCleaningWorkflows/{datasetUuid} Get all cleaning workflows
    GET /api/v1/ibm-file writes all the workflows to IBM file
    POST /api/v1/nodes/{nodeId}/schema/input Retrieve schema of a node
    POST /api/v1/nodes/{nodeId}/schema/output retrieve output schema of a node
    DELETE /api/v1/workflow/trash Move selected workflow to trash
    DELETE /api/v1/workflow/trash/{workflowId} Move workflow to trash
    GET /api/v1/workflows Get all the workflows for a given project in desc order with detailed information'
    POST /api/v1/workflows create a workflow
    PUT /api/v1/workflows update a workflow
    GET /api/v1/workflows/{id} Get workflow details by id
    DELETE /api/v1/workflows/{workflowId} delete the workflow
    POST /api/v1/workflows/{workflowId}/{workflowName}/clone clone the workflow
    GET /api/v1/workflows/{workflowId}/copy Api for copying the workflow
    GET /api/v1/workflows/{workflowId}/lock lock the workflow
    GET /api/v1/workflows/{workflowId}/unlock Unlock the workflow
    PUT /api/v1/workflows/{workflowId}/uuid/{uuid} updateUuid
    GET /api/v1/workflows/all Get all workflows
    POST /api/v1/workflows/beautify Beautify workflow
    GET /api/v1/workflows/count Get Workflow Count
    GET /api/v1/workflows/dashboard Get all the workflows of a project in desc order with basic information'
    DELETE /api/v1/workflows/emptyTrash empty wfs from trash
    GET /api/v1/workflows/execution-enable Get the value of execute enabled value of Configurations
    GET /api/v1/workflows/export/{id} Get workflow content to export
    POST /api/v1/workflows/generatePysparkCode Generate Pyspark Code
    GET /api/v1/workflows/latest Get Latest WorkFlows
    GET /api/v1/workflows/list/export Get Workflows for export
    GET /api/v1/workflows/name/{name} Get workflow by Name
    POST /api/v1/workflows/nodes/{nodeId}/execute Execute workflow's node
    GET /api/v1/workflows/nodes/state/inconsistent Return the list of nodes that are in an inconsistent state - mainly with regard to schema
    PUT /api/v1/workflows/restore Restore selected trashed wfs'
    PUT /api/v1/workflows/restore/{workflowId} Restore trashed wfs'
    GET /api/v1/workflows/trashed Get trashed workflows for a given project in desc order with detailed information'
    GET /api/v1/workflows/users/logged-in Get workflows owned and shared with logged-in user
    GET /api/v1/workflows/uuid/{uuid} Get workflow by uuid
    POST /api/v1/workflows/validateCode Api for syntax checking of pyspark code
    GET /api/v1/workflows/versions Retrieve the workflow versions
    GET /api/v1/workflows/wfName/{id} Get workflow name by id
    GET /api/v1/workflows/workflowExecutions/{jobId} Get workflow using jobId

workflow-execute-controller
++++++++++++

Operations allow execution with workflows
::

    GET /api/v1/execute/access/{workflowId} checkWorkflowExecuteAccessForWebApp
    POST /api/v1/lib-jars Returns the list of jar files under the fire-user-lib directory
    GET /api/v1/spark-configs Returns the Spark Configuration for the username
    POST /api/v1/spark-job/messages Consume the message sent from YarnRestWorkflowContext
    POST /api/v1/workflow-execution/{workflowExecutionId}/kill Kills the execution of workflow
    POST /api/v1/workflow-execution/{workflowExecutionId}/stop Stops the execution of workflow
    POST /api/v1/workflow-executions/kill Kills the execution of workflow
    POST /api/v1/workflow-executions/stop Stops workflow executions
    POST /api/v1/workflow/execute Executes the workflow
    
workflow-executions-controller
+++++++++++

Workflow Executions Controller
::

    GET /api/v1/cleaning-workflow-execution/{datasetUuid} Get all Cleaning Workflow Execution
    GET /api/v1/last/workflow-execution/{workflowId} Get last execution of workflow
    GET /api/v1/refreshTop10DatabricksJobStaus Refresh top 10 databricks executions status
    GET /api/v1/summary-workflow-execution/{datasetUuid} Get all Summary Workflow Execution
    GET /api/v1/update-status-workflow-execution/{wfeId} Update status of Workflow Execution
    GET /api/v1/workflow-executions Gets the workflow executions - Status - 0: RUNNING, 1 : STOPPED, 2 : COMPLETED, 3 : FAILED, 4: STARTING, 5: STOP, 6: KILLED, 7: STOPPING, 8: TIMEOUT, 9: PENDING, 10: SKIPPED
    DELETE /api/v1/workflow-executions Delete Selected Workflow Executions
    GET /api/v1/workflow-executions/{parentExecutionId} Get the nested workflow execution list
    GET /api/v1/workflow-executions/{workflowExecutionId}/logs/view View logs for the workflow execution
    GET /api/v1/workflow-executions/{workflowExecutionId}/status Get status by Workflow Execution Id
    DELETE /api/v1/workflow-executions/application/{applicationId}/days/{days} Delete older Workflow Executions of application
    GET /api/v1/workflow-executions/application/count Get Aplications' Workflow Execution count - Status - 0: RUNNING, 1 : STOPPED, 2 : COMPLETED, 3 : FAILED, 4: STARTING, 5: STOP, 6: KILLED
    GET /api/v1/workflow-executions/applications/{applicationId}/environments Get Workflow environment list
    GET /api/v1/workflow-executions/applications/{applicationId}/jobs/{jobId} Get Job details
    GET /api/v1/workflow-executions/applications/{applicationId}/stages Get Workflow execution stage list
    GET /api/v1/workflow-executions/applications/{applicationId}/stages/jobs/{jobId} Get Workflow execution stage details
    GET /api/v1/workflow-executions/count Get Workflow Execution count - Status - 0: RUNNING, 1 : STOPPED, 2 : COMPLETED, 3 : FAILED, 4: STARTING, 5: STOP, 6: KILLED
    DELETE /api/v1/workflow-executions/days/{days} Delete Workflow Executions by days
    GET /api/v1/workflow-executions/executors/applications/{applicationId} Get Workflow executer list
    GET /api/v1/workflow-executions/jobs/applications/{applicationId} Get Workflow execution job list
    GET /api/v1/workflow-executions/latest Gets latest five workflow executions
    GET /api/v1/workflow-executions/projects/{projectId} Gets latest five workflow executions of a project
    GET /api/v1/workflow-executions/status/{status} Gets the status of Workflow Execution
    GET /api/v1/workflow-executions/summary Gets the workflow executions summary. It includes all users' workflow executions
    GET /api/v1/workflow-executions/summary/all API to get summary by date, status and duration
    GET /api/v1/workflow-executions/summary/date API to get execution summary by date
    GET /api/v1/workflow-executions/tasks/count Get Executed Task Count
    POST /api/v1/workflow-executions/update-status Update status of selected Workflow Executions
    GET /api/v1/workflow-executions/workflows/{workflowId} Lists the workflow executions for a given workflow
    GET /api/v1/workflowExecution/{workflowExecutionId} Get Workflow Execution by workflowExecutionId
    GET /api/v1/worklow-executions/applications/{applicationId}/workflow-sqls Get Workflow sql list

workflow-executions-result-controller
++++++++++++++

Operations allow accessing workflow execution results in Sparkflows
::

    GET /api/v1/execution-results/workflow-executions/{analysisFlowExecutionId}/resultType/{type} View the workflow execution result
    GET /api/v1/execution-results/workflows/{workflowId}/nodes/{nodeId}/latest View the latest execution result of workflow

workflow-scheduler-controller
++++++++

Analysis Flow Scheduler in Sparkflows
::

    POST /api/v1/workflow-schedules Schedule new Workflow
    GET /api/v1/workflow-schedules-list/{workflowId} Get workflow Schedules list by workflow id
    DELETE /api/v1/workflow-schedules/{id} Delete scheduled Workflow
    GET /api/v1/workflow-schedules/{workflow-scheduleId} getWorklowScheduleDetails
    GET /api/v1/workflow-schedules/projects/{projectId}/workflows/{workflowId} Get list of all Workflows Scheduled respect to project

yarn-controller
++++++++++++

Yarn Controller
::

    GET /api/v1/viewYarnApplication/{applicationId} View YARN application
    GET /api/v1/yarn/applicationList Get YARN Jobs

