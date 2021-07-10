import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_router import router

def get_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in ['*']],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # application.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URL)
    application.include_router(router, prefix='')
    # application.add_exception_handler(CustomException, http_exception_handler)

    return application


app = get_application()


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)