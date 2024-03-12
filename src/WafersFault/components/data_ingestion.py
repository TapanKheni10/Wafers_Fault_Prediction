import pandas as pd
import numpy as np
import os
import sys
from pathlib import Path
from pymongo import MongoClient
from WafersFault import logger
from WafersFault.utils.common import get_size
from WafersFault.constants import MONGO_DB_URL, MONGO_DB_COLLECTION_NAME, MONGO_DB_DATABASE_NAME
from WafersFault.entity import config_entity

class DataIngestion:
    def __init__(self, config: config_entity.DataIngestionConfig):
        self.config = config

    def export_collection_as_dataframe(self) -> pd.DataFrame:
        logger.info("retrieving data from mongoDB as dataframe")

        mongo_client = MongoClient(MONGO_DB_URL)

        collection = mongo_client[MONGO_DB_DATABASE_NAME][MONGO_DB_COLLECTION_NAME]

        df = pd.DataFrame(list(collection.find()))

        logger.info(df.columns)

        if "_id" in df.columns.to_list():
            df.drop(columns=["_id"], axis=1, inplace=True)

        logger.info(df.columns)

        df.replace({"na": np.nan}, inplace=True)

        logger.info("data retrieval completed")

        return df
    
    def export_data_into_feature_store_file_path(self) -> None:
        logger.info("Exporting data from mongoDB to store it into the desired artifacts")

        sensor_data = self.export_collection_as_dataframe()
        logger.info(f"saving exported data into feature store file path: {self.config.root_dir}")

        if not os.path.exists(self.config.local_data_file):
            sensor_data.to_csv(self.config.local_data_file, index=False)

            logger.info(f"exported data from mongoDB stored at {self.config.local_data_file}")
        else:
            logger.info(f"file already exists of size: {get_size(Path(self.config.local_data_file))}")


    def initiate_data_ingestion(self) -> None:
        logger.info("data ingestion component initiated")

        self.export_data_into_feature_store_file_path()

        logger.info(f"data ingestion component completed")

