import sys
import yaml
import logging
from pathlib import Path
from loguru import logger

def init_logger():
    """
    For easy use with Digital Ocean
    Application Platform Deployment
    default log store.
    """
    config_file = Path(__file__).with_name("config.yml")
    with open(config_file) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        logging.config.dictConfig(config)
    
class CustomizeLogger:
    """
    To be used with a logging_config.json
    file, living at the root of app directory.
    """
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
    
