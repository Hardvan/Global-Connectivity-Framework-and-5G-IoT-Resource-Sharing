""" 1) Find Latency (Delay) for each Node. Latency = 2 * distance / speed.
    2) Plot Graph in ascending order.
    3) Clustering: Based on four Quadrants. Assume Midpoint as Origin."""


import random
import matplotlib.pyplot as plt
import math
import numpy as np

# Custom Modules
import Regions


GRAPH_NO = 1  # For naming the Graphs


def getLowerAndUpper():

    lower = random.randint(10, 60)
    upper = random.randint(100, 400)

    return lower, upper


def getQuadrant(long, lat, mid_long, mid_lat):

    quadrant = None

    # Origin
    X = mid_long
    Y = mid_lat

    # Current Point
    x = long
    y = lat

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
    Formula: Latency = 2 * distance / speed

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

    speed = 3e5         # in km/s

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


def plotGraph(x, y, x_name, y_name, color, title):

    # x-coordinates of left sides of bars
    left = list(range(1, len(x)+1))

    # Heights of bars: y

    # Labels for bars: x_name

    # Plotting a Bar Chart
    plt.bar(left, y, tick_label=x,
            width=0.8, color=[color])

    # Naming the x-axis
    plt.xlabel(x_name)

    # Naming the y-axis
    plt.ylabel(y_name)

    # Plot Title
    plt.title(title)

    # Save the Plot in Graphs folder
    title = title.replace(" ", "_")
    title = title.replace("/", "_")
    global GRAPH_NO
    plt.savefig(f"Graphs/{GRAPH_NO}_{title}.png")
    GRAPH_NO += 1

    # function to show the plot
    plt.show()


def doRegion(nodes, midpoint, region_name):

    # Getting Latency for Each Node
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
              color="blue", title=f"Latency v/s Node ID Bar Chart for {region_name} Region")

    """ Plotting Latency Graph in Ascending Order """

    # Performing selection sort to exchange node ids and latencies
    n = len(latency_list)
    for i in range(n):

        for j in range(i + 1, n):

            if latency_list[i] > latency_list[j]:

                # Swapping Latencies
                latency_list[i], latency_list[j] = latency_list[j], latency_list[i]

                # Swapping Node IDs
                node_id_list[i], node_id_list[j] = node_id_list[j], node_id_list[i]

    plotGraph(x=node_id_list, y=latency_list,
              x_name="Node ID", y_name="Latency (ms)",
              color="blue", title="Ascending Latency v/s Node ID Bar Chart for "+region_name+" Region")

    """ Dividing into Clusters """

    # Stored as {1:{"Pune":{"Country":"India"}}}
    cluster_dictionary = {1: {}, 2: {}, 3: {}, 4: {}}

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

        quadrant_nodes = cluster_dictionary[quadrant_no]

        quadrant_name = f"Quadrant {quadrant_no}"

        # Extracting all node ids and latencies in two lists

        node_id_list = [quadrant_nodes[name]["Node ID"]
                        for name in quadrant_nodes]
        latency_list = [quadrant_nodes[name]["Latency"]
                        for name in quadrant_nodes]

        plotGraph(x=node_id_list, y=latency_list,
                  x_name="Node ID", y_name="Latency (ms)",
                  color=color_list[quadrant_no-1], title="Latency v/s "+quadrant_name+" Chart")

    """ Plotting Latency Ratio Graph """

    node_id_list = [nodes[name]["Node ID"] for name in nodes]
    latency_list = [nodes[name]["Latency"] for name in nodes]

    # Normalizing Latency (0 to 1)
    max_latency = max(latency_list)
    latency_ratio_list = list(map(lambda x: x/max_latency, latency_list))

    plotGraph(x=node_id_list, y=latency_ratio_list,
              x_name="Node ID", y_name="Latency Ratio",
              color="Purple", title="Latency Ratio v/s Node ID for "+region_name+" Region")

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
              color="Green", title="Normalised Latency Ratio v/s Node ID Bar Chart for "+region_name+" Region")

    print("Max Value of Normalized Latency is:", max(latency_ratio_list))

    return node_id_list, latency_ratio_list


def doLoad(nodes, midpoint, region_name):

    # Getting Lower and Upper limit for Load
    for name in nodes:

        lower, upper = getLowerAndUpper()
        nodes[name]["Lower Limit"] = lower
        nodes[name]["Upper Limit"] = upper

    node_id_list = [nodes[name]["Node ID"] for name in nodes]

    load_list = []
    for name in nodes:

        lower = nodes[name]["Lower Limit"]
        upper = nodes[name]["Upper Limit"]

        load = getLoad(lower, upper)

        load_list.append(load)

    plotGraph(x=node_id_list, y=load_list,
              x_name="Node ID", y_name="Load (mbps)",
              color="orange", title="Load v/s Node Name Bar Chart for "+region_name+" Region")

    """ Plotting the Load Ratio Graph """

    max_load = max(load_list)
    load_ratio_list = list(map(lambda x: x/max_load, load_list))

    plotGraph(x=node_id_list, y=load_ratio_list,
              x_name="Node ID", y_name="Load Ratio",
              color="orange", title="Load Ratio v/s Node Name Bar Chart for "+region_name+" Region")

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
              color="green", title="Normalised Load Ratio v/s Node ID Bar Chart for "+region_name+" Region")

    print("Max Value of Normalized Load is:", max(load_ratio_list))

    return load_ratio_list


def plotLatencyAndLoad(node_id_list, latency_ratio_list, load_ratio_list):

    # Define Data

    x_axis = np.arange(len(node_id_list))

    # Multi bar Chart

    plt.bar(x_axis - 0.2, latency_ratio_list, width=0.4, label="Latency")
    plt.bar(x_axis + 0.2, load_ratio_list, width=0.4, label="Load")

    # Xticks
    plt.xticks(x_axis, node_id_list)

    # Add legend
    plt.legend()

    # Naming the x-axis
    plt.xlabel("Node ID")

    # Naming the y-axis
    plt.ylabel("Ratio")

    # Plot Title
    plt.title("Multi Bar Chart for Latency and Load")

    # Save the Plot in Graphs folder
    global GRAPH_NO
    plt.savefig(f"Graphs/{GRAPH_NO}_LatencyAndLoad.png")
    GRAPH_NO += 1

    # Display
    plt.show()


# TOP LEVEL STATEMENTS

def main():

    # Getting Region Details
    nodes, midpoint, region_name = Regions.getData()

    # Plotting Graph for Latency and Clusters
    node_id_list, latency_ratio_list = doRegion(nodes, midpoint, region_name)

    # For Load and Load Ratio
    load_ratio_list = doLoad(nodes, midpoint, region_name)

    # Plotting Multi Bar Chart for Latency & Load
    plotLatencyAndLoad(node_id_list, latency_ratio_list, load_ratio_list)


if __name__ == "__main__":
    main()