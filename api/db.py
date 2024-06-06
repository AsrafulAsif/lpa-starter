from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from api.config import settings
from api.model.Entity import User


async def init_db():
    client = AsyncIOMotorClient("mongodb+srv://reminder:NM3dyBFRBhH9lN9x@reminder.xuvwf3w.mongodb.net/reminder")
    await init_beanie(database=client.reminder, document_models=[User])
