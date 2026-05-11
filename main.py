from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api import router as api_router

app = FastAPI(title="SQL智辅 · Python版")

app.include_router(api_router)
app.mount("/", StaticFiles(directory="app/static", html=True), name="static")
