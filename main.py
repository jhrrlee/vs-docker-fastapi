from fastapi import FastAPI
from os import environ as env

app = FastAPI()

@app.get('/')
    
def index():
    return f"hello wwww environment = {env['MY_VARIABLE']}"
