## The value of the variable that we won't change in the future
from pathlib import Path

CONFIG_YAML_FILE_PATH = Path("config/config.yaml")
PARAMS_YAML_FILE_PATH = Path("params.yaml")
SCHEMA_YAML_FILE_PATH = Path("schema.yaml")
MONGO_DB_URL = f"mongodb+srv://tapankheni:tapankheni@cluster0.blfohxj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
MONGO_DB_DATABASE_NAME = "wafers_fault_project"
MONGO_DB_COLLECTION_NAME = "wafers_fault_data"