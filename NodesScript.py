""" 
1) Find Latency (Delay) for each Node. Latency = 2 * distance / speed.
2) Plot Graph in ascending order.
3) Clustering: Based on four Quadrants. Assume Midpoint as Origin.
"""


import random
import matplotlib.pyplot as plt
import math
import numpy as np
import os

# Custom Modules
import Regions


# GLOBAL VARIABLES
GRAPH_NO = 1  # For naming the Graphs


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


def plotGraph(x, y, x_name, y_name, color, title, region_name):

    # x-coordinates of left sides of bars
    left = list(range(1, len(x)+1))

    # Heights of bars: y

    # Labels for bars: x_name

    # Plotting a Bar Chart
    plt.bar(left, y, tick_label=x,
            width=0.8, color=[color])

    plt.xlabel(x_name)  # Naming the x-axis
    plt.ylabel(y_name)  # Naming the y-axis
    plt.title(title)  # Plot Title

    # Save the Plot in Graphs/region_name folder
    title = title.replace(" ", "_")
    title = title.replace("/", "_")
    region_name = region_name.replace(" ", "_")
    global GRAPH_NO
    if not os.path.exists(f"Graphs/{region_name}"):
        os.makedirs(f"Graphs/{region_name}")
    plt.savefig(f"Graphs/{region_name}/{GRAPH_NO}_{title}.png")
    GRAPH_NO += 1

    plt.show()  # Display the plot


def doRegion(nodes, midpoint, region_name):

    # Getting Latency for each Node
    for name in nodes:

        longitude = nodes[name]["Longitude"]
        latitude = nodes[name]["Latitude"]
        mid_longitude = midpoint["Longitude"]
        mid_latitude = midpoint["Latitude"]

        nodes[name]["Latency"] = getLatency(
            longitude, latitude, mid_longitude, mid_latitude)

    """ Plotting Latency Graph in Normal Order """

    # Extracting all names and latencies in two lists
    node_id_list = [nodes[name]["Node ID"] for name in nodes]
    latency_list = [nodes[name]["Latency"] for name in nodes]

    plotGraph(x=node_id_list, y=latency_list,
              x_name="Node ID", y_name="Latency (ms)",
              color="blue", title=f"Latency v/s Node ID Bar Chart for {region_name} Region",
              region_name=region_name)

    """ Plotting Latency Graph in Ascending Order """

    # Performing selection sort to exchange node ids and latencies
    n = len(latency_list)
    for i in range(n):
        for j in range(i + 1, n):
            if latency_list[i] > latency_list[j]:

                # Swapping Latencies & Node IDs
                latency_list[i], latency_list[j] = \
                    latency_list[j], latency_list[i]
                node_id_list[i], node_id_list[j] = \
                    node_id_list[j], node_id_list[i]

    plotGraph(x=node_id_list, y=latency_list,
              x_name="Node ID", y_name="Latency (ms)",
              color="blue", title=f"Ascending Latency v/s Node ID Bar Chart for {region_name} Region",
              region_name=region_name)

    """ Dividing into Clusters """

    # Stored as {1:{"Pune":{"Country":"India"}}}
    cluster_dictionary = {1: {},  # Quadrant 1
                          2: {},  # Quadrant 2
                          3: {},  # Quadrant 3
                          4: {},  # Quadrant 4
                          }

    for name in nodes:

        longitude = nodes[name]["Longitude"]
        latitude = nodes[name]["Latitude"]

        mid_longitude = midpoint["Longitude"]
        mid_latitude = midpoint["Latitude"]

        quadrant = getQuadrant(longitude, latitude,
                               mid_longitude, mid_latitude)

        cluster_dictionary[quadrant][name] = nodes[name]

    # Plotting the Bar Chart for each Cluster
    for quadrant_no in cluster_dictionary:

        # For Quadrant 1,2,3,4 respectively
        color_list = ["red", "green", "blue", "yellow"]

        # Extracting nodes in the quadrant
        quadrant_nodes = cluster_dictionary[quadrant_no]

        quadrant_name = f"Quadrant {quadrant_no}"

        # Extracting all node ids and latencies in two lists
        node_id_list = [quadrant_nodes[name]["Node ID"]
                        for name in quadrant_nodes]
        latency_list = [quadrant_nodes[name]["Latency"]
                        for name in quadrant_nodes]

        plotGraph(x=node_id_list, y=latency_list,
                  x_name="Node ID", y_name="Latency (ms)",
                  color=color_list[quadrant_no -
                                   1], title="Latency v/s "+quadrant_name+" Chart",
                  region_name=region_name)

    """ Plotting Latency Ratio Graph """

    node_id_list = [nodes[name]["Node ID"] for name in nodes]
    latency_list = [nodes[name]["Latency"] for name in nodes]

    # Normalizing Latency (0 to 1)
    max_latency = max(latency_list)
    latency_ratio_list = list(map(lambda x: x/max_latency, latency_list))

    plotGraph(x=node_id_list, y=latency_ratio_list,
              x_name="Node ID", y_name="Latency Ratio",
              color="Purple", title=f"Latency Ratio v/s Node ID for {region_name} Region",
              region_name=region_name)

    """ Distributing Latency """

    threshold = 0.75

    for i in range(len(latency_ratio_list)):

        ratio = latency_ratio_list[i]

        if ratio >= threshold:  # Ratio exceeds threshold value, then exchange

            difference = ratio - threshold

            # Find the least ratio and its index
            least_ratio = min(latency_ratio_list)
            least_ratio_index = latency_ratio_list.index(least_ratio)

            if least_ratio + difference <= 0.75:    # Distributing Load only if Lower Bar after addition is < threshold
                ratio -= difference
                least_ratio += difference
            else:
                raise Exception("Cannot Distribute Load in this Region")

            # Updating
            latency_ratio_list[i] = ratio
            latency_ratio_list[least_ratio_index] = least_ratio

    """ Plotting the Normalized Latency Ratio Graph """

    plotGraph(x=node_id_list, y=latency_ratio_list,
              x_name="Node ID", y_name="Latency Ratio",
              color="Green", title=f"Normalised Latency Ratio v/s Node ID Bar Chart for {region_name} Region",
              region_name=region_name)

    print("Max Value of Normalized Latency is:", max(latency_ratio_list))

    return node_id_list, latency_ratio_list


