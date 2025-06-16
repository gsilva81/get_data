from sqlalchemy import Column, Integer, String, Float
from db import Base

class WeatherData(Base):
    __tablename__ = "weather_data"

    id = Column(Integer, primary_key=True, index=True)
    city = Column(String, index=True)
    country = Column(String)
    temperature = Column(Float)
    feels_like = Column(Float)
    humidity = Column(Integer)
    description = Column(String)
