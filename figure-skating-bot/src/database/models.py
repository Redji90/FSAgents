from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base

class Competition(Base):
    __tablename__ = "competitions"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    date = Column(Date)
    location = Column(String)
    category = Column(String)
    discipline = Column(String)
    
    results = relationship("Result", back_populates="competition")

class Skater(Base):
    __tablename__ = "skaters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    country = Column(String)
    birth_date = Column(Date, nullable=True)
    
    results = relationship("Result", back_populates="skater")

class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True, index=True)
    competition_id = Column(Integer, ForeignKey("competitions.id"))
    skater_id = Column(Integer, ForeignKey("skaters.id"))
    
    short_program_score = Column(Float)
    free_program_score = Column(Float)
    total_score = Column(Float)
    rank = Column(Integer)
    
    competition = relationship("Competition", back_populates="results")
    skater = relationship("Skater", back_populates="results")