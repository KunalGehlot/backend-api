from typing import List, Optional
from pydantic import BaseModel, validator


class Video(BaseModel):
    """Video model"""

    title: str
    videoId: str
    description: Optional[str]
    publishedAt: str
    channelTitle: str
    thumb: Optional[str]
    URL: Optional[str]

    @validator("publishedAt", pre=True)
    def convert_to_datetime(cls, v):
        """Convert the publishedAt datetime object to a iso string"""
        return v.strftime("%Y-%m-%dT%H:%M:%SZ")


class Response(BaseModel):
    """Response model"""

    __root__: List[Video]
