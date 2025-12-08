from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np


app = FastAPI(title="House Price Prediction API Using app.route")


# load train model
with open("model.pkl","rb")as f:
    model = pickle.load(f)

class HouseData(BaseModel):
    area: float
    bedrooms: int
    age: int


@app.api_route("/predict", methods=["POST"])
def predict_price(data: HouseData):
    features = np.array([[data.area, data.bedrooms, data.age]])
    prediction = model.predict(features)[0]
    return {"Predicted_Price(in lakhs)": round(prediction, 2)}



