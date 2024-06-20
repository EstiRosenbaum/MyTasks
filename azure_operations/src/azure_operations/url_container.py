import logging
from datetime import datetime, timedelta

from azure.storage.blob import generate_container_sas, ContainerSasPermissions


class UrlContainer():
    def __init__(self, container_name, account_name, account_key):
        self.container_name = container_name
        self.account_name = account_name
        self.account_key = account_key
        
        logging.info("Creating an instance from the GenerateUrlContainer class .")

    def generate_url(self, folder_name):
        '''The function receives a folder name and returns a url for the folder in the requested container. '''
        
        sas_token = self._generate_sas_token()
        url = f"https://{self.account_name}.blob.core.windows.net/{self.container_name}/{folder_name}?{sas_token}"

        logging.info(f"Generated url for {self.container_name}/{folder_name}.")

        return url

    def _generate_sas_token(self):
        '''Generates a shared access signature token to be appended to the blob service URL.'''
        
        permission: ContainerSasPermissions = ContainerSasPermissions(
            read=True, write=True, delete=True, list=True, add=True, create=True
        )

        expiry: datetime = datetime.now() + timedelta(days=365)

        sas_token = generate_container_sas(
            account_name=self.account_name,
            account_key=self.account_key,
            container_name=self.container_name,
            permission=permission,
            expiry=expiry,
        )
        logging.info(f"A token is created for the container {self.container_name} .")
        return sas_token
