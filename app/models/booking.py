from sqlalchemy import Column, Integer, Date, ForeignKey
from app.models.base import Base

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    