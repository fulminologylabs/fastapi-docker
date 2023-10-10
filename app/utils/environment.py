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