
from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.schema import CreateTable


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship('Task', back_populates='user')


print(CreateTable(User.__table__))


router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users():
    pass


@router.get('/user_id')
async def user_by_id():
    pass


@router.post('/create')
async def create_user():
    pass


@router.put('/update')
async def update_user():
    pass


@router.delete('/delete')
async def delete_user():
    pass
