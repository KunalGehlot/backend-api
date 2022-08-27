from asyncio.log import logger
from data.videos import Video


async def store_data(data: list):
    """
    Store data in the database by looping through
    the data and storing each data in the database.

    Args: data (list) - data to be stored in the database
    Returns: None
    Raises: None
    """

    for vid in data:
        if search_video_by_id(vid["videoId"]):
            logger.warn(
                f"Video \"{vid['title']}:{vid['videoId']}\" already exists in the database, Skipping"
            )
            continue
        await store_vid(vid)

    return True


async def store_vid(vid: dict):
    """
    Store data in the database by looping through
    the data and storing each data in the database.

    Args: data (list) - data to be stored in the database
    Returns: None
    Raises: None
    """

    video = Video()

    video.title = vid["title"]
    video.videoId = vid["videoId"]
    video.description = vid["description"]
    video.publishedAt = vid["publishedAt"]
    video.channelTitle = vid["channelTitle"]
    video.thumb = vid["thumb"]
    video.URL = vid["URL"]

    video.save()
    logger.info(f"Video \"{vid['title']}:{vid['videoId']}\" saved in the database")

    return True


def search_video_by_id(video_id: str):
    """
    Search for a video by its ID.

    Args: video_id (str) - ID of the video to be searched for
    Returns: Video object if found, None otherwise
    Raises: None
    """

    return Video.objects(videoId=video_id).first()
