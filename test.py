from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient


credential = DefaultAzureCredential()
subscription = "6312cb34-7d60-4d8a-b56a-3f952aa74df6"

def azure_vnet_list():
    for resource_list in ResourceManagementClient(credential, subscription).resources.list():
        if resource_list.type == "Microsoft.Network/virtualNetworks":
            print(f"{resource_list.name}")

def main():
    azure_vnet_list()


if __name__ == '__main__':
    main()