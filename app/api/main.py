import sys
import logging
from loguru import logger
from fastapi import FastAPI
from app.api.app import Server
from app.config.config import config
from app.api.endpoints import health_check
from app.utils.environment import load_environment
from fastapi.middleware.cors import CORSMiddleware
from app.logs.logging import InterceptHandler, \
    add_log_handlers, OPTIONS

load_environment()

app = FastAPI(
    title="NextGen Leads x Ringy Integration API",
    version="1.0",
    description="A custom Ringy interface, for NextGen Leads data."
)
# add endpoints
app.include_router(health_check.router)
origins = ["*"] # NOTE ideally we can add our cron service
                #      and NextGen Leads to this list.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    intercept_handler = InterceptHandler()
    logging.root.setLevel(config.ROOT_LOG_LEVEL)
    add_log_handlers(intercept_handler)
    logger.configure(handlers=[{"sink": sys.stdout, "serialize": config.JSON_LOGS}])
    Server(app, OPTIONS).run()
