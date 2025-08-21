from sqlalchemy import Column, Integer, String, Float, JSON, Numeric
from app.models.base import Base

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    location = Column(String, index=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenities = Column(JSON, default=list)

    base_price = Column(Numeric(10, 2), nullable=False, default=100.00)
    weekend_multiplier = Column(Float, nullable=False, default=1.2)
