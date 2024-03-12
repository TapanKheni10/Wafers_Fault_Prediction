from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    local_data_file: Path

@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    file_dir: Path
    STATUS_FILE: str
    all_schema: dict

@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    cols_to_drop: list
    preprocessor_name: str

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    x_train_data_path: Path
    y_train_data_path: Path
    model_name: str
    params: dict

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    x_test_data_path: Path
    y_test_data_path: Path
    model_path: Path
    metrics_name: str