from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from datetime import date
from app.models.special_price import SpecialPrice

async def get_map_for_range(db: AsyncSession, property_id: int, start: date, end: date) -> dict[date, float]:
    q = select(SpecialPrice).where(
        SpecialPrice.property_id == property_id,
        SpecialPrice.date >= start,
        SpecialPrice.date < end,
    )
    res = await db.execute(q)
    rows = res.scalars().all()
    return {r.date: float(r.price) for r in rows}
