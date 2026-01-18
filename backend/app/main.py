from fastapi import FastAPI
from app.api.v1.router import router as v1_router
from app.db.session import engine
from app.db.base import Base
from app.models.task import Task
from app.models.user import User

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(v1_router, prefix="/api/v1")

@app.get("/")
def root():
    return {"status" : "OK"}