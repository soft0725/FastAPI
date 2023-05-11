# 모든 데이터는 pydantic에 의해 내부적으로 수행됨

from fastapi import FastAPI

app = FastAPI()

@app.get("/Users/me")
async def read_user_me():
    return {"Usert_id": "the current user"}

@app.get("/Users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}