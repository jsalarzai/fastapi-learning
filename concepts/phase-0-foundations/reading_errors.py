from pydantic import BaseModel


class Task(BaseModel):
    title: str
    priority: int
    done: bool


task = Task(title="Buy groceries", priority="high", done="yes")
print(task)
