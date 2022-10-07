from pydantic import BaseModel

class Todo(BaseModel):
    contents: str