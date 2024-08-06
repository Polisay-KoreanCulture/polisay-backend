# app/crud.py
from sqlalchemy.orm import Session
from app import models, schemas

def get_politicians(db: Session, skip: int = 0, limit: int = 500):
    return db.query(models.Politician).offset(skip).limit(limit).all()


def get_politicians_by_name_and_birth_date(db: Session, name: str, birth_date: str):
    return db.query(models.Politician).filter(models.Politician.name == name, models.Politician.birth_date == birth_date).all()

def get_all_wordcloud(db: Session):
    return db.query(models.AllWordcloud).all()