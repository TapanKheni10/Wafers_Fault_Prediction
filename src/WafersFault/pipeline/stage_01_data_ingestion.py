from WafersFault.components.data_ingestion import DataIngestion
from WafersFault.config import configuration

class DataIngestionTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = configuration.ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            obj = DataIngestion(config=data_ingestion_config)
            obj.initiate_data_ingestion()
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    pass