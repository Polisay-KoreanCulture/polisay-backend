# app/schemas.py
from pydantic import BaseModel
from datetime import date
from typing import Optional, Dict

class PoliticianBase(BaseModel):
    name: str
    birth_date: date
    political_score: Optional[float] = None 
    wordcloud_result: Optional[Dict] = {}   # 워드 클라우드 결과, JSON 형식
    speech_count: Optional[int] = 0

class PoliticianCreate(PoliticianBase):
    pass

class Politician(PoliticianBase):
    id: int

    class Config:
        orm_mode = True