def doLoad(nodes, midpoint, region_name):

    # Getting Lower and Upper limit for Load
    for name in nodes:

        lower, upper = getLowerAndUpper()
        nodes[name]["Lower Limit"] = lower
        nodes[name]["Upper Limit"] = upper

    node_id_list = [nodes[name]["Node ID"] for name in nodes]

    """ Plotting Load Graph """

    load_list = []
    for name in nodes:

        lower = nodes[name]["Lower Limit"]
        upper = nodes[name]["Upper Limit"]

        load = getLoad(lower, upper)

        load_list.append(load)

    plotGraph(x=node_id_list, y=load_list,
              x_name="Node ID", y_name="Load (mbps)",
              color="orange", title=f"Load v/s Node Name Bar Chart for {region_name} Region",
              region_name=region_name)

    """ Plotting the Load Ratio Graph """

    # Scaling Load (0 to 1)
    max_load = max(load_list)
    load_ratio_list = list(map(lambda x: x/max_load, load_list))

    plotGraph(x=node_id_list, y=load_ratio_list,
              x_name="Node ID", y_name="Load Ratio",
              color="orange", title=f"Load Ratio v/s Node Name Bar Chart for {region_name} Region",
              region_name=region_name)

    """ Distributing Load """

    threshold = 0.75

    for i in range(len(load_ratio_list)):

        ratio = load_ratio_list[i]

        if ratio >= threshold:  # Ratio exceeds threshold value, then exchange

            difference = ratio - threshold

            least_ratio = min(load_ratio_list)
            least_ratio_index = load_ratio_list.index(least_ratio)

            if least_ratio + difference <= 0.75:    # Distributing Load only if Lower Bar after addition is < threshold
                ratio -= difference
                least_ratio += difference

            # Updating
            load_ratio_list[i] = ratio
            load_ratio_list[least_ratio_index] = least_ratio

    """ Plotting the Normalized Load Ratio Graph """

    plotGraph(x=node_id_list, y=load_ratio_list,
              x_name="Node ID", y_name="Load Ratio",
              color="green", title=f"Normalised Load Ratio v/s Node ID Bar Chart for {region_name} Region",
              region_name=region_name)

    print("Max Value of Normalized Load is:", max(load_ratio_list))

    return load_ratio_list


def plotLatencyAndLoad(node_id_list, latency_ratio_list, load_ratio_list, region_name):

    x_axis = np.arange(len(node_id_list))

    # Multi bar Chart
    plt.bar(x_axis - 0.2, latency_ratio_list, width=0.4, label="Latency")
    plt.bar(x_axis + 0.2, load_ratio_list, width=0.4, label="Load")

    plt.xticks(x_axis, node_id_list)
    plt.legend()

    plt.xlabel("Node ID")  # Naming the x-axis
    plt.ylabel("Ratio")  # Naming the y-axis
    plt.title("Multi Bar Chart for Latency and Load")  # Plot Title

    # Save the Plot in Graphs folder
    global GRAPH_NO
    region_name = region_name.replace(" ", "_")
    if not os.path.exists(f"Graphs/{region_name}"):
        os.makedirs(f"Graphs/{region_name}")
    plt.savefig(f"Graphs/{region_name}/{GRAPH_NO}_LatencyAndLoad.png")
    GRAPH_NO += 1

    plt.show()  # Display the plot


# Starting Point of the Program
def main():

    # Getting Region Details
    nodes, midpoint, region_name = Regions.getData()

    # Plotting Graph for Latency and Clusters
    node_id_list, latency_ratio_list = doRegion(nodes, midpoint, region_name)

    # For Load and Load Ratio
    load_ratio_list = doLoad(nodes, midpoint, region_name)

    # Plotting Multi Bar Chart for Latency & Load
    plotLatencyAndLoad(node_id_list, latency_ratio_list, load_ratio_list, region_name)


if __name__ == "__main__":
    main()
