import numpy as np

limit = 100000
origo = 250000

def get_violating_drones(data):
    drones = data['report']['capture']['drone']
    violating = []
    for drone in drones:
        if check_distance(get_distance(drone)):
            violating.append(drone)
    return violating

def check_distance(distance):
    return distance < limit

def get_distance(drone):
    a = (origo - float(drone['positionY']))**2
    b = (origo - float(drone['positionX']))**2
    c = np.sqrt(a + b)

    return c
