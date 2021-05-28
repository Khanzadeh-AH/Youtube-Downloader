from fastapi import FastAPI
import uvicorn

from app.views import home, streaminfo

app = FastAPI()


def configure():
    app.include_router(home.router)
    app.include_router(streaminfo.router)


configure()

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=5000)

