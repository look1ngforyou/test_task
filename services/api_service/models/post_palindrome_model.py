from pydantic import BaseModel


class PostPalindromeModel(BaseModel):
    palindrome: bool

    class Config:
        extra = "forbid"
