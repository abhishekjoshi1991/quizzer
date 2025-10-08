from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.routers.user_route import router as user_router
from app.routers.quiz_routes import router as quiz_router
from app.database import Base, engine
from app.models.model import User # this need else table won't created
from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # create tables at startup
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title="Quizzer API",
        description="A fast and secure backend for creating, managing, and taking interactive quizzes.",
        version="1.0.0",
        lifespan=lifespan
    )

    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(user_router)
    app.include_router(quiz_router)
    return app

app = create_app()

