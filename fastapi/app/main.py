"""
API applicatoin
"""
import motor.motor_asyncio
from fastapi import FastAPI
from .models import SessionCollection

MONGO_DB = "enersense_db"
MONGO_COLLECTION = "sessions"


app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(
    "mongodb://root:password@mongo:27017")
db = client.get_database(MONGO_DB)
session_collection = db.get_collection(MONGO_COLLECTION)


@app.get(
    "/",
    response_description="List all sessions",
    response_model=SessionCollection,
    response_model_by_alias=False,
)
async def read_root():
    return SessionCollection(sessions=await session_collection.find().to_list(1000))
