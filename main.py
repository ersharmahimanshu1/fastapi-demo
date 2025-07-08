from fastapi import FastAPI
from pydantic import BaseModel
# what is basemodel
# what is pydantic
# how many type of variable 


from typing import List

app = FastAPI()

class EmpModel(BaseModel):
    name: str
    age: int

class Emp: 
    def __init__(self, name, age):
        self.name = name
        self.age = age


    name = ""
    age= 0

employees = []


# Create Employee objects
emp1 = Emp("John Doe", "101")
emp2 = Emp("Jane Smith", "102")
emp3 = Emp("Peter Pan", "103")

# Add Employee objects to the list
employees.append(emp1)
employees.append(emp2)
employees.append(emp3)

@app.get("/hello") #route (/hello)
def root():
    return employees



# @app.get("/bye")
# async def root():
#     return {"message": "bye"}

@app.post("/emp")
def create_items(emp: EmpModel):
    employees.append(emp)
    return employees



# value add kr rhe h vo value permanent add honi chahiye 


     






# from fastapi import FastAPI

# app = FastAPI()

# @app.post("/item")
# def create_item():
#     return {"message": "Item created"}

# from fastapi import APIRouter, FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None

# app = FastAPI()
# router = APIRouter()

# @router.post("/items/")
# def create_item(item: Item):
#     return {"message": "Item created"}

# app.include_router(router)


# http://127.0.0.1:8000 