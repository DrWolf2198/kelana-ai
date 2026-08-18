from fastapi import FastAPI
from pydantic import BaseModel
from services.trip_service import(calculate_daily_budget, get_trip_category, get_transportation_recommendation, get_recommended_place)

class TripRequest(BaseModel):
    destination:    str
    days:           int
    budget:         float
    travel_style:   str

app = FastAPI()

#  GET endpoint at the root path
@app.get('/')
def home():
    return{
        'message' : 'Welcome to Kelana AI'
    }

# GET health
@app.get('/health')
def health():
    return{
        'status' : 'OK'
    }

@app.get('/trip-categories')
def trip_category():
    return ['Backpacker', 'Standard', 'Luxury']

# TUGAS 3
# @app.get('/api/v1/recommendations')
# def recommendations():
#     return ['Tokyo Tower', 'Mount Fuji', 'Shibuya']

# @app.get('/api/v1/transportations')
# def transportations():
#     return ['Bus', 'Train', 'Flight']

@app.get('/api/v1/transportastion')
def transportation():
    return 

# POST endpoint - receives JSON, return JSON
@app.post('/api/v1/trips')
def create_trip(request: TripRequest):
    daily_budget = calculate_daily_budget(
        request.budget, request.days
    )
    category = get_trip_category(
        request.budget
    )
    recommendation_transport = get_transportation_recommendation(category)
    recommendation_place = get_recommended_place(request.destination)
    return{
        'destination' : request.destination,
        'days': request.days,
        'budget' : request.budget,
        'daily_budget' : daily_budget,
        'category' : category,
        'recommendation_transport' : recommendation_transport,
        'recommendation_place' : recommendation_place
    }
