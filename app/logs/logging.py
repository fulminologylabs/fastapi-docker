import sys
import logging
from loguru import logger
from gunicorn.glogging import Logger
from app.config.config import config

LOG_FORMAT = "[%(asctime)s %(process)d:%(threadName)s] %(name)s - %(levelname)s - %(message)s | %(filename)s:%(lineno)d"

class InterceptHandler(logging.Handler):
    def emit(self, record):
        # get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # find caller from where originated the logged message
        frame, depth = sys._getframe(6), 6
        while frame and frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())


class GunicornLogger(Logger):
    def setup(self, _cfg):
        handler = logging.NullHandler()
        self.error_logger = logging.getLogger("gunicorn.error")
        self.error_logger.addHandler(handler)

        self.access_logger = logging.getLogger("gunicorn.access")
        self.access_logger.addHandler(handler)

        self.error_logger.setLevel(config. GUNICORN_ERROR_LOG_LEVEL)
        self.access_logger.setLevel(config.ACCESS_LOG_LEVEL)



def add_log_handlers(handler: InterceptHandler) -> None:
    seen = set()
    for name in [
        *logging.root.manager.loggerDict.keys(),
        "gunicorn",
        "gunicorn.access",
        "gunicorn.error",
        "uvicorn",
        "uvicorn.access",
        "uvicorn.error",
    ]:
        if name not in seen:
            seen.add(name.split(".")[0])
            logging.getLogger(name).handlers = [handler]
    # Removes duplication of our own logging
    framework_logger = logging.getLogger("fastapi")
    framework_logger.propagate = False
    
OPTIONS = {
    "bind": "0.0.0.0",
    "port": "8000",
    "workers": config.WORKERS,
    "accesslog": "-",
    "errorlog": "-",
    "worker_class": "uvicorn.workers.UvicornWorker",
    "logger_class": GunicornLogger,
}
