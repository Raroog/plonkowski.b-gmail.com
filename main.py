#main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug = 'true')

@app.get("/method/")
async def get_fun():
    return {"get": "GET"}





class Post(BaseModel):
	msg : str
{"msg" : "POST"}

@app.post("/method/")
async def post_fun(post : Post):
	return post




class Put(BaseModel):
	msg : str
{"msg" : "PUT"}

@app.put("/method/")
async def put_fun(put : Put):
	return put




class Delete(BaseModel):
	delete : str
	{"msg" : "DELETE"}

@app.delete("/method/")
async def delete_fun(delete : Delete):
	return delete   

