import sys
import logging  # Cannot have an API without a logger
import asyncio  # Asyncio is a library that allows you to write async programs
import uvicorn  # Sweet little Async SGI

from routes import reader
from fastapi import FastAPI  # We need a Fast, Scalable API
from handlers.async_ops import worker
from data.mongo_setup import global_init

# Initialize the logger
logger = logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s %(levelname)s : %(message)s",
    handlers=[logging.FileHandler("fam(ily).log"),
              logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)
# Initialize FastAPI
app = FastAPI()
# Include all the routes
app.include_router(reader.router)


async def main() -> None:
    """Entry point for the application"""

    logger.debug("Async main() called")

    while True:
        logger.debug("Async main() loop")

        asyncio.ensure_future(worker())  # Start the worker
        await asyncio.sleep(10)  # Sleep for 10 seconds

        break  # For development purposes (Could be a part of input args)


if __name__ == "__main__":
    """If this is the main file, run the main function"""

    logger.info("Starting up fam(ily)")
    uvicorn.run(app, port=8888)  # Run the app on port 8888

    logger.info("Initializing MongoDB")
    global_init()  # Initialize the database

    logger.info("Starting Backgroung Async Tasks")
    asyncio.run(main())  # Run the main function in the background
