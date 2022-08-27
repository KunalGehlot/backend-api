from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class Video(BaseModel):
    title: str
    videoId: str
    description: Optional[str]
    publishedAt: datetime
    channelTitle: str
    thumb: Optional[str]
    url: Optional[str]


class Response(BaseModel):
    videos: List[Video]
