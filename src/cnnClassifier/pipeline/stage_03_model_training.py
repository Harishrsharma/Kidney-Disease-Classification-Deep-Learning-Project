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

from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logger


STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()
        
if __name__ == '__main__':
    try:
        logger.info(f"*******************")
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
        
