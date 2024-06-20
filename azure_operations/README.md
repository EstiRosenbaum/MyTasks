# Azure operations

This project is a library of operations in Azure, it provides a simple and convenient way to connect to Azure and perform various operations on it related to Azure storage blob.

## Installation

The file is stored in the last tag of the repository,
To install the requested package, download it from there by the following command:

```bash
pip install git+https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/Green2Moon/SkylineAutomation.git#subdirectory=${PACKAGE_FILE_NAME}
```

### The details needed to be filled

`GITHUB_USER` - Enter your Git username.\
`GITHUB_TOKEN` - insert the token associated with the requested project.\
`PACKAGE_FILE_NAME` - enter the name of the folder from which the requested whl file was created.

## Usage

To use the azure_operations library, follow these steps:

1. Import the AzureConnection class from the library:

    ```python
    from azure_operations.azure_connection import AzureConnection
    ```

2. Create an instance of the AzureConnection class and give it connection_string

    ```python
    azure_connection = AzureConnection('connection_string')
    ```

3. Now create an instance of azure_container from AzureConnection on which you can run the container related functions

    ```python
    container = azure_connection.get_azure_container('container-name')
    ```

4. An example of using functions:

    ```python
    container.create_file('file-name')
    container.is_folder_exist('folder-name')
    print(container.count_files_from_folder('folder-name'))
    ```

5. Create an instance of get_url_container from AzureConnection from which you can get the url to the desired container:

    ```python
    url = azure_connection.get_url_container('container-name')
    ```

6. An example of using functions:

    ```python
    print(url.generate_url('folder-name'))
    ```

Successfully!
