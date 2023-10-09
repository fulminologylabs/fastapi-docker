import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="fastapi-dcoker",
    version="1.0",
    description="quickstart template."
)

