import uvicorn  # Sweet little Async SGI
from routes import yt
from fastapi import FastAPI  # We need a Fast, Scalable API

# Generate
app = FastAPI()

# Include all the routes
app.include_router(yt.router)

if __name__ == '__main__':
    uvicorn.run(app, port=4400)
