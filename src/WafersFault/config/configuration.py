from WafersFault.constants import CONFIG_YAML_FILE_PATH, PARAMS_YAML_FILE_PATH, SCHEMA_YAML_FILE_PATH, MONGO_DB_URL, MONGO_DB_COLLECTION_NAME, MONGO_DB_DATABASE_NAME
from WafersFault.utils.common import read_yaml, create_directories
from WafersFault.entity import config_entity

class ConfigurationManager:
    def __init__(self, 
                 config_filepath=CONFIG_YAML_FILE_PATH,
                 params_filepath=PARAMS_YAML_FILE_PATH, 
                 schema_filepath=SCHEMA_YAML_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> config_entity.DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = config_entity.DataIngestionConfig(
            root_dir=config.root_dir,
            local_data_file=config.local_data_file,
        )

        return data_ingestion_config