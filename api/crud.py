from sqlalchemy.orm import Session
from . import models, schemas

def get_todo(db: Session, todo_id: int):
    todo_data = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    return todo_data

def get_todos(db: Session):
    todos_data = db.query(models.Todo).all()
    return todos_data

def create_todo(db: Session, todo: schemas.TodoBase):
    todo_data = models.Todo(**todo.model_dump())
    db.add(todo_data)
    db.commit()
    db.refresh(todo_data)
    return todo_data

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    todo_data = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if(todo.title): 
        todo_data.title = todo.title
    if(todo.done):
        todo_data.done = todo.done
    db.commit()
    db.refresh(todo_data)
    return todo_data

def delete_todo(db: Session, todo_id: int):
    todo_data = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    db.delete(todo_data)
    db.commit()
    return todo_data


    
    