from fastapi import HTTPException

tasks_db : list[dict] = []

def create_task(title:str) -> dict:
    new_task = {
        "id" : len(tasks_db) + 1,
        "title" : title,
        "completed" : False
    }
    tasks_db.append(new_task)
    return new_task

def list_tasks() -> list[dict]:
    return tasks_db

def get_task(task_id : int) -> dict:
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

def update_task(task_id: int, title:str) -> dict:
    for task in tasks_db:
        if task["id"] == task_id:
            task["title"] = title
            return task
    raise HTTPException(status_code=404, detail="Task not found.")

def delete_task(task_id: int) -> dict:
    for index, task in enumerate(tasks_db):
        if task["id"] == task_id:
            tasks_db.pop(index)
            return 
    raise HTTPException(status_code=404, detail="Task not found.")
