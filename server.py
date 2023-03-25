from fastapi import  FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

app:FastAPI = FastAPI ()


app.mount('/output', StaticFiles(directory="output"), name="static")


if __name__ == "__main__":
    print("Server starting...")
    uvicorn.run(app, host="0.0.0.0", port=5555)