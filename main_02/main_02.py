from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}

# http://127.0.0.1:8000/items/foo로 이동을 하면 {"item_id": "foo"} 가 나올것이다
# 하지만 입력받는 매개변수의 타입을 바꾸면 에러가 날 것이다.

@app.get("/itemlist/{item_id}")
async def read_item(item_id: int): # 매개변수의 타입을 int로 받음
    return {"item_id": item_id} # 그럼 여기서 item_id가 foo이면 에러가 남 

# http://127.0.0.1:8000/itemlist/1 뒤에 매개변수의 타입이 int형이면 에러가 나지 않지만
# http://127.0.0.1:8000/itemlist/foo 이런식이면 매개변수의 타입이 str이기 때문에 에러가남 