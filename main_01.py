from fastapi import FastAPI # FastAPI 임포트 

app = FastAPI() # FastAPI 인스턴스 생성 

@app.get("/")
async def root():
    return {"message": "Hello world"}

# 실행 uvicorn main:app --reload 
# 하지만 지금 이 파일의 이름은 main1.py 이기 때문에 main을 main1로 바꿔주어야함 