import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "rag_01"

list_of_files = [
    ".github/workflows/.gitkeep",
    
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "data/embeddings/.gitkeep",
    
    "models/.gitkeep",
    "notebooks/trials.ipynb",
    "templates/index.html",
    
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/data/__init__.py",
    f"src/{project_name}/retrieval/__init__.py",
    f"src/{project_name}/generation/__init__.py",
    f"src/{project_name}/evaluation/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
]


for filepath in list_of_files:
    filepath = Path(filepath) #to solve the windows path issue
    filedir, filename = os.path.split(filepath) # to handle the project_name folder


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")