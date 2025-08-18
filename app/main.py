from fastapi import FastAPI
from app.api.v1 import property

app = FastAPI(title="Hotel Booking System")

app.include_router(property.router)
