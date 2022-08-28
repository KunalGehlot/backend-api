import logging

from datetime import datetime
from data.videos import Video

logger = logging.getLogger("my_logger")


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

    return True  # Can be used to check for success


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
    video.publishedAt = datetime.strptime(vid["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")
    video.channelTitle = vid["channelTitle"]
    video.thumb = vid["thumb"]
    video.URL = vid["URL"]

    video.save()
    logger.info(f"Video \"{vid['title']}:{vid['videoId']}\" saved in the database")

    return True  # Can be used to check for success


def search_video_by_id(video_id: str):
    """
    Search for a video by its ID.

    Args: video_id (str) - ID of the video to be searched for
    Returns: Video object if found, None otherwise
    Raises: None
    """

    return Video.objects(videoId=video_id).first()


async def get_videos_paginated(limit: int, page: int):
    """
    Get videos paginated.

    Args: limit (int) - limit of videos to be returned
    page (int) - page number
    Returns: list of Video query
    Raises: None
    """

    if limit == -1:
        result = Video.objects()  # Get all the videos
    # If no limit is provided, default to 1
    else:
        if limit is None or limit <= 1:
            limit = 2
        # If no page is provided, default to 1
        if page is None or page <= 1:
            page = 1

        logger.info(f"Reading videos with limit {limit} and page {page}")
        result = (
            Video.objects()
            .order_by("-publishedAt")
            .skip((page - 1) * limit)
            .limit(limit)
        )  # Get the videos

    return result


async def search_video(query: str):
    """
    Search for a video by its title and descriptio.

    Args: search_term (str) - title of the video to be searched for
    Returns: Video object if found, None otherwise
    Raises: None
    """
    logger.info(f"Searching for videos with query {query}")
    result = Video.objects.search_text(query).order_by("$text_score")
    return result
