from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Skater(Base):
    __tablename__ = 'skaters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String, nullable=False)

class Competition(Base):
    __tablename__ = 'competitions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, nullable=False)

class Result(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    skater_id = Column(Integer, nullable=False)
    competition_id = Column(Integer, nullable=False)
    score = Column(Float, nullable=False)
    rank = Column(Integer, nullable=False)