from sqlalchemy.orm import Session
from . import models
from datetime import date
from typing import List, Dict

async def create_competition(
    db: Session,
    name: str,
    date: date,
    location: str,
    category: str,
    discipline: str
) -> models.Competition:
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

async def get_competitions(db: Session, skip: int = 0, limit: int = 100) -> List[models.Competition]:
    return db.query(models.Competition).offset(skip).limit(limit).all()

async def create_result(
    db: Session,
    competition_id: int,
    skater_id: int,
    short_program: float,
    free_program: float,
    total: float,
    rank: int
) -> models.Result:
    db_result = models.Result(
        competition_id=competition_id,
        skater_id=skater_id,
        short_program_score=short_program,
        free_program_score=free_program,
        total_score=total,
        rank=rank
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
