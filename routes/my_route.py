import logging

from .schema import schema
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from handlers.db_services import get_videos_paginated, search_video

router = APIRouter()
logger = logging.getLogger("my_logger")


@router.get("/")
async def read_root():
    """Read the root of the API"""

    html_content = """
    <html>
        <head>
            <title>Welcome!</title>
        </head>
        <body>
            <h1>Welcome to fam(ily)!</h1>
            <h3>head over to <a href="/docs">/docs</a> to see the API</h3>
        </body>
    </html>
    """
    # Return the HTML content
    return HTMLResponse(content=html_content, status_code=200)


@router.get("/get-videos", response_model=schema.Response)
async def get_vids(limit: int, page: int):
    """
    Get all the videos in the database
    if limit is -1 OR get a specific page
    of videos with a limit of videos per page

    Args:
        limit (int): The number of videos per page
        page (int): The page number

    Returns:
        Response: The response object

    Raises:
        Default Exception
    """
    try:
        result = await get_videos_paginated(limit, page)
        # Convert to dicts
        results = [ob.to_mongo().to_dict() for ob in result]
        return results
    except Exception as e:
        logger.error(f"Error reading videos: {e}")
        return {"error": str(e)}


@router.get("/search", response_model=schema.Response)
async def search(query: str):
    """
    Search for videos in the database
    Args:
        query (str): The query to search for
    Returns:
        Response: The response object
    Raises:
        Default Exception
    """
    try:
        result = await search_video(query)
        # Convert to dicts
        results = [ob.to_mongo().to_dict() for ob in result]
        if len(results) == 0:
            return {"Error": "No results found"}
        return results
    except Exception as e:
        logger.error(f"Error searching for videos: {e}")
        return {"Error": str(e)}
