from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Todo(BaseModel):
    id: int
    task: str

todos: List[Todo] = []

@app.post("/add")
def add(todo: Todo):
    todos.append(todo)
    return {"message":"Task addded"}

@app.get("/list")
def list_all():
    return todos

@app.delete("/delete/{todo_id}")
def delete(todo_id: int):
    for i,t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(i)
            return {"message":"Task deleted"}
    raise HTTPException(404,"Task not found")