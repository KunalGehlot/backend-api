import logging

from .schema import schema
from fastapi import APIRouter
from data.videos import Video
from fastapi.responses import HTMLResponse

router = APIRouter()
logger = logging.getLogger("my_logger")


@router.get("/")
def read_root():
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
        if limit == -1:
            result = Video.objects()  # Get all the videos
            # Convert to dicts
            results = [ob.to_mongo().to_dict() for ob in result]
            return results
        # If no limit is provided, default to 1
        elif limit is None or limit <= 1:
            limit = 2
            # If no page is provided, default to 1
            if page is None or page <= 1:
                page = 1

            logger.info(f"Reading videos with limit {limit} and page {page}")
            result = (
                Video.objects().skip((page - 1) * limit).limit(limit)
            )  # Get the videos
            # Convert to dicts
            results = [ob.to_mongo().to_dict() for ob in result]
            return results
    except Exception as e:
        logger.error(f"Error reading videos: {e}")
        return {"error": str(e)}
