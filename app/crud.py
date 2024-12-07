from sqlalchemy.orm import Session
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from fastapi import HTTPException
from . import models,schemas

def get_user_by_id(db: Session, user_id: str):
    if user_id == "all":
        users = db.query(models.User).all()  # Query to get all users
        if not users:  # Check if empty
            raise HTTPException(status_code=404, detail="No users found in the database.")
        return users
    return db.query(models.User).filter(models.User.user_id == user_id).first()

def delete_user_by_id(db: Session, user_id: str):
    user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()  # Commit the transaction to persist the deletion

    return {"message": "User deleted successfully"}

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
        created_at=user.created_at,
        updated_at=user.updated_at                       
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Success"}