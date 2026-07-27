from typing import Optional

from pydantic import BaseModel


class CropInput(BaseModel):
    Crop: str
    Year: int
    State: str
    Area: float
    Production: float
    Rainfall: Optional[float] = None
    Temperature: Optional[float] = None
    Humidity: Optional[float] = None
    N: float
    P: float
    K: float
    pH: float
    Season: Optional[str] = None
    Annual_Rainfall: Optional[float] = None
    Fertilizer: Optional[float] = None
    Pesticide: Optional[float] = None
    avg_temp_c: Optional[float] = None
    total_rainfall_mm: Optional[float] = None
    avg_humidity_percent: Optional[float] = None




