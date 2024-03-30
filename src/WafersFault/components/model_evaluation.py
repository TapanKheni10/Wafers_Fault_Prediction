import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score
import joblib
from pathlib import Path
from WafersFault.utils.common import save_json
import os
from WafersFault import logger
from WafersFault.entity import config_entity

class ModelEvaluation:
    def __init__(self, config: config_entity.ModelEvaluationConfig) -> None:
        self.config = config

    def eval_matrix(self, y_true, y_pred):
        precision = precision_score(y_true=y_true, y_pred=y_pred)
        recall = recall_score(y_true=y_true, y_pred=y_pred)
        f1 = f1_score(y_true=y_true, y_pred=y_pred)
        accuracy = accuracy_score(y_true=y_true, y_pred=y_pred)
        return precision, recall, f1, accuracy
    
    def save_matrix(self):
        X_test = np.load(self.config.x_test_data_path)
        y_test = np.load(self.config.y_test_data_path)

        model = joblib.load(self.config.model_path)

        y_pred = model.predict(X_test)

        (precision, recall, f1, accuracy) = self.eval_matrix(y_pred=y_pred, y_true=y_test)

        if accuracy < 0.5:
            raise Exception("no best model found with an accuracy more than the threshold 0.6.")
        
        logger.info("best model found on both training and testing data")

        scores = {
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "accuracy_score": accuracy
        }

        save_json(path=Path(os.path.join(self.config.root_dir, self.config.metrics_name)), data=scores)