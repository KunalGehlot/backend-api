import logging
import requests

logger = logging.getLogger(__name__)

BASE_URL = "https://www.googleapis.com/youtube/v3/search"
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
        res = await requests.get(BASE_URL, headers=HEADERS, params=params)
        res.raise_for_status()
        return res
    except requests.exceptions.HTTPError as errh:
        logger.error("Http Error:", errh)
        raise errh
    except requests.exceptions.ConnectionError as errc:
        logger.error("Error Connecting:", errc)
        raise errc
    except requests.exceptions.Timeout as errt:
        logger.error("Timeout Error:", errt)
        raise errt
    except requests.exceptions.RequestException as err:
        if "403" in str(err):
            logger.error("Quota exceeded")
            return 403
        logger.error("OOps: Something Else", err)
        raise err
