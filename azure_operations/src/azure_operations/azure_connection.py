import logging
from azure.storage.blob import BlobServiceClient

from .azure_container import AzureContainer
from .url_container import UrlContainer


class AzureConnection():

    def __init__(self, connection_string):
        try:
            self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            logging.info("The system has connected to Azure storage blob")
            
        except Exception as e:
            logging.error(f"Connecting to Azure failed {str(e)}")
            raise ValueError(f"Connecting to Azure failed {str(e)}")
                
    def get_connect(self): 
        return self.blob_service_client
    
    def get_account(self):
        '''The function returns the name of the account. '''
        
        return self.blob_service_client.account_name
    
    def get_account_key(self):
        '''The function returns the key of the account. '''
        
        return self.blob_service_client.credential.account_key

    def get_azure_container(self, container_name):
        '''The function returns an instance of the AzureContainer class 
        on which the functions related to the container are performed. '''
        
        return AzureContainer(self.blob_service_client.get_container_client(container_name))

    def get_url_container(self, container_name):
        '''The function returns an instance of the UrlContainer class 
        which creates a URL adapted to the requested container. '''
        
        return UrlContainer(container_name, self.get_account(), self.get_account_key())
