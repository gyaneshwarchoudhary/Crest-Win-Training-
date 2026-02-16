import time
from fastapi import FastAPI, Depends, HTTPException, status, BackgroundTasks, Request
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, Field
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# --- CONFIGURATION & DATABASE ---
SECRET_KEY = "super-secret-key"
ALGORITHM = "HS256"
Base = declarative_base()
engine = create_engine("sqlite:///./test.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
pwd_context = CryptContext(
    schemes=["sha256_crypt"], deprecated="auto", bcrypt__truncate_error=True
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# --- SQLALCHEMY MODEL ---
class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    hashed_password = Column(String)
    role = Column(String, default="user")


Base.metadata.create_all(bind=engine)


# --- PYDANTIC MODELS (Input Validation) ---
class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=3)
    role: str = "user"  # Default value


class Token(BaseModel):
    access_token: str
    token_type: str


app = FastAPI()


# --- MIDDLEWARE ---
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start_time)
    return response


# --- DEPENDENCIES ---
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        user = db.query(UserDB).filter(UserDB.username == username).first()
        if not user:
            raise HTTPException(status_code=401)
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def check_admin(user: UserDB = Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403, detail="Forbidden: Admins only")
    return user


# --- ROUTES ---
@app.post("/register")
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # Pydantic validates the input 'user_in' automatically
    try:
        hashed = pwd_context.hash(user_in.password)
        if not hashed:
            raise Exception("password is not hasing ")
        print(
            f"hashed--------------------------------{user_in.password}-------------------------------------------d{hashed}"
        )
        new_user = UserDB(
            username=user_in.username, hashed_password=hashed, role=user_in.role
        )
        if not new_user:
            raise HTTPException(
                status_code=301, details="somethign went wrong while crating user"
            )
        db.add(new_user)
        db.commit()
        return {"msg": f"User {user_in.username} registered successfully"}
    except HTTPException as e:
        print("---------------this is the following error ", e)


@app.post("/token", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = db.query(UserDB).filter(UserDB.username == form_data.username).first()
    if not user or not pwd_context.verify(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = jwt.encode({"sub": user.username}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}


@app.get("/admin-only")
def admin_route(admin: UserDB = Depends(check_admin)):
    return {"data": "Secret admin stuff"}


@app.post("/task")
def run_bg_task(bt: BackgroundTasks, user: UserDB = Depends(get_current_user)):
    bt.add_task(lambda: print(f"Processing for {user.username}..."))
    return {"msg": "Background task scheduled"}
