from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.models.user import User

def create_task(db: Session, user: User, title:str) -> Task:
    new_task = Task(
        title = title,
        completed = False,
        user_id = user.id
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def list_tasks(db:Session, user: User) -> list[Task]:
    return db.query(Task).filter(Task.user_id == user.id).all()

def get_task(db: Session, user: User, task_id : int) -> Task:
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    return task

def update_task(db: Session, user: User, task_id: int, title:str) -> Task:
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    task.title = title
    db.commit()
    db.refresh(task)
    return task

def delete_task(db:Session, user: User, task_id: int) -> None:
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user.id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found.")
    db.delete(task)
    db.commit()