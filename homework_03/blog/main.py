import uvicorn
from fastapi import FastAPI
from view import router as ping

app = FastAPI()
app.include_router(ping)

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True,
    )