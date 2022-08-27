import logging

from .schema import schema
from fastapi import APIRouter
from data.videos import Video
from fastapi.responses import HTMLResponse

router = APIRouter()
logger = logging.getLogger("my_logger")


@router.get("/")
def read_root():
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
    return HTMLResponse(content=html_content, status_code=200)


@router.get("/get-videos", response_model=schema.Response)
async def get_vids(limit: int, page: int):
    if limit is None or limit <= 1:
        limit = 2

    if page is None or page <= 1:
        page = 1

    logger.info(f"Reading videos with limit {limit} and page {page}")
    result = Video.objects().skip((page - 1) * limit).limit(limit)
    results = [ob.to_mongo().to_dict() for ob in result]
    logger.error(type(results))
    return results
