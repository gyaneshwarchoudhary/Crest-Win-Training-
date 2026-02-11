from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def homePage():
    return {"message": "hii from the homepage"}


def main():
    print("Hello from day-09!")
    uvicorn.run(
        "main:app",
        port=8000,
        host="0.0.0.0",
        reload=True,
    )


if __name__ == "__main__":
    main()
