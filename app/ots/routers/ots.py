
from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas, crud
from ..database import SessionLocal, engine


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter()


@router.get('/')
async def ots_service(request: Request):
    service_spec = {
        'durations': ['1hour', '1day']
    }
    return service_spec


@router.get('/debug/{ots_id}')
async def get_ots(ots_id: int, db: Session = Depends(get_db)):
    return crud.get_ots(ots_id, db)


@router.get('/secret/{path}')
async def reveal_secret(path: str, db: Session = Depends(get_db)):
    return crud.reveal_secret(path, db)


@router.post('/', response_model=schemas.Ots)
async def creat_ots(ots: schemas.OtsCreate, db: Session = Depends(get_db)):
    ots = crud.create_ots(ots=ots, db=db)
    return ots['path']


@router.get('/debug')
async def show_all_ots(db: Session = Depends(get_db)):
    ots = crud.show_all(db=db)
    return ots
