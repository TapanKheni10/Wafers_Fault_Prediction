import joblib
import numpy as np
import pandas as pd
import os, sys
from pathlib import Path
from WafersFault import logger

class PredictionPipeline:
    def __init__(self, pred_file_path) -> None:
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        self.preprocessor = joblib.load(Path("artifacts/data_transformation/preprocessor.joblib"))
        self.prediction_file_path = Path(pred_file_path)

    def predict(self):
        target_column = "Good/Bad"
        input_df = pd.read_csv(self.prediction_file_path)

        input_df = input_df.drop(columns=["Unnamed: 0"]) if "Unnamed: 0" in input_df.columns else input_df

        transformed_input_df = self.preprocessor.transform(input_df)

        predictions = self.model.predict(transformed_input_df)

        input_df[target_column] = [pred for pred in predictions]

        target_column_mapping = {0:'Bad', 1:'Good'}

        input_df[target_column] = input_df[target_column].map(target_column_mapping)

        os.makedirs("artifacts/prediction", exist_ok=True)
        input_df.to_csv("artifacts/prediction/prediction_file.csv", index=False)

        logger.info("prediction completed.")

        prediction_result = pd.read_csv(Path("artifacts/prediction/prediction_file.csv"))
        return prediction_result
