from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal, engine, Base
from models import WeatherData
from weather_service import fetch_weather_data

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/weather/{city}")
def save_weather(city: str, db: Session = Depends(get_db)):
    weather = fetch_weather_data(city)
    if weather:
        weather_obj = WeatherData(**weather)
        db.add(weather_obj)
        db.commit()
        db.refresh(weather_obj)
        return weather_obj
    else:
        raise HTTPException(status_code=404, detail="City not found in OpenWeather API")

@app.get("/weather/{city}")
def get_weather(city: str, db: Session = Depends(get_db)):
    result = db.query(WeatherData).filter(WeatherData.city == city).all()
    return result
