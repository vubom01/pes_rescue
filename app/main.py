import uvicorn
from fastapi import FastAPI
from app.api.api_router import router

app = FastAPI()

app.include_router(router=router, prefix='')

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)