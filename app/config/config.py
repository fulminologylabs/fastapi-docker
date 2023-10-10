import os
from app.utils.environment import load_environment

load_environment()

class Config:
    """
        Application configuration module. requires access to environment variables.
    """
    # general
    ENVIRONMENT              : str = os.getenv("ENVIRONMENT", "local")
    API_PREFIX               : str = "/api"
    WORKERS                  : int  = int(os.environ.get("GUNICORN_WORKERS", "5"))
    # services
    RINGY_KEY                : str = "123password"
    # logging
    GUNICORN_ERROR_LOG_LEVEL : str = os.getenv("GUNICORN_ERROR_LOG_LEVEL", "INFO")
    ACCESS_LOG_LEVEL         : str = os.getenv("ACCESS_LOG_LEVEL", "ERROR")
    ROOT_LOG_LEVEL           : str  = os.getenv("ROOT_LOG_LEVEL", "ERROR")
    JSON_LOGS                : bool = True if os.environ.get("JSON_LOGS", "0") == "1" else False

config = Config()
