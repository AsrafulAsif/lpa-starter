from beanie import Document
from pydantic import Field
from bson import ObjectId


class User(Document):
    id: ObjectId = Field(default_factory=ObjectId, alias="id")
    name: str = Field(...)

    # class Settings:
    #     name = "User"
    #     allow_population_by_field_name = True
    #     # json_encoders = {
    #     #     ObjectId: str
    #     # }

    class Config:
        name = "User"
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
