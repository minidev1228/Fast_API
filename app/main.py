from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud,models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()


@app.post("/user")
async def post_user(user:schemas.UserCreate, db:Session=Depends(get_db)):
    db_user = crud.get_user_by_id(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db,user=user)


@app.get("/user/{user_id}/")
async def get_user_by_id(user_id:str,db:Session=Depends(get_db)):
    print(user_id)
    user = crud.get_user_by_id(db, user_id=user_id)
    return user

@app.delete("/user/{user_id}/")
async def delete_user_by_id(user_id:str,db:Session=Depends(get_db)):
    print(user_id)
    user = crud.delete_user_by_id(db, user_id=user_id)
    return user