from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database.core import SessionLocal
from src.users.service import (
    create_user, get_all_users,
    get_user_by_id, update_user, delete_user
)
from src.users.models import UserIn, UserOut

router = APIRouter(prefix="/users", tags=["users"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=UserOut, status_code=201)
def api_create_user(data: UserIn, db: Session = Depends(get_db)):
    return create_user(db, data)

@router.get("/", response_model=list[UserOut])
def api_get_all(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/{user_id}", response_model=UserOut)
def api_get_one(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(404, "Not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
def api_update_user(user_id: int, data: UserIn, db: Session = Depends(get_db)):
    user = update_user(db, user_id, data)
    if not user:
        raise HTTPException(404, "Not found")
    return user

@router.delete("/{user_id}", status_code=204)
def api_delete_user(user_id: int, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(404, "Not found")
