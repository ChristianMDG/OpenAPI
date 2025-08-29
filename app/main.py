from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

#exo 1 Ping : 

@app.get("/ping", summary="Retourne pong")
async def get_pong():
    return "pong"


class User(BaseModel):
    id: int
    name: str
    email:str
users_db: List = []

#Exercice 2 – Manipuler les paramètres et les réponses: 
@app.get("/users",summary="Récupère la liste des utilisateurs avec pagination")
async def get_users(page:int ):
    return users_db
