from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, exists
from datetime import timedelta
from app.models.booking import Booking
from app.models.blocked_date import BlockDate