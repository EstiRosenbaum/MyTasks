import logging
import subprocess


from .azure_connection import AzureConnection
from .copy_model import CopyModel


class Copy:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def copy_blobs(self, data: CopyModel):
        try:
            source_url = self._generate_folder_url(data.from_container_name, data.from_blob_location)
            target_url = self._generate_folder_url(data.to_container_name, f"{data.to_folder}/")

            logging.info("The routes were sent to the function that handles azcopy")

            self._azcopy_action(source_url, target_url, data.as_subdir)

        except Exception as e:
            logging.error(f"Copy failed {str(e)}")
            raise ValueError(str(e))

    def duplicate_file_with_different_name( self, container_name, folder_name, file_name, new_file_name):
        try:
            source_url = self._generate_folder_url(container_name, f"{folder_name}/{file_name}")
            target_url = self._generate_folder_url(container_name, f"{folder_name}/{new_file_name}")

            logging.info("The routes were sent to the function that handles azcopy")

            self._azcopy_action(source_url, target_url)

        except Exception as e:
            logging.error(f"Copy failed {str(e)}")
            raise ValueError(str(e))

    def _generate_folder_url(self, container_name, folder_name):
        url = AzureConnection(self.connection_string).get_url_container(container_name)
        logging.info("A URL was created to send to azcopy")

        return url.generate_url(folder_name)

    def _azcopy_action(self, source_url, target_url, as_subdir=False):
        try:
            azcopy_command = f'azcopy copy "{source_url}" "{target_url}" --recursive=true --as-subdir="{as_subdir}"'
            subprocess.run(azcopy_command, shell=True)

            logging.info("Data copied successfully")

        except Exception as e:
            logging.error(f"Copy failed {str(e)}")
            raise ValueError(str(e))
        