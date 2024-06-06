from fastapi import FastAPI
from api.router.TestRouter import router
from api.db import init_db

app = FastAPI()

app.include_router(router)


@app.on_event("startup")
async def on_startup():
    await init_db()
