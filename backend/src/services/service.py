import json

import pandas as pd
from io import BytesIO
from fastapi import UploadFile, File, HTTPException
from typing import List, Dict


async def process_file(file: UploadFile = File(...)):
    try:
        # 파일 확장자 확인
        extension = file.filename.split('.')[-1].lower()

        # 파일 내용을 읽어와서 판다스로 변환
        if extension == 'csv':
            contents = await file.read()
            df = pd.read_csv(BytesIO(contents))
            df = df.reset_index(drop=True)
        elif extension in ['xls', 'xlsx']:
            contents = await file.read()
            df = pd.read_excel(BytesIO(contents))
            df = df.reset_index(drop=True)
        else:
            raise HTTPException(status_code=400, detail="지원되지 않는 파일 형식입니다.")

        # 데이터프레임을 딕셔너리로 변환해서 반환
        return json.loads(df.to_json(orient='table', index=False))
        # return df.to_dict(orient="records")

    except pd.errors.EmptyDataError:
        raise HTTPException(status_code=400, detail="파일이 비어있습니다.")
    except pd.errors.ParserError:
        raise HTTPException(status_code=400, detail="파일을 파싱하는 중에 오류가 발생했습니다.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"파일 처리 중 오류가 발생했습니다: {str(e)}")


async def process_files(files: List[UploadFile]) -> Dict[str, dict]:
    file_data = {}
    for file in files:
        # 파일 확장자 확인
        extension = file.filename.split('.')[-1].lower()

        # 파일 내용을 읽어와서 판다스로 변환
        if extension == 'csv':
            # CSV 파일 처리
            contents = await file.read()
            df = pd.read_csv(BytesIO(contents))
            df = df.reset_index(drop=True)
            file_data[file.filename] = json.loads(df.to_json(orient='table', index=False))
            # file_data[file.filename] = df.to_dict(orient="records")
        elif extension in ['xls', 'xlsx']:
            # Excel 파일 처리
            contents = await file.read()
            df = pd.read_excel(BytesIO(contents))
            df = df.reset_index(drop=True)
            file_data[file.filename] = json.loads(df.to_json(orient='table', index=False))
            # file_data[file.filename] = df.to_dict(orient="records")
        else:
            raise ValueError(f"{file.filename}은(는) 지원되지 않는 파일 형식입니다.")

    return file_data
