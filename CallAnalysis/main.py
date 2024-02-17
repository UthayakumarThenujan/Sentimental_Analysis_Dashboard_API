from fastapi import FastAPI
from routes.user import user
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(user)
