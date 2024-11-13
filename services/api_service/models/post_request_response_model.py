from uuid import UUID
from pydantic import BaseModel


class PostRequestResponseModel(BaseModel):
    id: UUID
    result: str

    class Config:
        extra = "forbid"
