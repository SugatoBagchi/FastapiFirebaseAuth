from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException
from fastapi.requests import Request
import uvicorn
import pyrebase

import firebase_admin

from firebaseConfig import firebaseConfig
from firebase_admin import credentials, auth

from models import LoginSchema, SignUpSchema


app = FastAPI(
    description="This is a simple app built with FastAPI to show Firebase Authentication",
    title="Firebase Authentication with FastAPI",
    docs_url="/",
)

if not firebase_admin._apps:
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)


firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()  

@app.post('/signup')
async def create_an_account(user_data: SignUpSchema):
    email = user_data.email
    password = user_data.password 
    try:
        user = auth.create_user_with_email_and_password(email, password)
        # return JSONResponse(status_code=200, content={"message": f"{user} user created successfully"})
        return JSONResponse(status_code=200, content={"message": f"{user.uid} user created successfully"})
    except Exception as e:
        # raise HTTPException(status_code=400, detail= f"{user} ")
        return JSONResponse(status_code=400, content={"message": f"{e}"})

@app.post('/login')
async def create_access_token(user_data: LoginSchema):
    email = user_data.email
    password = user_data.password 

    try:
        user = auth.sign_in_with_email_and_password(email, password)

        token = user['idToken']
        return JSONResponse(status_code=200, content={"message": "User logged in successfully", "token": f"{token}"})
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": f"{e}"})
    

@app.post('/ping')
async def validate_token(request: Request):
    headers = request.headers
    jwt = headers.get('Authorization')
    user = auth.verify_id_token(jwt)

    return user
    

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)