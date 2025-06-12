from fastapi import FastAPI
from sqlalchemy import text
from src.users.controller import router as user_router
from src.database.core import engine

app = FastAPI()
app.include_router(user_router)

@app.on_event("startup")
def apply_migrations():
    with engine.connect() as connection:
        migration_sql = open("src/sql/db_migration.sql").read()
        connection.execute(text(migration_sql))

@app.get("/")
def root():
    return {"message": "CRUD FastAPI + raw SQL, migration runs automatically on startup"}
