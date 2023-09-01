""" 1) Find Latency (Delay) for each Node. Latency = 2 * distance / speed.
    2) Plot Graph in ascending order.
    3) Clustering: Based on four Quadrants. Assume Midpoint as Origin."""


import random
import matplotlib.pyplot as plt
import math
import numpy as np

# Custom Modules
import Regions


def getLowerAndUpper():

    lower = random.randint(10, 60)
    upper = random.randint(100, 400)

    return lower, upper


def getData():

    choice = None
    nodes = None
    midpoint = None
    region_name = None

    print("Which Region?")
    print("""Region 1: BT Asia-Pacific\n
          Region 2: Quest\n
          Region 3: TATA\n
          Region 4: ERNET\n
          Region 5: PERN""")

    while True:
        choice = int(input("Enter your choice (1-5): "))
        if choice in range(1, 5+1):
            break
        else:
            print("Invalid Choice. Enter again")

    if choice == 1:
        nodes, midpoint, region_name = Regions.BTAsiaPacific_Region()

    elif choice == 2:
        nodes, midpoint, region_name = Regions.Quest_Region()

    elif choice == 3:
        nodes, midpoint, region_name = Regions.TATA_Region()

    elif choice == 4:
        nodes, midpoint, region_name = Regions.ERNET_Region()

    elif choice == 5:
        nodes, midpoint, region_name = Regions.PERN_Region()

    return nodes, midpoint, region_name


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

    # function to show the plot
    plt.show()

    # Save the Plot in Graphs folder
    plt.savefig("Graphs/"+title+".png")


def doRegion(nodes, midpoint, region_name):

    # Getting Latency for Each Node
    for name in nodes:

        longitude = nodes[name]["Longitude"]
        latitude = nodes[name]["Latitude"]

        mid_longitude = midpoint["Longitude"]
        mid_latitude = midpoint["Latitude"]

        latency = getLatency(longitude, latitude, mid_longitude, mid_latitude)

        nodes[name]["Latency"] = latency

    """ Plotting Latency Graph in Normal Order """

    # Extracting all names and latencies in two lists

    node_id_list = []
    for name in nodes:
        node_id_list.append(nodes[name]["Node ID"])

    latency_list = []
    for name in nodes:
        latency = nodes[name]["Latency"]
        latency_list.append(latency)

    plotGraph(x=node_id_list, y=latency_list,
              x_name="Node ID", y_name="Latency (ms)",
              color="blue", title="Latency v/s Node ID Bar Chart for "+region_name+" Region")

    """ Plotting Latency Graph in Ascending Order """

    # Performing selection sort to exchange node ids and latencies
    for i in range(len(latency_list)):

        for j in range(i + 1, len(latency_list)):

            if latency_list[i] > latency_list[j]:

                # Swapping Latencies
                temp = latency_list[i]
                latency_list[i] = latency_list[j]
                latency_list[j] = temp

                # Swapping Node IDs
                temp = node_id_list[i]
                node_id_list[i] = node_id_list[j]
                node_id_list[j] = temp

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

        quadrant_name = "Quadrant " + str(quadrant_no)

        # Extracting all node ids and latencies in two lists

        node_id_list = []
        for name in quadrant_nodes:
            node_id_list.append(quadrant_nodes[name]["Node ID"])

        latency_list = []
        for name in quadrant_nodes:
            latency_list.append(quadrant_nodes[name]["Latency"])

        plotGraph(x=node_id_list, y=latency_list,
                  x_name="Node ID", y_name="Latency (ms)",
                  color=color_list[quadrant_no-1], title="Latency v/s "+quadrant_name+" Chart")

    """ Plotting Latency Ratio Graph """

    node_id_list = []
    for name in nodes:
        node_id_list.append(nodes[name]["Node ID"])

    latency_list = []
    for name in nodes:
        latency = nodes[name]["Latency"]
        latency_list.append(latency)

    latency_ratio_list = list(map(lambda x: x/max(latency_list), latency_list))

    plotGraph(x=node_id_list, y=latency_ratio_list,
              x_name="Node ID", y_name="Latency Ratio",
              color="Purple", title="Latency Ratio v/s Node ID for "+region_name+" Region")

    """ Distributing Latency """

    threshold = 0.75

    for i in range(len(latency_ratio_list)):

        ratio = latency_ratio_list[i]

        if ratio >= threshold:  # Ratio exceeds threshold value, then exchange

            difference = ratio - threshold

            least_ratio = min(latency_ratio_list)
            least_ratio_index = latency_ratio_list.index(least_ratio)

            if least_ratio + difference <= 0.75:    # Distributing Load only if Lower Bar after addition is < threshold
                ratio -= difference
                least_ratio += difference

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

    node_id_list = []
    for name in nodes:
        node_id_list.append(nodes[name]["Node ID"])

    load_list = []
    for name in nodes:

        lower = nodes[name]["Lower Limit"]
        upper = nodes[name]["Upper Limit"]

        load = random.randint(lower, upper)
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

    # Display
    plt.show()

    # Save the Plot in Graphs folder
    plt.savefig("Graphs/LatencyAndLoad.png")


# TOP LEVEL STATEMENTS

def main():

    # Getting Region Details
    nodes, midpoint, region_name = getData()

    # Plotting Graph for Latency and Clusters
    node_id_list, latency_ratio_list = doRegion(nodes, midpoint, region_name)

    # For Load and Load Ratio
    load_ratio_list = doLoad(nodes, midpoint, region_name)

    # Plotting Multi Bar Chart for Latency & Load
    plotLatencyAndLoad(node_id_list, latency_ratio_list, load_ratio_list)


if __name__ == "__main__":
    main()
