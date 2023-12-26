from typing import List
from fastapi import FastAPI, Depends
from . import models, schemas
from .database import engine, get_db
from sqlalchemy.orm import Session
from sqlalchemy import func
from .routers import post, user, vote, auth
from .config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(vote.router)
app.include_router(auth.router)


@app.get("/", response_model=List[schemas.PostOut])
def read_root(db: Session = Depends(get_db), limit: int = 10, skip: int = 0):
    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    return results


