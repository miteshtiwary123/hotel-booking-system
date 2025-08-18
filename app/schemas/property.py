from pydantic import BaseModel
from typing import List, Optional

class PropertyBase(BaseModel):
    title: str
    description: Optional[str]
    location: str
    latitude: float
    longitude: float
    amenities: List[str] = []

class PropertyCreate(PropertyBase):
    pass

class PropertyUpdate(PropertyBase):
    pass

class PropertyOut(PropertyBase):
    id: int

    class Config:
        from_attributes = True