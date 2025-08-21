from sqlalchemy import Column, Integer, Date, ForeignKey, Numeric
from app.models.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    total_price = Column(Numeric(10,2), nullable=False, default=0)
