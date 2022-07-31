from beanie import Document, Indexed
from pydantic import Field, EmailStr

class User(Document):
    username: str = Field(..., unique=True, max_length=15)
    first_name: str = Field(..., max_length=30)
    last_name: str = Field(..., max_length=30)
    email: Indexed(EmailStr, unique=True)
    travels: int = 0

    class Collection:
        name = 'users'