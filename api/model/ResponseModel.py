from pydantic import BaseModel
from typing import Any


class SimpleResponse(BaseModel):
    message: str = "Successful."
    statusCode: int = 200


class BaseResponse(SimpleResponse):
    data: Any
