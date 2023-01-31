from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.route.api import router as api_router
from app.core.config import get_app_settings


def get_application() -> FastAPI:
    settings = get_app_settings()

    # '**' takes a dict and extracts its contents and passes them as parameters to a function.
    app = FastAPI(**settings.fastapi_kwargs)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)

    return app


app = get_application()
