# app/models.py
# 데이터 베이스 테이블 정의

from sqlalchemy import Column, Integer, String, Date, Float, JSON
from app.database import Base

class Politician(Base):
    __tablename__ = "politicians"

    id = Column(Integer, primary_key=True, index=True)  # 고유 id
    name = Column(String(255), index=True)  # 의원명, VARCHAR 길이 지정
    birth_date = Column(Date)  # 생년월일, yy-mm-dd
    political_score = Column(Float, nullable=True)  # 정치성향 점수, 실수형
    wordcloud_result = Column(JSON)  # 워드 클라우드 결과, JSON 형식
    speech_count = Column(Integer ,default=0)  # 발언량

class AllWordcloud(Base):
    __tablename__ = "all_wordcloud"

    term = Column(Integer, primary_key=True, index=True)
    wordcloud_result = Column(JSON)
