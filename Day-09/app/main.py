from fastapi import FastAPI
import uvicorn
from api.routes import user


app = FastAPI(docs_url=None, redoc_url=None)

app.include_router(user.router, prefix="/users", tags=["Users"])


def main():
    print("Hello from day-09!")


# if __name__ == "__main__":
#     main()
