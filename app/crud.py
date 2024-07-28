# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_politicians(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.Politician).offset(skip).limit(limit).all()
