from services.trip_service import(
    calculate_daily_budget,
    get_recommended_place,
    get_transportation_recommendation,
    get_trip_category
    )

def print_destination(destination):
    print('Your Destination')

    index=0
    while index < len(destination):
        print(f'{index+1}, {destination[index]}')
        index+=1
    
def recommended_place(destination):
    print('Recommended Places')
    print()

    for destination in destination:
        print(destination)

        for place in get_recommended_place(destination):
            print(f' - {place}')

        print()


def print_trip_summary(
    destination,
    days,
    budget,
    travel_style,
    currency,
    travel_month,
    hotel_cost,
    transportation_cost,
    food_cost,
    miscellaneous_cost,
    transportation
    ):

    total_estimate_cost = (
        hotel_cost
        + transportation_cost
        + food_cost
        + miscellaneous_cost
    )

    print('=========================')
    print('kelanaAI')
    print('=========================')

    print(f'Destination         : {destination}')
    print(f'Days                : {days}')
    print(f'Budget              : {budget}')
    print(f'Style               : {travel_style}')
    print(f'Days                : {days}')
    print(f'Budget              : {budget} {currency}')
    print(f'Currency            : {currency}')
    print(f'Travel month        : {travel_month}')
    print(f'Hotel cost          : {hotel_cost}')
    print(f'Transportation cost : {transportation_cost}')
    print(f'Food cost           : {food_cost}')
    print(f'Miscellaneous cost  : {miscellaneous_cost}')
    print(f'Recommended Transportation : {transportation}')
    print_re

    if total_estimate_cost > budget:
            print('Budget exceeded!')

    print()

#  Call it with any trip
print_trip_summary(
['Japan','Korea'],
7,
300.0,
'Backpacker',
'USD',
'July',
100.0,
30.0,
40.0,
10.0
)
