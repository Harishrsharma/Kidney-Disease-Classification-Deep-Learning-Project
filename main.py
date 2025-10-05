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
from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline 
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare base model"
try: 
   logger.info(f"*******************")
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   prepare_base_model = PrepareBaseModelTrainingPipeline()
   prepare_base_model.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e



