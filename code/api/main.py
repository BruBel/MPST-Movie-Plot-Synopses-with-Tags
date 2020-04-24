from fastapi import FastAPI
from pydantic import BaseModel
from classifier import Classifier

app = FastAPI()


class New(BaseModel):
    synopsis: str


class ResponseModel(BaseModel):
    categories: list


@app.get('/')
def root():

    return {"message": "Hello World!"}


@app.post('/predict')
async def predict_category(new: New):

    response = Classifier().predict(new.synopsis)

    response_model = ResponseModel(
        categories=response['categories'])

    return response_model
