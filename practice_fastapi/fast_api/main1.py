from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Login(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: Login):
    if data.username == "admin" and data.password == "1234":
        return {"message": "Login Succesful"}
    return{"message": "Invalid data or password"}