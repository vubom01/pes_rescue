import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_router import router
from app.core.config import settings


def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in ['*']],
        allow_credentials=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(router, prefix=settings.API_PREFIX)

    return application


app = get_application()
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)