import logging

from .schema import schema
from fastapi import FastAPI

from fastapi_utils.inferring_router import InferringRouter


app = FastAPI()
router = InferringRouter()
logger = logging.getLogger("my_logger")


@app.get("/", response_model=schema.Response)
def read_root():
    return {"Hello": "World"}
