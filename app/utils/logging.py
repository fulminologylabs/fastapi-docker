import os
import logging
from pathlib import Path
from app.config.config import config
from app.logs.custom_logging import CustomizeLogger

def init_logger() -> logging.Logger:
    logger = logging.getLogger(__name__)
    log_dir = config.LOG_DIR

    if not os.path.exists(log_dir):
        print("Log directory not found, creating directory...")
        os.makedirs(log_dir, exist_ok=True)
    
    config_path = Path(__file__).with_name("logging_config.json")
    logger = CustomizeLogger.make_logger(config_path)
    return logger
