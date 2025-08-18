from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func
from app.models.property import Property
from app.schemas.property import PropertyCreate

async def create_property(db: AsyncSession, prop: PropertyCreate):
    db_obj = Property(**prop.model_dump())
    db.add(db_obj)
    await db.commit()
    await db.refresh(db_obj)
    return db_obj

async def get_properties(db: AsyncSession, location: str = None, amenity: str = None):
    query = select(Property)
    if location:
        query = query.where(Property.location.ilike(f"%{location}%"))
    if amenity:
        query = query.where(func.jsonb_contains(Property.amenities, f'"{amenity}"'))
    result = await db.execute(query)
    return result.scalars().all()
