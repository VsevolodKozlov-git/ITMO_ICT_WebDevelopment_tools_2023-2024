from fastapi import FastAPI, Depends
import models
from sqlmodel import Session
from db import init_db, get_session_depends
from pydantic import ValidationError

app = FastAPI()


@app.on_event("startup")
def on_startup():
    init_db()



@app.post('/user/create/')
def create_user(user: models.UserBase, session:Session=Depends(get_session_depends)):
    user = models.User.model_validate(user)
    session.add(user)
    session.commit()
    session.refresh(user)
    return {'data': user}

