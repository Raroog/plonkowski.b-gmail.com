#main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug = 'true')

@app.get("/method")
async def get_fun():
    return {"get": "GET"}


@app.post("/method")
async def post_fun():
	return{"post" : "POST"}


@app.put("/method")
async def put_fun():
	return {"put": "PUT"}


@app.delete("/method")
async def delete_fun():
	return{"delete" : "DELETE"}   