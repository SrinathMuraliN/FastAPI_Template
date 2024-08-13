import os
from contextlib import asynccontextmanager
from typing import AsyncIterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend
from starlette.middleware.sessions import SessionMiddleware

from apps.user_management import views


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    """
    Cache lifespan initialization
    """
    FastAPICache.init(InMemoryBackend())
    yield


def setup_app():
    """
    Function to setup fastapi application
    """
    fastapi_app = FastAPI(lifespan=lifespan)
    fastapi_app.add_middleware(SessionMiddleware, secret_key="fastapi")
    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in os.environ["ALLOWED_ORIGIN"]],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return fastapi_app


app = setup_app()

# Including the router
app.include_router(views.router, prefix="/api", tags=["Login"])
