import logging


class AzureContainer():
    def __init__(self, container_client):
        self.container_client = container_client 
     
        logging.info("Creating an instance from the AzureContainer class .")

# ----------------file-----------------------------

    def get_file(self, file_path): 
        ''' A function that receives a path to a file and returns the requested file. '''
        
        try:
            file = self.container_client.get_blob_client(file_path).download_blob()
            logging.info(f"Get file {file_path} .")
            
            return file.readall()
        
        except Exception as e:
            logging.error(f"Failed to download file {file_path} - {str(e)} .")
            raise ValueError(f"Failed to download file {file_path} - {str(e)} .") 

    def create_file(self, file_path):
        ''' The function accepts the routing of a file and creates the file in the requested routing. '''
        
        try:  
            self.container_client.get_blob_client(file_path).upload_blob(b"", overwrite=True)
            logging.info(f"An empty file named {file_path} was created .")
            
        except Exception as e:
            logging.error(f"Failed to create empty file - {str(e)} .")
            raise ValueError(f"Failed to create empty file - {str(e)} .")
            
    def delete_file(self, file_path):
        ''' The function receives a path to a specific file and deletes it. '''
        
        try:
            self.container_client.get_blob_client(file_path).delete_blob()
            logging.info("The file was successfully deleted .")
            
        except Exception as e:
            logging.error(f"Failed to delete file {file_path} - {str(e)} .")
            raise ValueError(f"Failed to delete file {file_path} - {str(e)} .")     

    def is_file_exist(self, file_path):
        ''' The function receives a path to the file and checks if the file exists there. '''
        
        try:
            logging.info(f"Checking if file exists from folder {file_path}") 
            return len(list(self.container_client.list_blobs(file_path))) >= 1
        
        except Exception as e:
            logging.error(f"Failed to check if file exist - {str(e)}")
            raise ValueError(f"Checking if file exists from folder {file_path}")    
     
    def get_all_files(self):
        '''The function returns all the files in the container. '''
        
        try:
            files = self.container_client.list_blobs()
            logging.info("Returning all the files in the container .")    
            
            return list(set(file.name.rstrip("/") for file in files))
                                                        
        except Exception as e:
            logging.error(f"Failed to get all files in container - {str(e)} .")
            raise ValueError(f"Failed to get all files in container - {str(e)} .")
   
    def restore_file(self, file_path):
        '''The function receives a path to the file and restores it. '''
        
        try:
            self.container_client.get_blob_client(file_path).undelete_blob()
            logging.info(f"The restore file {file_path} .")
            
        except Exception as e:
            logging.error(f"Failed to restore file {file_path} - {str(e)} .")
            raise ValueError(f"Failed to restore file {file_path} - {str(e)} .")
        
    def move_file(self, source_file, target_file):
        '''The function receives the original routing to the file and where to move it. '''
        
        try:
            source_file_client = self.container_client.get_blob_client(source_file)
            self.container_client.get_blob_client(target_file).start_copy_from_url(source_file_client.url)
            logging.info("The file was successfully move .")
            
        except Exception as e:
            logging.error(f"Failed move file - {str(e)} .")
            raise ValueError(f"Failed move file - {str(e)} .") 

    def get_size_of_file(self,file_path):
        '''The function receives a path to the file and returns its size. '''
        
        try:            
            properties_blob = self.container_client.get_blob_client(file_path).get_blob_properties()
            logging.info(f"Get size of file {file_path} .")
            return properties_blob.size
            
        except Exception as e:
            logging.error(f"Failed to get size of file {file_path} - {str(e)} .")
            raise ValueError(f"Failed get size of file {file_path} - {str(e)} .")

    def save_file_locally(self, file_path, local_folder_path):
        '''The function receives a path to a file in azure and a path to a 
        local folder and downloads the requested file to this folder'''
        
        try:
            file = self.container_client.get_blob_client(file_path).download_blob()
            data_file = file.readall()
            path = f"{local_folder_path}/{file_path.rsplit('/', 1)[-1]}"
            
            with open(path, 'w') as file:
                file.write(data_file.decode('utf-8'))
            
            logging.info(f'The file {file_path} was downloaded successfully')
                
        except Exception as e:
            logging.error(f"Failed downloaded file {file_path} - {str(e)} .")
            raise ValueError(f"Failed downloaded file {file_path} - {str(e)} .")
           
