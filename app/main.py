from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db
from typing import List

models.Base.metadata.create_all(bind=engine) #테이블 생성

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/politicians/", response_model=list[schemas.Politician])
def read_politicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    politicians = crud.get_politicians(db, skip=skip, limit=limit)
    return politicians

@app.get("/politicians/search/", response_model=List[schemas.Politician])
def search_politicians(name: str, birth_date: str, db: Session = Depends(get_db)):
    politicians = crud.get_politicians_by_name_and_birth_date(db, name=name, birth_date=birth_date)
    return politicians

@app.get("/wordcloud-all/", response_model=list[schemas.AllWordcloud])
def read_all_wordcloud(db: Session = Depends(get_db)):
    wordcloud_items = crud.get_all_wordcloud(db)
    return wordcloud_items