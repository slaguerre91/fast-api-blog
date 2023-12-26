from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import engine, get_db
from .. import oauth2

router = APIRouter(
    tags = ["Authentication"]
)

@router.post("/login")
def create_user(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail=f"Invalid credentials")
    
    verified = utils.verify(user_credentials.password, user.password)
    if not verified:
        raise HTTPException(status_code=status.HTTP_403_NOT_FOUND, detail=f"Invalid credentials")
    
    access_token = oauth2.create_token(data = {"user_id" : user.id})

    return {"access token": access_token, "token_type": "bearer"}