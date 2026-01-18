from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.v1.health import router as health_router
from app.schemas.task import TaskCreate, TaskResponse
from app.core import tasks as task_service
from app.db.deps import get_db
from app.api.v1 import auth
from app.core.security import get_current_user
from app.models.user import User

router = APIRouter(tags=["v1"])
router.include_router(health_router)
router.include_router(auth.router)

@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks(db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    return task_service.list_tasks(db, current_user)

@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    return task_service.create_task(db, current_user, task.title)

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    return task_service.get_task(db, current_user, task_id)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    return task_service.update_task(db, current_user, task_id, task.title)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user : User = Depends(get_current_user)):
    task_service.delete_task(db, current_user, task_id)
    return {"detail": "Task deleted."}