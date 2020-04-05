#main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug = 'true')

@app.get("/method")
async def get_fun():
    return {"get": "GET"}





class Post(BaseModel):
	name : str = "POST"


@app.post("/method")
async def post_fun(post : Post):
	return post




class Put(BaseModel):
	name : str = "PUT"



@app.put("/method")
async def put_fun(put : Put):
	return put




class Delete(BaseModel):
	name : str = "DELETE"


@app.delete("/method")
async def delete_fun(delete : Delete):
	return delete   

