import os
import logging 
from pathlib import Path
from dotenv import load_dotenv

def load_environment() -> None:
    """
        Loads the environment file .env
    """
    logging.info("Loading environment")
    filename = Path(".").absolute().as_posix() + "/.env"
    load_dotenv(dotenv_path=filename, verbose=True)

def get_db_uri(with_driver: bool = False) -> str:
    """
        Returns postgres db uri.
    """
    load_environment()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("DB_PORT")
    db = os.getenv("DB_NAME")

    if with_driver:
        return f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return f"postgres://{user}:{password}@{host}:{port}/{db}"

def get_test_db_uri(with_driver: bool = False) -> str:
    """
        For Tests only.
    """
    load_environment()

    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST")
    port = os.getenv("TEST_DB_PORT")
    db = os.getenv("TEST_DB_NAME")
    if with_driver:
        return f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return f"postgres://{user}:{password}@{host}:{port}/{db}"  
