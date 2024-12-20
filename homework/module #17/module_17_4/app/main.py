from fastapi import FastAPI
from app.routers import user


app = FastAPI()


@app.get('/')
async def welcome_message() -> dict:
    return {'message': 'Welcome to Taskmanager'}


app.include_router(user.router)
