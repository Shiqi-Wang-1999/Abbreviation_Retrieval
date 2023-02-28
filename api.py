from fastapi.middleware.cors import CORSMiddleware
from json_object import SuccessJsonObject, ErrorJsonObject
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile, Form
import traceback
import datetime
from typing import List
import os
from main import main_match

import uvicorn
from pydantic import BaseModel, Field
from log import Logger

log = Logger().logger

app = FastAPI(title="基于向量空间模型的短文本匹配API",
              description="基于向量空间模型的短文本匹配API",
              version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class InputParameter(BaseModel):
    segment_type: str = Field('char', title="分词器类型(char/jieba/hanlp),3选1")
    isbert: bool = Field(False, title="是否使用bert作为词向量,若使用分词器必须使用char类型")
    isrmstopwords: bool = Field(True, title="是否去停用词")
    text: str = Field(None, title="待匹配文本")
    


@app.get('/', name='index', description='index')
async def index():
    return {'欢迎使用基于向量空间模型的短文本匹配系统！'}


@app.post('/matcher', name='匹配接口', description='输入参数，返回匹配结果')
async def ner_predict_service(match_para: InputParameter):
    try:
        start = datetime.datetime.now()
        out = main_match(text=match_para.text,segment_type=match_para.segment_type,
        isbert=match_para.isbert,isrmstopwords=match_para.isrmstopwords)
        end = datetime.datetime.now()
        log.info("time:" + str((end - start).total_seconds()) + 's')
        return JSONResponse(SuccessJsonObject(out).info())
    except Exception as e:
        traceback.print_exc()
        message = traceback.format_exc()
        log.error(message)
    return JSONResponse(ErrorJsonObject(message=message, data=None).info())


if __name__ == '__main__':
    uvicorn.run("api:app", port=5555, reload=True, access_log=False)
