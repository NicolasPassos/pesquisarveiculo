from pydantic import BaseModel
from typing import Optional, Any, Dict
from enum import Enum

class ResponseModel(BaseModel):
    Message: Optional[str]
    Status_code: Optional[int]
    Detail: Optional[str]
    Response: str | list[Dict[str, Any]] | Dict[str, Any]