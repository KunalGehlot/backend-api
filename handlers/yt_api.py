import logging
import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://www.googleapis.com/youtube/v3/search"
# Some default headers for the requests
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


async def list_videos(
    key,
    q="Food",  # I'm just hungry...
    order="date",
    qtype="video",
    max_results=25,
    part="snippet",
    published_after="2019-01-01T00:00:00Z",
) -> requests.Response:
    """
    Simple function to list videos from the YouTube API.

    Args:
        key (str): The YouTube API key
        q (str): The search query
        order (str): The order to return the videos in
        qtype (str): The type of videos to return
        max_results (int): The maximum number of videos to return
        part (str): Search resource properties that API response will include
        published_after (str): The earliest date to return videos from
    Raises:
        Exception: If the YouTube API returns an error
    Returns:
        requests.Response: The response from the YouTube API
    """

    params = {
        "q": q,
        "key": key,
        "type": qtype,
        "part": part,
        "order": order,
        "maxResults": max_results,
        "publishedAfter": published_after,
    }

    try:
        res = await requests.get(
            BASE_URL, headers=HEADERS, params=params
        )  # GET request to the YouTube API
        res.raise_for_status()
        # Raise an exception if the request was not successful
        return res
    # Handle the HTTP error
    except requests.exceptions.HTTPError as errh:
        logger.error("Http Error:", errh)
        raise errh
    # Handle the connection error
    except requests.exceptions.ConnectionError as errc:
        logger.error("Error Connecting:", errc)
        raise errc
    # Handle the timeout error
    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error:", errt)
        raise errt
    # Handle all other errors
    except requests.exceptions.RequestException as err:
        if "403" in str(err):  # Handle the 403 error
            logger.error("Quota exceeded")
            return 403
        logger.error("OOps: Something Else", err)
        raise err  # Raise the error to the caller
