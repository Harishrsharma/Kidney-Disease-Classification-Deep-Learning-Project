import os
from pathlib import Path
import logging

#logging string
logging.basicConfig(level=logging.INFO , format = '%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

project_name = "cnnClassifier"


list_of_files = [
    ".github/workflows/.gitkeep", # if this folder is empty then it will not be tracked by git so we add a .gitkeep file
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"


]


for filepath in list_of_files:
    filepath = Path(filepath)  # convert to Path object for better path manipulations because it is OS independent
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True) # exist_ok=True means if the folder already exists then do not throw an error
        logger.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logger.info(f"Creating empty file: {filepath}")
    else:
        logger.info(f"File already exists: {filepath}, skipping creation.")