# ------------folder---------------------------
   
    def get_folder(self, folder_name):
        '''The function receives the name of the folder and returns everything that is in it. '''
        
        try:
            logging.info(f"Get folder {folder_name} .")
            files = self.get_files_from_folder(folder_name)
            
            return list(map(lambda file: {file:self.get_file(file)}, files))
                  
        except Exception as e:
            logging.error(f"Failed to get folder {folder_name} - {str(e)} .")
            raise ValueError(f"Failed to get folder {folder_name} - {str(e)} .")  
         
    def create_folder(self, folder_name):
        '''The function receives a folder name and creates a folder with that name in the container. '''
        
        try:  
            self.create_file(f"{folder_name}/")
            logging.info(f"An empty folder named {folder_name} was created .")
            
        except Exception as e:
            logging.error(f"Failed to create empty folder - {str(e)} .")
            raise ValueError(f"Failed to create empty folder - {str(e)} .")
      
    def delete_folder(self, folder_name):
        '''The function receives a folder name and deletes this folder from the container. '''
        
        try:
            files = self.container_client.list_blobs(folder_name)
            list(map(lambda file: self.delete_file(file), files))
            logging.info(f"The folder {folder_name} has been successfully deleted .")
            
        except Exception as e:
            logging.error(f"Failed to delete folder {folder_name} - {str(e)} .")
            raise ValueError(f"Failed to delete folder - {str(e)} .")

    def is_folder_exist(self, folder_name):
        '''The function receives a folder name and checks whether a folder with this name exists in the container. '''
        
        try:
            logging.info(f"Checks if a folder {folder_name} exists .") 
            return self.is_file_exist(f"{folder_name}/")
            
        except Exception as e:
            logging.error(f"Failed to check if folder exist - {str(e)} .")
            raise ValueError(f"Failed to check if folder exist - {str(e)} .")
  
    def get_all_folders(self):
        '''The function returns all the folders that are in the container. '''
        
        try:
            folders = self.container_client.walk_blobs(delimiter="/")
            logging.info("Returning all the folders in the container .")
           
            return list(set(folder.name.rstrip("/") for folder in folders if folder.name.endswith("/")))                                                                                
                                        
        except Exception as e:
            logging.error(f"Failed to get all folders in container - {str(e)} .")
            raise ValueError(f"Failed to get all folders in container - {str(e)} .")

    def get_folders_starting_with(self, prefix):
            '''The function accepts a prefix and returns the folders that start with the received string'''
            
            try:    
                blob_list = self.container_client.list_blobs(name_starts_with = prefix)
                
                return list(map(lambda blob: blob.name.split('/')[1],
                                filter(lambda blob: len(blob.name.split('/')) > 2, blob_list)))
                                            
            except Exception as e:
                logging.error(f"Failed to get folders starting with {prefix} - {str(e)} .")
                raise ValueError(f"Failed to get folders starting with {prefix}  - {str(e)} .")
              
    def get_folders_ending_with(self,folder_name, suffix): 
        '''The function accepts a suffix and returns the folders that end with the received suffix. '''
        
        try:
            blob_list = self.container_client.list_blobs(name_starts_with = folder_name)
            logging.info(f"Returning all the folders in the container that end with {suffix} .")
             
            return list(set(map(lambda blob: blob.name.split('/')[1],
                                   filter(lambda blob: blob.name.split('/')[1].endswith(suffix), blob_list))))

        except Exception as e:
            logging.error(f"Failed to get folders ending with {suffix} - {str(e)} .")
            raise ValueError(f"Failed to get folders ending with {suffix} - {str(e)} .")

    def get_folders_starting_with_and_ending_with(self, prefix, suffix): 
        '''The function accepts a prefix and a suffix and returns 
        the folders that start and end with the requested values'''
        
        try:  
            folders_starting_with = self.get_folders_starting_with(prefix)
            logging.info(f"Returning all the folders in the container that start with {prefix} and end with {suffix}.")

            return list(filter(lambda blob: blob.endswith(suffix),folders_starting_with))

        except Exception as e:
            logging.error(f"Failed to get folders starting with {prefix} and ending with {suffix} - {str(e)} .")
            raise ValueError(f"Failed to get choosed folders in container - {str(e)} .")

    def get_contents_of_folder_without_depth_layers(self, folder_name):
        '''The function receives a name of a folder and returns what it contains only in the outer layer. '''
        
        try: 
            blobs = self.container_client.walk_blobs(f'{folder_name}/', delimiter='/')
            logging.info(f"Content successfully received from folder - {folder_name}")
            
            return list(map(lambda file: file.name, blobs)) 
                         
        except Exception as e:
            logging.error(f"Failed to get content in outer layer from folder {folder_name} - {str(e)}.")
            raise ValueError(f"Failed to get content in outer layer from folder {folder_name} - {str(e)} .") 
 
    def get_folders_from_external_folder(self, folder_name):
        '''The function accepts a folder name and returns the folders inside it.'''
        
        try: 
            blobs = self.container_client.walk_blobs(f'{folder_name}/', delimiter='/')
            logging.info(f"Receiving the folders from the folder - {folder_name} completed successfully")
            
            return list(map(lambda file: file.name.split('/')[1],filter(lambda file: file.name.endswith('/'),blobs))) 
                         
        except Exception as e:
            logging.error(f"Failed to get folders from external folder {folder_name} - {str(e)}.")
            raise ValueError(f"Failed to get folders from external folder {folder_name} - {str(e)} .")    

