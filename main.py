from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class EmpModel(BaseModel):
    id: int
    name: str
    age: int
   

# Internal class (optional)
class Emp:
    def __init__(self, name, age, id):
        self.id = id
        self.name = name
        self.age = age

employees = []

# Sample data
employees.append(EmpModel(name="John Doe", age=30, id=1))
employees.append(EmpModel(name="Jane Smith", age=28, id=2))
employees.append(EmpModel(name="Peter Pan", age=24, id=3))


@app.get("/emp")
async def root():
    return employees


@app.post("/emp")
async def root(emp: EmpModel):
    employees.append(emp)
    return employees

@app.put("/emp")
async def root(id, emp: EmpModel):
    
    return employees

# http://127.0.0.1:8000 