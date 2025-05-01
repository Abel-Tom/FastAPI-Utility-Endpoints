import time
from fastapi import FastAPI
from api.routes import router
from api.email import email_router

app = FastAPI(title="FastAPI Demo App")

app.include_router(router)
app.include_router(email_router)

