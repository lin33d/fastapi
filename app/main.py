from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel
from app.bookings.router import router as router_bookings


app = FastAPI()
app.include_router(router_bookings)

class SHotel(BaseModel):
    adress: str
    name: str
    stars: int


class HotelSearchArgs():
    def __init__(
        self,
        location: str,
        date_from: date,
        date_to: date,
        stars: Optional[int] = Query(None, ge=1, le=5),
        has_spa: Optional[bool] = None,
                 
    ):
        self.location = location
        self.date_from = date_from 
        self.date_to = date_to 
        self.stars = stars 
        self.has_spa = has_spa 


@app.get("/hotels", response_model=list[SHotel])
def get_hotels(
    search_args: HotelSearchArgs = Depends()              
    ):

    return search_args


class SBooking(BaseModel):
    room_id: int
    date_from: date 
    date_to: date

@app.post("/bookings")
def add_booking(booking: SBooking):
    pass