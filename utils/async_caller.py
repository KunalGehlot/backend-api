import logging

from yt_api import list_videos

logger = logging.getLogger(__name__)


async def worker(keys) -> None:
    api_res = list_videos(keys[0])
    if api_res.status_code == 403:
        if not keys:
            logger.error("No keys left")
            raise ValueError("No keys left")
        keys.pop()
        api_res = list_videos(keys[0])
    data = clean_res(api_res)
    store_data(data)
    
def clean_res(api_res) -> dict:
    data = api_res.json()
    
    
    return data