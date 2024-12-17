from fastapi import FastAPI, status, Body, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_all_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str, age: int) -> str:
    current_id = max((user.id for user in users), default=0) + 1
    new_user = User(id=current_id, username=username, age=age)
    users.append(new_user)
    return f'User {current_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: int, username: str, age: int) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f'The user {user_id} is updated'
    raise HTTPException(status_code=404, detail='User was not found')


@app.delete('/user/{user_id}')
async def delete_user(user_id: int) -> str:
    for user in users:
        if user.id == user_id:
            users.pop(user_id - 1)
            return f'The user {user_id} was deleted'
    raise HTTPException(status_code=404, detail='User was not found')
