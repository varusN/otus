import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/ping/")
def pong():
    return {
        "message": "pong",
    }


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )