from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates    
from fastapi.responses import HTMLResponse

from pydantic import BaseModel

from qr_generator import Qr

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory='templates')

class Item(BaseModel):
    text: str

    def __str__(self):
        return self.text

@app.get("/qr", response_class=HTMLResponse)
async def index(request: Request):
    return template.TemplateResponse("index.html", {"request" : request, "id": 1})

@app.post("/qr")
async def index(request: Request, text: str = Form()):
    Qr.make(text)
    return template.TemplateResponse("index.html", {"request" : request, "id": 1, "qr_ready": text})
