from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.db import get_db
from app.schemas.property import PropertyCreate, PropertyOut
from app.crud import property as crud_property

router = APIRouter(prefix="/properties", tags=["properties"])

@router.post("/", response_model=PropertyOut)
async def create_property(property_in: PropertyCreate, db: AsyncSession = Depends(get_db)):
    return await crud_property.create_property(db, property_in)

@router.get("/", response_model=PropertyOut)
async def list_properties(location: str = None, amenity: str = None, db: AsyncSession = Depends(get_db)):
    return await crud_property.get_properties(db, location, amenity)