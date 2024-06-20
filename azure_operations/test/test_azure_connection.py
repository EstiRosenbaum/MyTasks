import unittest
from unittest.mock import patch
from src.azure_operations.azure_connection import AzureConnection


class Mock_blob_service_client():
    def get_container_client(self, container_name):
        return container_name is not None


@patch('src.azure_operations.azure_connection.BlobServiceClient.from_connection_string', return_value=Mock_blob_service_client())
class TestConnection(unittest.TestCase):

    def test_get_azure_container(self, from_connection_string):
        connect = AzureConnection("connection_string")
        result = connect.get_azure_container("container_name")
        from_connection_string.assert_called_once()
        
        assert result is not None

    def test_get_connect(self, from_connection_string):
        connect = AzureConnection("connection_string")
        result = connect.get_connect()
        from_connection_string.assert_called_once()
        
        assert result.get_container_client("container_name") is True
        


        