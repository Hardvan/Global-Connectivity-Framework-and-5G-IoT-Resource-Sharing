"""
    This file contains the functions to calculate the metrics such as latency, load and
    the quadrant in which the point lies.
    
    Functions included:
        getLowerAndUpper()
        getQuadrant(long, lat, mid_long, mid_lat)
        getLatency(long, lat, mid_long, mid_lat)
        getLoad(lower, upper)
"""


import random
import math


def getLowerAndUpper():
    """Returns the lower and upper limit of the load in mbps.

    Returns:
        lower (int): Lower limit of the load. (mbps)
        upper (int): Upper limit of the load. (mbps)
    """

    lower = random.randint(10, 60)
    upper = random.randint(100, 400)

    return lower, upper


def getQuadrant(long, lat, mid_long, mid_lat):
    """Returns the quadrant in which the point lies.

    Args:
        long (float): Longitude of the point.
        lat (float): Latitude of the point.
        mid_long (float): Longitude of the midpoint.
        mid_lat (float): Latitude of the midpoint.

    Returns:
        quadrant (int): Quadrant in which the point lies.
    """

    # Origin
    X = mid_long
    Y = mid_lat

    # Current Point
    x = long
    y = lat

    quadrant = None
    if x > X and y > Y:
        quadrant = 1
    elif x < X and y > Y:
        quadrant = 2
    elif x < X and y < Y:
        quadrant = 3
    elif x > X and y < Y:
        quadrant = 4

    return quadrant


def getLatency(long, lat, mid_long, mid_lat):
    """Returns the latency between two points in ms.
    Formula: Latency = 2*distance / speed

    Args:
        long (float): Longitude of the first point.
        lat (float): Latitude of the first point.
        mid_long (float): Longitude of the second point.
        mid_lat (float): Latitude of the second point.

    Returns:
        time (float): Latency between the two points in ms.
    """

    long_km = long * 111.32 * math.cos(math.radians(lat))
    lat_km = lat * 110.574

    mid_long_km = mid_long * 111.32 * math.cos(math.radians(mid_lat))
    mid_lat_km = mid_lat * 110.574

    distance = math.sqrt((long_km - mid_long_km)**2 +
                         (lat_km - mid_lat_km)**2)     # in km

    speed = 3e5  # in km/s

    time = (2 * distance / speed) * 1000  # in ms

    return time


def getLoad(lower, upper):
    """Returns the load between two points in mbps.

    Args:
        lower (int): Lower limit of the load. (mbps)
        upper (int): Upper limit of the load. (mbps)

    Returns:
        load (int): Load between the two points in mbps.
    """

    return random.randint(lower, upper)
