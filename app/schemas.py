# app/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Dict

class PoliticianBase(BaseModel):
    name: str
    birth_date: date
    political_score: float
    wordcloud_result: Dict  # 워드 클라우드 결과, JSON 형식
    speech_count: int

class PoliticianCreate(PoliticianBase):
    pass

class Politician(PoliticianBase):
    id: int

    class Config:
        orm_mode = True
