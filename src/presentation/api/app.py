from fastapi import FastAPI

from src.presentation.api.v1.router import router as v1_router


def create_app() -> FastAPI:
    app = FastAPI(
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
    )
    app.include_router(v1_router, prefix="/api")
    return app


app = create_app()
