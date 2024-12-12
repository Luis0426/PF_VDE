from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

# Crea la aplicación FastAPI
app = FastAPI()

# Configura directorios de plantillas y archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Ruta para la página principal
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Documento Proyecto Final"})


# Ruta para pagina de graficas
@app.get("/graficas", response_class=HTMLResponse)
async def read_pagina2(request: Request):
    return templates.TemplateResponse("graficas.html", {"request": request})

