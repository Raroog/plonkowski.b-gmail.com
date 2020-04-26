#main.py

from hashlib import sha256
from fastapi import FastAPI, Response, Cookie, HTTPException
from fastapi import FastAPI, Request, Response, status
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    correct_username = secrets.compare_digest(credentials.username, "trudnY")
    correct_password = secrets.compare_digest(credentials.password, "PaC13Nt")
	if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return 





@app.post('/login')
def read_current_user(username: str = Depends(get_current_username)):
    return RedirectResponse(url="/welcome", status_code=HTTP_302_FOUND)








