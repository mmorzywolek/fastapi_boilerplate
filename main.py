from fastapi import FastAPI
import articles
import auth
import users
from db import database, metadata, engine

metadata.create_all(engine)

app = FastAPI()

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()

@app.get("/")
def index():
    return {'Message': 'First page'}

app.include_router(articles.router)
app.include_router(users.router)
app.include_router(auth.router)
