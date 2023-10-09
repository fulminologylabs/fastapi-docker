import os
import logging
import uvicorn
from fastapi import FastAPI
from app.utils.environment import load_environment
from fastapi.middleware.cors import CORSMiddleware
from fastapi.logger import logger as fastapi_logger

active_env = os.environ["ENVIRONMENT"]
load_environment(active_env)

app = FastAPI(
    title="fastapi-docker",
    version="1.0",
    description="quickstart template."
)

gunicorn_error_logger = logging.getLogger("gunicorn.error")
gunicorn_logger = logging.getLogger("gunicorn")
uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.handlers = gunicorn_error_logger.handlers

fastapi_logger.handlers = gunicorn_error_logger.handlers

if __name__ != "__main__":
    fastapi_logger.setLevel()
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
        logging.info(f"Running {active_env}")
        return { "status": "healthy" }
    except Exception as e:
        return { 
            "status": "cannot connect to API. Contact nick@fulminologylabs.co and cemhealthadvisor@gmail.com",
            "error": f"{str(e)}"
            }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
