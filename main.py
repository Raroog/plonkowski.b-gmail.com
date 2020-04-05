#main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug = 'true')


#class Prowadzacyssiepaue(BaseModel):
#	msg :str

@app.get("/get")
async def get_fun():
    return {"get": "GET"}

@app.post("/post")
async def post_fun():
	return{"post" : "POST"}


@app.put("/put")
async def put_fun():
	return {"put": "PUT"}


@app.delete("/delete")
async def delete_fun():
	return{"delete" : "DELETE"}   

