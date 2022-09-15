from operator import mod
from fastapi import FastAPI
from pydantic import BaseModel

class Model(BaseModel):
    status: int
    message: str

    
app = FastAPI()


@app.post("/qr")
async def index(model: Model):
    return model