from sqlalchemy.orm import Session
from sqlalchemy import text
from src.database.core import load_sql
from src.users.models import UserIn, UserOut

def create_user(session: Session, data: UserIn) -> UserOut:
    stmt = text(load_sql("users/create_user.sql"))
    row = session.execute(stmt, data.dict()).first()
    session.commit()
    return UserOut(**row._mapping)

def get_all_users(session: Session) -> list[UserOut]:
    stmt = text(load_sql("users/get_all_users.sql"))
    rows = session.execute(stmt).all()
    return [UserOut(**r._mapping) for r in rows]

def get_user_by_id(session: Session, user_id: int) -> UserOut | None:
    stmt = text(load_sql("users/get_user_by_id.sql"))
    row = session.execute(stmt, {"user_id": user_id}).first()
    return UserOut(**row._mapping) if row else None

def update_user(session: Session, user_id: int, data: UserIn) -> UserOut | None:
    params = data.dict(); params["user_id"] = user_id
    stmt = text(load_sql("users/update_user.sql"))
    row = session.execute(stmt, params).first()
    session.commit()
    return UserOut(**row._mapping) if row else None

def delete_user(session: Session, user_id: int) -> bool:
    stmt = text(load_sql("users/delete_user.sql"))
    row = session.execute(stmt, {"user_id": user_id}).first()
    session.commit()
    return bool(row)
