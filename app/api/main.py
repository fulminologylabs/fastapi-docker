import os
import logging
import uvicorn
from fastapi import FastAPI
from app.utils.environment import load_environment
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger as fastapi_logger
from app.logs.custom_logging import configure_framework_logging

active_env = os.environ["ENVIRONMENT"]
load_environment(active_env)

app = FastAPI(
    title="fastapi-docker",
    version="1.0",
    description="quickstart template."
)

loggers: tuple = configure_framework_logging()
fastapi_logger.handlers = loggers[0]

if __name__ != "__main__":
    fastapi_logger.setLevel(loggers[1].level)
else:
    fastapi_logger.setLevel(logging.DEBUG)

origins = ["*"] # NOTE ideally we can add our cron service
                #      and NextGen Leads to this list.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health-check")
async def root():
    try:
        logger.info(f"Running in: {active_env}")
        return { "status": "healthy" }
    except Exception as e:
        return { 
            "status": "cannot connect to API. Contact nick@fulminologylabs.co and cemhealthadvisor@gmail.com",
            "error": f"{str(e)}"
            }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="DEBUG")
