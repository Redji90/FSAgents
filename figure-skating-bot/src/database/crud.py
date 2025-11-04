from sqlalchemy.orm import Session
from . import models
from datetime import date
from typing import Optional

def create_competition(
    db: Session, 
    name: str, 
    date: date, 
    location: str, 
    category: str, 
    discipline: str
):
    db_competition = models.Competition(
        name=name,
        date=date,
        location=location,
        category=category,
        discipline=discipline
    )
    db.add(db_competition)
    db.commit()
    db.refresh(db_competition)
    return db_competition

# ...остальные CRUD операции...
