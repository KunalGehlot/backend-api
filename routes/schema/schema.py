from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, validator


class Video(BaseModel):
    title: str
    videoId: str
    description: Optional[str]
    publishedAt: str
    channelTitle: str
    thumb: Optional[str]
    url: Optional[str]

    @validator("publishedAt", pre=True)
    def convert_to_datetime(cls, v):
        return v.strftime("%Y-%m-%dT%H:%M:%SZ")


class Response(BaseModel):
    __root__: List[Video]
