
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


credential = DefaultAzureCredential()
subscription = "6312cb34-7d60-4d8a-b56a-3f952aa74df6"

class demo():
     def get(resource_group_name: str, deployment_name: str, operation_id: str, **kwargs: Any) 
      -> azure.mgmt.resource.resources.v2016_02_01.models._models_py3.DeploymentOperation