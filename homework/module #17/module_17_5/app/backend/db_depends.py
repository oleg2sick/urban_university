from .db import SessionLocal

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()