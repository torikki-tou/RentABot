from fastapi import FastAPI

from src.api.api import api_router


app = FastAPI()
app.include_router(router=api_router, prefix='/api')

