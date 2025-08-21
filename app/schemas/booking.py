from pydantic import BaseModel, Field
from datetime import date

class BookingCreate(BaseModel):
    property_id: int
    start_date: date
    end_date: date

class BookingOut(BaseModel):
    id: int
    property_id: int
    start_date: date
    end_date: date
    total_price: float

    class Config:
        from_attributes = True

class QuoteOut(BaseModel):
    property_id: int
    start_date: date
    end_date: date
    nights: int
    breakdown: list[dict]
    total: float
    currency: str = "INR"