# ---------------------------------------------
 
    def upload_to_container(self, source_path, target_path):
        '''The function receives an original routing for the material 
        and a routing for where to upload the material and uploads it to the container .'''
        
        try:
            with open(source_path, mode="rb") as data:
                self.container_client.upload_blob(name=target_path, data=data, overwrite=True)
            logging.info("The file was successfully upload .")
                     
        except Exception as e:
            logging.error(f"Failed upload file - {str(e)} .")
            raise ValueError(f"Failed upload file - {str(e)} .")
      
    def get_files_from_folder(self, folder_name):
        '''The function accepts a folder name and returns all the files in that folder. '''
        
        try:
            logging.info(f"Get files from folder {folder_name} .")
            return list(self.container_client.list_blob_names(name_starts_with=f"{folder_name}/"))
                   
        except Exception as e:
            logging.error(f"Failed get files from folder {folder_name} - {str(e)}.")
            raise ValueError(f"Failed get files from folder {folder_name} - {str(e)} .") 
      
    def count_files_from_folder(self, folder_name):
        '''The function accepts a folder name and returns the amount of files present in this folder. '''
        
        try: 
            logging.info(f"files count in folder {folder_name} .")    
            return len(self.get_files_from_folder(folder_name))
        
        except Exception as e:
            logging.error(f"Failed to count files in folder {folder_name} - {str(e)} .")
            raise ValueError(f"Failed to count files in folder {folder_name} - {str(e)} .")    
 
    def get_files_by_suffix_from_folder(self, folder_name, suffix):
        '''The function receives a folder name and an extension 
        and returns all the files in the folder that end with the requested extension. '''
        
        try:
            files = self.container_client.list_blobs(folder_name)
            logging.info(f"Receiving files by suffix from {folder_name} .")
            
            return list(map(lambda folder: folder.name, filter(lambda file: file.name.endswith(suffix),files)))
                                                                                                   
        except Exception as e:
            logging.info(f"Failed to receive the files by suffix from {folder_name} - {str(e)} .")
            raise ValueError(f"Failed to receive the files by suffix from {folder_name} - {str(e)} .")
