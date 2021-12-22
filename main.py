import os

from fastapi import FastAPI
from mangum import Mangum

stage = os.environ.get('STAGE', None)
root_path = f"/{stage}" if stage else "/"

app = FastAPI(title="Serverless Python Starter", root_path=root_path) 

@app.get("/")
def index():
    return "Index"
    
@app.get("/hello")
def hello():
    return {"message": "Hello World"}

handler = Mangum(app)