from sqlalchemy import Column, Integer, String, ForeignKey, Boolean

from .database import Base

class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(60), index=True)
    done = Column(Boolean, default=False)
    
