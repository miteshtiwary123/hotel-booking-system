from pydantic import BaseModel, Field
from typing import List, Optional

class PropertyBase(BaseModel):
    title: str
    description: Optional[str]
    location: str
    latitude: float
    longitude: float
    amenities: List[str] = []
    base_price: float =Field(ge=0)
    weekend_multiplier: float = Field(default=1.2, ge=0)

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(PropertyBase):
    pass

class PropertyOut(PropertyBase):
    id: int

    class Config:
        from_attributes = True