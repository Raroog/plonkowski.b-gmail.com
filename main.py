#main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(debug = 'true')

@app.get("/get/")
async def get_fun():
    return {"get": "GET"}





class Post(BaseModel):
	msg : str


a = {"msg" : "POST"}

@app.post("/a/")
async def post_fun(post : Post):
	return post




class Put(BaseModel):
	msg : str


b = {"msg" : "PUT"}

@app.put("/b/")
async def put_fun(put : Put):
	return put




class Delete(BaseModel):
	delete : str

c = {"msg" : "DELETE"}

@app.delete("/c/")
async def delete_fun(delete : Delete):
	return delete   

