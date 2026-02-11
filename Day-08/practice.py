from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


user = User(id=1, name="fsdf")

app = FastAPI()


@app.get("/")
def homePage():
    print(user)
    return {"message": "hello from the homepage"}


@app.get("/user")
def userPage():
    return {"user": user}
