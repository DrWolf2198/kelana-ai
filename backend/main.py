from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.trip_service import (calculate_daily_budget, get_trip_category, get_transportation_recommendation, get_recommended_place)
from models.trip import Trip
from database import SessionLocal, init_db

class TripRequest(BaseModel):
    destination:    str
    days:           int
    budget:         float
    travel_style:   str

class UpdateBudgetRequest(BaseModel):
    budget: float

app = FastAPI()

# create tables on startup
init_db()

# GET /
@app.get('/')
def home():
    return {
        'message': 'Welcome to Kelana AI'
    }

# GET /health
@app.get('/health')
def health():
    return {
        'status': 'OK'
    }

# GET /trip-categories
@app.get('/trip-categories')
def trip_category():
    return ['Backpacker', 'Standard', 'Luxury']

# GET /api/v1/recommendations
@app.get('/api/v1/recommendations')
def recommendations():
    return ['Tokyo Tower', 'Mount Fuji', 'Shibuya']

# GET /api/v1/transportations
@app.get('/api/v1/transportations')
def transportations():
    return ['Bus', 'Train', 'Flight']

# POST /api/v1/trips
@app.post('/api/v1/trips')
def create_trip(request: TripRequest):
    daily_budget = calculate_daily_budget(request.budget, request.days)
    category     = get_trip_category(request.budget)
    recommendation_transport = get_transportation_recommendation(category)
    recommendation_place     = get_recommended_place(request.destination)

    trip = Trip(
        destination  = request.destination,
        days         = request.days,
        budget       = request.budget,
        category     = category,
        daily_budget = daily_budget,
    )

    db = SessionLocal()
    db.add(trip)
    db.commit()
    db.refresh(trip)
    db.close()
    return trip

# GET /api/v1/trips/{trip_id}
@app.get('/api/v1/trips/{trip_id}')
def get_trip(trip_id: int):
    db   = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()
    db.close()

    if trip is None:
        raise HTTPException(status_code=404, detail=f'Trip with id {trip_id} not found')
    return trip

# PUT /api/v1/trips/{trip_id}
@app.put('/api/v1/trips/{trip_id}')
def update_trip(trip_id: int, request: UpdateBudgetRequest):
    db   = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f'Trip with id {trip_id} not found')

    # recalculate based on new budget
    trip.budget       = request.budget
    trip.category     = get_trip_category(request.budget)
    trip.daily_budget = calculate_daily_budget(request.budget, trip.days)

    db.commit()
    db.refresh(trip)
    db.close()
    return trip

# DELETE /api/v1/trips/{trip_id}
@app.delete('/api/v1/trips/{trip_id}')
def delete_trip(trip_id: int):
    db   = SessionLocal()
    trip = db.query(Trip).filter(Trip.id == trip_id).first()

    if trip is None:
        db.close()
        raise HTTPException(status_code=404, detail=f'Trip with id {trip_id} not found')

    db.delete(trip)
    db.commit()
    db.close()
    return {'message': f'Trip with id {trip_id} deleted successfully'}
