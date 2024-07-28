from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine) #테이블 생성

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}



@app.get("/politicians/", response_model=list[schemas.Politician])
def read_politicians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    politicians = crud.get_politicians(db, skip=skip, limit=limit)
    return politicians