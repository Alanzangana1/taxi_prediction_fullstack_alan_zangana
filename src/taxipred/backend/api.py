from fastapi import FastAPI
from taxipred.backend.data_processing import TaxiData
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

taxi_data = TaxiData()
model = joblib.load("taxi_price_model.pkl")

@app.get("/")
async def root():
    return {"message": "Taxi Trip Price running"}

@app.get("/taxi/")
async def read_taxi_data():
    return taxi_data.to_json()

class TripInput(BaseModel):
    Trip_Distance_km: float
    Passenger_Count: int
    Base_Fare: float
    Per_Km_Rate: float
    Per_Minute_Rate: float
    Trip_Duration_Minutes: int
    Time_of_Day: str
    Day_of_Week: str
    Traffic_Conditions: str
    Weather: str

@app.post("/predict")
async def predict(trip: TripInput):
    data = pd.DataFrame([trip.dict()])
    price = model.predict(data)[0]
    return {"predicted_price": float(price)}