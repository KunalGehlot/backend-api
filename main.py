import sys
import logging  # Cannot have an API without a logger
import uvicorn  # Sweet little Async SGI

from time import sleep
from routes import my_route
from fastapi import FastAPI  # We need a Fast, Scalable API
from handlers.async_ops import worker
from data.mongo_setup import global_init

# Initialize the logger
logger = logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s : %(message)s",
    handlers=[logging.FileHandler("fam(ily).log"), logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger("my_logger")
# Initialize FastAPI
app = FastAPI()
# Include all the routes
app.include_router(my_route.router)


@app.on_event("startup")
async def startup():
    logger.info("Initializing MongoDB")
    global_init()  # Initialize the database

    logger.info("Starting Backgroung Async Tasks")
    # await main()  # Run the main function in the background


async def main() -> None:
    """Entry point for the application"""

    logger.debug("Async main() called")
    while True:
        logger.debug("Async main() loop")
        await worker()  # Start the worker
        sleep(10)  # Sleep for 10 seconds
        # break  # For development purposes (Could be a part of input args)


if __name__ == "__main__":
    """If this is the main file, run the server"""
    logger.info("Starting up fam(ily)")
    uvicorn.run(
        "main:app", host="0.0.0.0", port=8888, reload=True
    )  # Run the app on port 8888
