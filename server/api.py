from fastapi import FastAPI, WebSocket
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client.syncboard

@app.get("/")
async def root():
    return {"message": "Welcome to SyncBoard!"}
