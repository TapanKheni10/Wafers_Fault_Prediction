import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier
from WafersFault import logger
from WafersFault.entity import config_entity
import os
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, cross_val_predict

class ModelTrainer:
    def __init__(self, config: config_entity.ModelTrainerConfig) -> None:
        self.config = config

    def train(self):
        X_train = np.load(self.config.x_train_data_path)
        y_train = np.load(self.config.y_train_data_path)

        logger.info(f"Shape of X_train: {X_train.shape}")
        logger.info(f"Shape of y_train: {y_train.shape}")
        
        random_classifier = RandomForestClassifier(random_state=42)
        # random_scores = cross_val_score(random_classifier, X_train, y_train, cv=10, scoring="roc_auc", verbose=2)
        random_classifier.fit(X_train, y_train)

        joblib.dump(random_classifier, os.path.join(self.config.root_dir, self.config.model_name))