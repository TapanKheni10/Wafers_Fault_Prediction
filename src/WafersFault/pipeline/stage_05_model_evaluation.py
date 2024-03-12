from WafersFault.components.model_evaluation import ModelEvaluation
from WafersFault.config import configuration

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        try:
            config = configuration.ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            obj = ModelEvaluation(config=model_evaluation_config)
            obj.save_matrix()

        except Exception as e:
            raise e
        
if __name__ == '__main__':
    pass