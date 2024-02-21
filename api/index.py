from . import models, schemas, crud
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from fastapi import FastAPI, APIRouter, Depends, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI();

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

apiRouter = APIRouter();

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@apiRouter.get("/", tags=["Root"])
def read_root() -> dict:
    return {"Hello": "World"};


# Create a new todo
@apiRouter.post("/todos/", tags=["Todos"], response_model=schemas.Todo)
def create_todo(todo: schemas.TodoBase, db: Session = Depends(get_db)) -> schemas.Todo:
    return crud.create_todo(db, todo)

@apiRouter.get("/todos/", tags=["Todos"], response_model=list[schemas.Todo])
def read_todos(db: Session = Depends(get_db)) -> list[schemas.Todo]:
    return crud.get_todos(db)

@apiRouter.get("/todos/{todo_id}", tags=["Todos"], response_model=schemas.Todo)
def read_todo(todo_id: int, db: Session = Depends(get_db)) -> schemas.Todo | HTTPException:
    db_todo = crud.get_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@apiRouter.put("/todos/{todo_id}", tags=["Todos"], response_model=schemas.Todo)
def update_todo(todo_id: int, todo: schemas.TodoUpdate, db: Session = Depends(get_db)) -> schemas.Todo | HTTPException:
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# FIXME - sqlalchemy.orm.exc.UnmappedInstanceError: Class 'builtins.NoneType' is not mapped
@apiRouter.delete("/todos/{todo_id}", tags=["Todos"], response_model=schemas.Todo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> schemas.Todo | HTTPException:
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
       raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

app.include_router(apiRouter, prefix="/api");