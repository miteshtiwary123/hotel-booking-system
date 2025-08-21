from sqlalchemy import Column, Integer, Date, ForeignKey, Numeric
from app.models.base import Base

class SpecialPrice(Base):
    __tablename__ = "special_price"

    id = Column(Integer, primary_key=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"), index=True)
    date = Column(Date, nullable=False, index=True)
    price = Column(Numeric(10,2), nullable=False)
