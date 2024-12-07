from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from . import models,schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip:int=0, limit:int=100):
#     # return db.query(models.User).offset(skip).limit(limit).all()
#     return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user:schemas.UserCreate):
    db_user = models.User(
        user_id=user.user_id,
        username=user.username,
        password_hash=user.password_hash,
        email=user.email,
        first_name=user.first_name,
        last_name=user.last_name,
        role=user.role,
        profile_picture=user.profile_picture,
        bio=user.bio,
        created_at=DateTime(user.created_at),
        updated_at=DateTime(user.updated_at)                       
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user


# def get_todos(db: Session, skip:int=0, limit: int=100):
#     return db.query(models.Todo).offset(skip).limit(limit).all()


# def create_user_todo(db:Session, todo:schemas.TodoCreate, user_id : int):
#     db_todo = models.Todo(**todo.model_dump(),owner_id=user_id )
#     db.add(db_todo)
#     db.commit()
#     db.refresh(db_todo)
#     return db_todo


# NOTE :
# - add that instance object to your database session.
# - commit the changes to the database (so that they are saved).
# - refresh your instance (so that it contains any new data from the database, like the generated ID).