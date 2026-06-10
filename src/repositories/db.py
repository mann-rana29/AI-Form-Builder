from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

client = AsyncIOMotorClient = None

async def connect_to_db(app):
    global client
    
    MONGO_URI = os.getenv("MONGO_URI")
    if not MONGO_URI:
        raise ValueError("MONGO_URI variable is missing!")
    
    client = await AsyncIOMotorClient(MONGO_URI)

    print("MongoDB Atlas is successfully connected.")


async def close_db(app):
    global client

    if client:
        await client.close()
        print("MongoDB Atlas connection closed.")

async def get_db(app):
    global client

    DB_NAME = os.getenv("DB_NAME")

    if not DB_NAME:
        raise ValueError("DB_NAME variable is missing!")

    if client is None:
        raise RuntimeError("Database client is not initialized.")
    
    return client[DB_NAME]