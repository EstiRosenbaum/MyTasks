import unittest
from unittest.mock import MagicMock, patch
from src.azure_operations.operations_container import *
from src.azure_operations.azure_connection import *


class Mock_blob_service_client():
    def get_container_client(self, container_name):
        return container_name is not None


@patch('src.azure_operations.azure_connection.BlobServiceClient.from_connection_string', return_value=Mock_blob_service_client())
class TestConnectAzure(unittest.TestCase):

    def setup_mocks_connection(self, _):
        return AzureConnection("connection_string").get_azure_container('test-container')

    def test_get_file(self, mock_azure_container):
        mock_azure_container.get_blob_client = MagicMock(return_value=MagicMock(url='mocked_url'))  
        file_content = mock_azure_container.get_file("file_name")
        mock_azure_container.get_file.assert_called_once()
        
        assert file_content is not None

    def test_create_file(self, mock_azure_container):
        result = mock_azure_container.create_file("file1.txt")
        mock_azure_container.create_file.assert_called()
        
        assert result is not None

    def test_delete_file(self, mock_azure_container):
        self.setup_mocks_connection("mock_container")
        result = mock_azure_container.delete_blob("folder_name")
        mock_azure_container.delete_blob.assert_called()
        
        assert result is not None

    def test_is_file_exist(self, mock_azure_container):
        self.setup_mocks_connection("mock_container")
        result = mock_azure_container.exists("folder_name")
        mock_azure_container.exists.assert_called()
        
        assert result is not None

    def test_get_all_files(self, mock_azure_container):
        result = mock_azure_container.get_all_files()
        mock_azure_container.get_all_files.assert_called()
        
        assert result is not None

    def test_restore_file(self, mock_azure_container):
        mock_azure_container.get_blob_client = MagicMock(return_value=MagicMock(url='mocked_url'))
        result = mock_azure_container.restore_file("file1.txt")
        mock_azure_container.restore_file.assert_called_with("file1.txt")
        
        assert result is not None

    def test_moved_file(self, mock_azure_container):
        mock_azure_container.get_blob_client = MagicMock(return_value=MagicMock(url='mocked_url'))
        mock_azure_container.move_file("source_file", "target_file")
        mock_azure_container.move_file.assert_called_with("source_file", "target_file")
            
    @patch("src.azure_operations.operations_container.AzureContainer.get_files_from_folder", return_value="list")
    @patch("src.azure_operations.operations_container.AzureContainer.get_file", return_value="list")
    def test_get_folder(self, mock_get_file, _, mock_azure_container):
        mock_azure_container.get_files_from_folder = MagicMock(return_value=MagicMock(list='mocked_list'))
        mock_azure_container.get_folder('try')
        mock_azure_container.get_folder.assert_called()

    @patch("src.azure_operations.operations_container.AzureContainer.create_file")
    def test_create_folder(self, folder_name, _):
        self.setup_mocks_connection("mock_container")
        folder_name.create_folder('follder')
        folder_name.create_folder.assert_called_once()

    def test_delete_folder(self, mock_azure_container):
        result = mock_azure_container.delete_folder("file1.txt")
        mock_azure_container.delete_folder.assert_called()
        
        assert result is not None

    @patch("src.azure_operations.operations_container.AzureContainer.is_folder_exist", return_value=True)
    @patch("src.azure_operations.operations_container.AzureContainer.is_file_exist", return_value=True)
    def test_is_folder_exist(self, mock_file_exist, mock_is_folder_exist, _):
        result = AzureContainer.is_folder_exist("file")
        AzureContainer.is_file_exist("file")
        mock_is_folder_exist.assert_called()
        mock_file_exist.assert_called()
        
        assert result is True

    @patch("src.azure_operations.operations_container.AzureContainer.get_all_files", return_value=["folder1", "folder2"])
    def test_get_all_folders(self, _, mock_azure_container):
        result = AzureContainer.get_all_files("folder_name")
        expected_result = ["folder1", "folder2"]
        assert result == expected_result

    @patch("azure.storage.blob.BlobClient.upload_blob", return_value="Mock file content")
    def test_upload_to_container(self, _, mock_azure_container):
        mock_client = MagicMock()
        mock_azure_container.return_value = mock_client
        source_path = 'test_file.txt'
        target_path = 'uploaded_file.txt'
        mock_azure_container.upload_to_container(source_path, target_path)
        mock_azure_container.upload_to_container.assert_called_once_with(source_path, target_path)
            
    def test_get_files_from_folder(self, mock_azure_container):
        result = mock_azure_container.get_all_files()
        mock_azure_container.get_all_files.assert_called()
        
        assert result is not None

    @patch("src.azure_operations.operations_container.AzureContainer.get_files_from_folder")
    def test_count_files_from_folder(self, mock_get_files, _):
        folder_name = "test_folder"
        mock_get_files.return_value = ["file1.txt", "file2.txt"]
        result = AzureContainer("container_name").count_files_from_folder(folder_name)
        mock_get_files.assert_called_with(folder_name)
        
        assert result == 2

    def test_get_files_by_suffix_from_folder(self, mock_azure_container):
        folder_name = "test_folder"
        result = mock_azure_container.get_files_by_suffix_from_folder(folder_name, ".txt")
        mock_azure_container.get_files_by_suffix_from_folder(folder_name, ".txt")
            
        assert result is not None
        