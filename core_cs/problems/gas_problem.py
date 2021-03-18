# if I have two gas stations 5 miles apart, if I knew the prices,
# should I go to the one 5miles away or stay with this one.
DISTANCE_TO_STATION = 5


def should_i_go(mpg: int, cost_at_a: float, cost_at_b: float, left_in_tank: float) -> bool:
    # calculate how many gallons the car will use and multiply by two

    # cost to fill the tank here
    full_tank_a = left_in_tank * cost_at_a

    # gallons used to get there
    gallons_used = mpg / (DISTANCE_TO_STATION * 2)

    # cost to fill the tank there
    full_tank_b = (left_in_tank - gallons_used) * cost_at_b

    if cost_at_a < (left_in_tank - mpg * cost_at_b/(2 * DISTANCE_TO_STATION)) / left_in_tank:
        return True
    else:
        return False

    # how much is it gonna cost to go to b?
    # if full_tank_a < full_tank_b:
    #     return True
    # else:
    #     return False

# left_in_tank * cost_at_a < left_in_tank - mpg * cost_at_b/(2 * DISTANCE_TO_STATION) * cost_at_b
