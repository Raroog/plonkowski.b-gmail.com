#main.py


from fastapi import FastAPI, Request, Response, status





@app.get("/welcome")
def read_root():
    return {"message": "Welcome universe, this is planet Earth"}


@app.get("/")
def read_root():
    return {"message": "Hello men and women"}




