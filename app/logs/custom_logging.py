import sys
import json
import logging
from pathlib import Path
from loguru import logger


def configure_framework_logging():
    gunicorn_error_logger = logging.getLogger("gunicorn.error")
    gunicorn_logger = logging.getLogger("gunicorn")
    uvicorn_access_logger = logging.getLogger("uvicorn.access")
    uvicorn_access_logger.handlers = gunicorn_error_logger.handlers
    return gunicorn_error_logger, gunicorn_logger
    

class CustomizeLogger:
    @classmethod
    def make_logger(cls, config_path: Path):
        config = cls.load_logging_config(config_path)
        logging_config = config.get("logger")
        logger = cls.customize_logging(
            logging_config.get("path") + "/" + logging_config.get("filename"),
            level=logging_config.get("level"),
            retention=logging_config.get("retention"),
            rotation=logging_config.get("rotation"),
            format=logging_config.get("format")
        )
        return logger
    
    @classmethod
    def customize_logging(
        cls,
        filepath: Path,
        level: str,
        rotation: str,
        retention: str,
        format: str,
    ):
        logger.remove()
        logger.add(
            str(filepath),
            rotation=rotation,
            retention=retention,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format
        )
        logger.add(
            sys.stdout,
            enqueue=True,
            backtrace=True,
            level=level.upper(),
            format=format
        )

    
    @classmethod
    def load_logging_config(cls, config_path):
        config = None
        with open(config_path) as config_file:
            config = json.load(config_file)
        return config
    
