from sqlalchemy import Column, Integer, Date, ForeignKey
from app.models.base import Base

class BlockDate(Base):
    __tablename__ = "blocked_dates"

    id = Column(Integer, primary_key=True, index=True)
    property_id = Column(Integer, ForeignKey("properties.id", ondelete="CASCADE"))
    date = Column(Date, nullable=False)
    