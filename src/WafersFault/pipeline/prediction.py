import joblib
import numpy as np
import pandas as pd
import os, sys
from pathlib import Path

class PredictionPipeline:
    def __init__(self) -> None:
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        self.preprocessor = joblib.load(Path("artifacts/model_transformation/preprocessor.joblib"))

    def save_input_files(self) -> str:
        pred_file_dir = "artifacts/prediction"

        os.makedirs(pred_file_dir, exist_ok=True)


    def predict(self, data):
        transformed_data = self.preprocessor.transform(data)
        prediction = self.model.predict(transformed_data)

        return prediction