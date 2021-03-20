# -*- coding: utf-8 -*-
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from api_router import APIs

app = FastAPI()
apis = APIs()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=200)
async def root():
    return "app is running"

@app.get("/weather", status_code=200)
async def weather(location: str):
    response = apis.get_weather(location)
    return JSONResponse(response)


if __name__ == "__main__":
    uvicorn.run("application:app", host="0.0.0.0", port=80, reload=True)
