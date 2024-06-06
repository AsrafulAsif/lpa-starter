from beanie import Document
from pydantic import Field
from bson import ObjectId


class User(Document):
    id: ObjectId
    name: str = Field(...)
    age: str = Field(...)

    class Settings:
        name = "users"
        allow_population_by_field_name = True
        json_encoders = {
            ObjectId: str
        }
