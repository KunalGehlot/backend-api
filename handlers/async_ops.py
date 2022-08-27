import logging

from yt_api import list_videos
from keys import get_keys, update_keys, process_keys
from db import store_data

logger = logging.getLogger(__name__)


async def worker() -> None:
    """
    Background task that runs in parallel to other tasks.
    It fetches the data from the API and stores it in the database.

    Args: None
    Raises: None
    Returns: None
    """

    keys = get_keys()
    k_obj, index = process_keys(keys)
    api_res = await list_videos(k_obj["key"])

    if api_res == 403:
        logging.warn("Updating the key status")
        k_obj["status"] = "Quota exceeded"  # Update the status of the key
        keys[index] = k_obj  # Update the key in the keys list
        update_keys(keys)  # Update the keys in the file
        logging.warn("Skipping the call")
        return

    logger.debug("Cleaning the response")
    data = clean_res(api_res)  # Pick the values needed to be stored
    logger.info("Storing the data")
    store_data(data)  # Store the data in the mongodb database


def clean_res(api_res) -> dict():
    """
    Processes the response from the API and returns
    the data to be stored in the database.

    Args: api_res - response from the API
    Raises: None
    Returns: list of data to be stored in the database
    """

    data_list = list()
    raw = api_res.json()
    for item in raw["items"]:
        logger.debug("Video: %s", item["snippet"]["title"])
        data = dict()

        data["title"] = item["snippet"]["title"]
        data["description"] = item["snippet"]["description"]
        data["publishedAt"] = item["snippet"]["publishedAt"]
        data["channelTitle"] = item["snippet"]["channelTitle"]
        data["thumb"] = item["snippet"]["thumbnails"]["high"]["url"]
        data["URL"] = "http://youtube.com/watch?v=" + item["id"]["videoId"]

        data_list.append(data)

    return data_list
