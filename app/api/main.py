import uvicorn
from fastapi import FastAPI
from app.config.config import Config
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="fastapi-docker",
    version="1.0",
    description="quickstart template."
)

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
        return { "status": "healthy" }
    except Exception as e:
        return { 
            "status": "cannot connect to API. Contact nick@fulminologylabs.co and cemhealthadvisor@gmail.com",
            "error": f"{str(e)}"
            }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
