from pydantic import BaseModel, Field


class GetMethodRequestResponse(BaseModel):
    result: str

    class Config:
        extra = "forbid"
