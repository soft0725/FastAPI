# 사전정의 값 
# 경로 매개변수 값을 원하면 파이썬 표준 Enum을 사용할 수 있음 

from enum import Enum 

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/model/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet: # ModelName.alexnet 처럼 클래스 안에 값으로 확인 가능
        return {"model_name": model_name, "message": "alexnet hello!"}
    
    if model_name.value == "resnet": # model_name.value으로 비교 가능
        return {"model_name": model_name, "message": "resnet hello!"}
    
    else:
        return {"model_name": model_name, "message": "lenet hello!"}