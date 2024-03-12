from WafersFault.components.data_validation import DataValidation
from WafersFault.config import configuration

class DataValidationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = configuration.ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            obj = DataValidation(config=data_validation_config)
            obj.validate_all_columns()
            
        except Exception as e:
            raise e
        
if __name__ == '__main__':
    pass