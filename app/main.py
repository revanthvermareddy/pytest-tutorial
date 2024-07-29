from fastapi import FastAPI

from .config import settings
from .routers import root, info


app = FastAPI(
    description=settings.description
)

app.include_router(router=root.router, prefix='', tags=['Root APIs'])
app.include_router(router=info.router, prefix='', tags=['Root APIs'])