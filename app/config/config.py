import os
from app.utils.environment import load_environment
from app.utils.constants import RuntimeEnvironments, LogLevels, \
    API_PREFIX, GUNICORN_WORKERS, JSON_LOGS

load_environment()

class Config:
    """
        Application configuration module. requires access to environment variables.
    """
    # general
    ENVIRONMENT              : str = os.getenv("ENVIRONMENT", RuntimeEnvironments.PROD.value)
    API_PREFIX               : str = API_PREFIX
    WORKERS                  : int  = int(os.environ.get("GUNICORN_WORKERS", GUNICORN_WORKERS))
    # services
    RINGY_KEY                : str = "123password"
    # logging
    GUNICORN_ERROR_LOG_LEVEL : str = os.getenv("GUNICORN_ERROR_LOG_LEVEL", LogLevels.INFO.value)
    ACCESS_LOG_LEVEL         : str = os.getenv("ACCESS_LOG_LEVEL", LogLevels.INFO.value)
    ROOT_LOG_LEVEL           : str  = os.getenv("ROOT_LOG_LEVEL", LogLevels.INFO.value)
    JSON_LOGS                : bool = True if os.environ.get("JSON_LOGS", JSON_LOGS) == "1" else False

config = Config()
