from WafersFault import logger
from WafersFault.entity import config_entity
import pandas as pd
import numpy as np
import os
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import KNNImputer, SimpleImputer
from sklearn.preprocessing import RobustScaler
from imblearn.combine import SMOTETomek
from sklearn.model_selection import train_test_split
import joblib

class DataTransformation:
    def __init__(self, config: config_entity.DataTransformationConfig) -> None:
        self.config = config

    def do_data_transformation(self):

        df = pd.read_csv(self.config.data_path)

        logger.info("dropping the unnecessary columns")
        df.drop(columns=self.config.cols_to_drop, axis=1, inplace=True)

        logger.info("spliting dependent and independent features")
        X = df.iloc[:,:-1]
        y = df["Good/Bad"]

        logger.info(f"Shape of X: {X.shape}, shape of y: {y.shape}")

        logger.info("data preprocessing started....")
        numerical_columns = list(X.columns)

        preprocessor = ColumnTransformer(
            transformers=[
                ("Numeric_1", KNNImputer(n_neighbors=5), numerical_columns),
                ("Numeric_2", Pipeline([
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", (RobustScaler()))
                ]), numerical_columns)
            ]
        )

        preprocessor_pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor)
            ]
        )

        X_transformed = preprocessor_pipeline.fit_transform(X)
        logger.info(f"Shape of the transformed X: {X.shape}")
        logger.info("data preprocessing completed....")

        logger.info("class imbalance handling phase started")

        resampler = SMOTETomek(sampling_strategy="auto")
        X_res, y_res = resampler.fit_resample(X_transformed, y)

        logger.info(f"Before resampling, Shape of the training instances: {np.c_[X_transformed, y].shape}\n")
        logger.info(f"After resampling, Shape of the training instances: {np.c_[X_res, y_res].shape}\n")
        logger.info(y.value_counts())
        logger.info(y_res.value_counts())

        logger.info("done with class imbalance")

        logger.info("train_test_split started....")
        X_train, X_test, y_train, y_test = train_test_split(X_res, y_res, test_size=0.2, random_state=42)
        y_train = np.where(y_train==-1, 0, 1)
        y_test = np.where(y_test==-1, 0, 1)

        logger.info(f"X_train shape: {X_train.shape}, y_train shape: {y_train.shape}")
        logger.info(f"X_test shape: {X_test.shape}, y_test shape: {y_test.shape}")
        logger.info("train_test_split completed.....")

        np.save(os.path.join(self.config.root_dir, "X_train.npy"), X_train)
        np.save(os.path.join(self.config.root_dir, "X_test.npy"), X_test)
        np.save(os.path.join(self.config.root_dir, "y_train.npy"), y_train)
        np.save(os.path.join(self.config.root_dir, "y_test.npy"), y_test)

        joblib.dump(preprocessor_pipeline, os.path.join(self.config.root_dir, self.config.preprocessor_name))
