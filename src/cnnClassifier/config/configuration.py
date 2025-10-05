import os
import sys

# Get the Current Working Directory (CWD) of the notebook process
current_dir = os.getcwd() 

# Assuming your project root is the CWD, you can define 'src_dir' relative to it
# If 'src' is directly in the CWD (project_root/src)
src_dir = os.path.join(current_dir, 'src') 

# If the notebook is deep inside the project and you need to go up levels:
# current_dir = os.getcwd() 
# project_root = os.path.abspath(os.path.join(current_dir, os.pardir, os.pardir)) # Example: go up two levels
# src_dir = os.path.join(project_root, 'src') 


# Add the 'src' directory to the system path
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories,save_json
from cnnClassifier.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config