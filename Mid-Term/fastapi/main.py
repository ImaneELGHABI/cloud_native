
from fastapi import FastAPI
import pickle
from pydantic import BaseModel
import numpy as np
from sklearn import *



with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

app = FastAPI()

class PredictRequest(BaseModel):
    bedrooms : int
    bathrooms : float
    sqft_living:int
    sqft_lot: int
    floors:float
    waterfront: int
    view: int
    condition:  int
    grade: int
    sqft_above: int
    sqft_basement :int
    yr_built:int
    yr_renovated : int
    zipcode: int
    lat:float
    long:float
    sqft_living15 : int
    sqft_lot15: int



@app.post('/predict')
def predict(request: PredictRequest):
    features = np.array([request.bedrooms, request.bathrooms, request.sqft_living, request.sqft_lot, request.floors, 
                        request.waterfront, request.view, request.condition, request.grade, request.sqft_above,
                        request.sqft_basement, request.yr_built, request.yr_renovated, request.zipcode,
                        request.lat, request.long, request.sqft_living15, request.sqft_lot15]).reshape(1,-1)
    prediction = model.predict(features)
    return {"prediction": prediction[0]}
