from typing import List

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from services.service import process_files, process_file

app = FastAPI()
# CORS 설정 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 허용할 도메인 (프론트엔드 URL)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용 (GET, POST, PUT, DELETE 등)
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/api/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    try:
        # 서비스 함수 호출하여 파일 처리
        data = await process_file(file)
        return {"filename": file.filename, "data": data}
    except HTTPException as e:
        # 발생한 HTTPException을 그대로 반환
        raise e
    except Exception as e:
        # 그 외 예외 처리
        raise HTTPException(status_code=500, detail=f"처리 중 오류 발생: {str(e)}")


@app.post("/api/uploadfiles")
async def upload_files(files: List[UploadFile] = File(...)):
    try:
        # 서비스 함수 호출하여 파일 처리
        file_data = await process_files(files)
    except ValueError as e:
        return {"error": str(e)}

    # 처리된 파일 데이터를 반환
    return {"files": list(file_data.keys()), "data": file_data}
