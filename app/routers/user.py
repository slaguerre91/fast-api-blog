from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import engine, get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(new_User: schemas.CreateUser, db: Session = Depends(get_db)):
    hashed = utils.hash(new_User.password)
    new_User.password = hashed
    user = models.User(**new_User.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@router.get("/{id}", response_model=schemas.User)
def get_post(id: int, db: Session = Depends(get_db)):
    # cursor.execute('select * from posts where id = %s', (str(id)))
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id of {id} does not exist")
    return user