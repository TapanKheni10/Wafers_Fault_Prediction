import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC
from WafersFault import logger
from WafersFault.entity import config_entity
import os
from sklearn.metrics import f1_score, precision_score, recall_score, roc_auc_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV

class ModelTrainer:
    def __init__(self, config: config_entity.ModelTrainerConfig) -> None:
        self.config = config
        self.models = {
            "RandomForestClassifier" : RandomForestClassifier(),
            "GradientBoostingClassifier" : GradientBoostingClassifier(),
            "XGBClassifier" : XGBClassifier(),
            "SVC" : SVC()
        }

    def evaluate_models(self, X, y, models) -> dict:

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=32)

        model_performances = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train, y_train)
            
            y_pred = model.predict(X_test)

            test_score = accuracy_score(y_test, y_pred)
            model_performances[list(models.keys())[i]] = test_score

        return model_performances
    
    def finetune_model(self, best_model, best_model_name, X_train, y_train) -> object:

        model = best_model

        params_grid = self.config.params["model_selection"]["model"][best_model_name]["search_param_grid"]

        grid_search = GridSearchCV(
            best_model, param_grid=params_grid, cv=5, n_jobs=-1, verbose=1 
        )

        grid_search.fit(X_train, y_train)

        best_params = grid_search.best_params_

        print(f"best params are: {best_params}")

        fintuned_model = best_model.set_params(**best_params)

        return fintuned_model

    def train(self):

        logger.info("fetching train data from the given path.")
        X_train = np.load(self.config.x_train_data_path)
        y_train = np.load(self.config.y_train_data_path)
        logger.info("fetching of train data done.")

        logger.info(f"Shape of X_train: {X_train.shape}")
        logger.info(f"Shape of y_train: {y_train.shape}")

        model_report = self.evaluate_models(X_train, y_train, self.models)

        ## getting the best model score
        best_model_score = max(sorted(model_report.values()))
        logger.info(f"best model score: {best_model_score}")

        ## gettin the best model name from the dictionary
        best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
        logger.info(f"best model name: {best_model_name}")

        ## getting the model object to finetune it
        best_model = self.models[best_model_name]
        
        model = self.finetune_model(
            best_model=best_model,
            best_model_name=best_model_name,
            X_train=X_train,
            y_train=y_train
        )

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))