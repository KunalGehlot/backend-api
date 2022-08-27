import uvicorn
from routes import yt
from fastapi import FastAPI

# Generate
app = FastAPI()

# Include all the routes
app.include_router(yt.router)

if __name__ == '__main__':
    uvicorn.run(app, port=4400)
