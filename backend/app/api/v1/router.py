from fastapi import APIRouter, HTTPException
from app.api.v1.health import router as health_router
from app.schemas.task import TaskCreate, TaskResponse
from app.core import tasks as task_service

router = APIRouter(tags=["v1"])
router.include_router(health_router)

@router.get("/tasks", response_model=list[TaskResponse])
def list_tasks():
    return task_service.list_tasks()

@router.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id : int):
    return task_service.get_task(task_id)

@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate):
    return task_service.update_task(task_id, task.title)

@router.post("/tasks", response_model=TaskResponse)
def create_task(task : TaskCreate):
    return task_service.create_task(task.title)

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int):
        task_service.delete_task(task_id)
        return {"detail" : "Task deleted."}