from fastapi import FastAPI

app = FastAPI()

#exo 1 Ping

@app.get("/ping", summary="Retourne pong")
async def get_pong():
    return "pong"

