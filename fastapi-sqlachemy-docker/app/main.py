import os
import uvicorn
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi_sqlalchemy import DBSessionMiddleware, db

from app.models import User as UserModel
from app.schema import UserBase, UserResponse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, '.env'))

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.getenv('DATABASE_URL'))

@app.post('/users', response_model=UserResponse)
def create_user(user: UserBase):
    db_user = UserModel(username=user.username, fullname=user.fullname)
    db.session.add(db_user)
    db.session.commit()
    return db_user

@app.get('/')
def index():
    return {'message': 'Hello World'}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)