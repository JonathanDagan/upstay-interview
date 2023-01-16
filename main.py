from fastapi import FastAPI
from pydantic import BaseModel

import time
from calculator import Calculator

app = FastAPI()


class Calculation(BaseModel):
    expression: str


calc = Calculator()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/calculate")
async def calculate(calculation: Calculation):
    start_time = time.time()
    result = calc.calculate(calculation.expression)
    end_time = time.time()
    return {"result": result, "time": end_time - start_time}
