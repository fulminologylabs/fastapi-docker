import os
from app.utils.environment import load_environment

ENVIRONMENT = os.getenv("ENVIRONMENT", "local")
load_environment(ENVIRONMENT)

class Config:
    """
        Application configuration module. requires access to environment variables.
    """
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "local")
    API_PREFIX : str = "/api"
    LOG_DIR    : str = "/var/log/hub"
    RINGY_KEY  : str = "123password"


config = Config()
