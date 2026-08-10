def print_trip_summary(
    destination,
    days,
    budget,
    currency,
    travel_month,
    hotel_cost,
    transportation_cost,
    food_cost,
    miscellaneous_cost
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
    print(f'Budget              : {budget} {currency}')
    print(f'Currency            : {currency}')
    print(f'Travel month        : {travel_month}')
    print(f'Hotel cost          : {hotel_cost}')
    print(f'Transportation cost : {transportation_cost}')
    print(f'Food cost           : {food_cost}')
    print(f'Miscellaneous cost  : {miscellaneous_cost}')

    if total_estimate_cost > budget:
        print('Budget exceeded!')

    print()

    #Call it with any trip
print_trip_summary(
    'Fuji',
    7,
    200000.0,
    'Yen',
    'July',
    70000.0,
    30000.0,
    40000.0,
    10000.0
     )
