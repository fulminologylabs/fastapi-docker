from enum import Enum

API_PREFIX       = "/api"
GUNICORN_WORKERS = "5"
JSON_LOGS        = "0"

class RuntimeEnvironments(Enum):
    LOCAL = "local"
    PROD  = "prod"


class LogLevels(Enum):
    DEBUG = "DEBUG"
    INFO  = "INFO"
    ERROR = "ERROR"

