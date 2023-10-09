import logging 
from pathlib import Path
from dotenv import load_dotenv

def load_environment(env_name: str = "local") -> None:
    """
        Loads the environment file .env.{environment_slug}
    """
    logging.debug(f"Loading environment: {env_name}")
    filename = Path(".").absolute().as_posix() + "/.env"
    load_dotenv(dotenv_path=filename, verbose=True)