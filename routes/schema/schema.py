from pydantic import BaseModel
from typing import List, Optional


class Response(BaseModel):
    Hello: str
