""" 
    Flow of execution:
    1. Get region details such as nodes, midpoint and region name from Regions.py
    2. doRegion() function:
        Plot Latency v/s Node ID Bar Chart
        Plot Ascending Latency v/s Node ID Bar Chart
        Plot Latency v/s Quadrant Chart
        Plot Latency Ratio v/s Node ID Bar Chart
        Plot Normalised Latency Ratio v/s Node ID Bar Chart
    3. doLoad() function:
        Plot Load v/s Node ID Bar Chart
        Plot Load Ratio v/s Node ID Bar Chart
        Plot Normalised Load Ratio v/s Node ID Bar Chart
    4. plotLatencyAndLoad() function:
        Plot Multi Bar Chart for Latency and Load

    TODO:
    1. Shortest path from midpoint to all nodes: Apply Bellman Ford algorithm.
    2. Maximum flow (load) in the network region: Apply Ford Fulkerson Algorithm.
"""


import matplotlib.pyplot as plt
import numpy as np
import os

# Custom Modules
import Regions
from Metrics import *


# GLOBAL VARIABLES
GRAPH_NO = 1  # For naming the Graphs


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

    # Scaling Latency (0 to 1)
    max_latency = max(latency_list)
    latency_ratio_list = list(map(lambda x: x/max_latency, latency_list))

    plotGraph(x=node_id_list, y=latency_ratio_list,
              x_name="Node ID", y_name="Latency Ratio",
              color="Purple", title=f"Latency Ratio v/s Node ID for {region_name} Region",
              region_name=region_name)

    """ Distributing Latency (Normalizing) """

    threshold = 0.75
    print(f"Threshold Value for Latency: {threshold}")

    for i in range(len(latency_ratio_list)):

        ratio = latency_ratio_list[i]

        if ratio >= threshold:  # Ratio exceeds threshold value, then exchange

            difference = ratio - threshold

            # Find the least ratio and its index
            least_ratio = min(latency_ratio_list)
            least_ratio_index = latency_ratio_list.index(least_ratio)

            if least_ratio + difference <= 0.75:  # Distributing Load only if Lower Bar after addition is < threshold
                ratio -= difference
                least_ratio += difference
            else:
                print("❌ Cannot Distribute Load in this Region")
                print("Continuing anyway...")

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

    """ Distributing Load (Normalizing) """

    threshold = 0.75
    print(f"Threshold Value for Load: {threshold}")

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


def bellmanFord(nodes, midpoint, region_name):
    """Shortest path from user selected source to all nodes in the region

    Args:
        nodes (dict): Dictionary of Nodes
        midpoint (dict): Dictionary of Midpoint
        region_name (str): Name of the Region

    Algorithm:
    1. Ask user for source node (display all nodes & their ids)
    2. Create adjacency list for all nodes in the format: {node: [[neighbour1, weight1], [neighbour2, weight2]]}
    3. Apply Bellman Ford Algorithm
    4. Plot the Graph
    5. Print the Shortest Path
    """

    print("Applying Bellman Ford Algorithm...")

    # Node ID -> Name, Name -> Node ID mapping
    node_id_to_name = {nodes[name]["Node ID"]: name for name in nodes}
    name_to_node_id = {name: nodes[name]["Node ID"] for name in nodes}

    # 1. Ask user for source node (display all nodes & their ids)
    print("Select Source Node:")
    for name in nodes:
        print(f"{nodes[name]['Node ID']} : {name}")

    source_node_id = int(input("Enter Node ID: "))
    source_node_name = node_id_to_name[source_node_id]

    print(
        f"Selected Source Node: {source_node_name} (Node ID: {source_node_id})")

    # 2. Create adjacency list for all nodes in the format:
    # {node: [[neighbour1, weight1], [neighbour2, weight2]]}
    adjacency_list = {}
    for name in nodes:
        adjacency_list[name] = []
        for neighbour_name in nodes:  # Getting Latency for each neighbour

            if name == neighbour_name:  # Skip if same node
                continue

            longitude = nodes[name]["Longitude"]
            latitude = nodes[name]["Latitude"]
            neighbour_longitude = nodes[neighbour_name]["Longitude"]
            neighbour_latitude = nodes[neighbour_name]["Latitude"]

            latency = getLatency(
                longitude, latitude, neighbour_longitude, neighbour_latitude)
            latency = round(latency, 2)

            adjacency_list[name].append(
                [neighbour_name, latency])

    # Save the Adjacency List in a text file
    # Separate table for each node
    # Each table will have columns: Neighbour Name, Latency
    with open("bellman.md", "w") as file:
        file.write(f"# Bellman Ford for {region_name} Region\n\n")

        file.write(f"No. of Nodes: {len(nodes)}\n\n")

        for name in adjacency_list:
            file.write(f"## Adjacency List for {name} Node\n\n")
            file.write("| Neighbour Name | Latency (ms) |\n")
            file.write("| --- | --- |\n")
            for neighbour_name, latency in adjacency_list[name]:
                file.write(f"| {neighbour_name} | {latency} |\n")
            file.write("\n")
    print("✅ Adjacency List saved in bellman.md")

    # To check bellman ford algorithm, make half of the latencies from source to neighbours as a large number
    for i in range(len(adjacency_list[source_node_name])):
        if random.randint(0, 1) == 1:
            adjacency_list[source_node_name][i][1] = round(10000 *
                                                           random.uniform(1, 10), 2)

    # Append the Adjacency List for the Source Node in a text file
    with open("bellman.md", "a") as file:
        file.write(
            f"## Adjacency List for Source Node: '{source_node_name}' after converting ~ 50% of latencies to a large number\n\n")
        file.write("| Neighbour Name | Latency (ms) |\n")
        file.write("| --- | --- |\n")
        for neighbour_name, latency in adjacency_list[source_node_name]:
            file.write(f"| {neighbour_name} | {latency} |\n")
        file.write("\n")

    # 3. Apply Bellman Ford Algorithm
    # 3.1. Initialize distance of all nodes to infinity
    distance = {}
    for name in nodes:
        distance[name] = float("inf")

    # 3.2. Distance of source node to itself is 0
    distance[source_node_name] = 0

    # 3.3 Save old distance from source node to neighbour latency
    old_distance = {}
    for neighbour_name, latency in adjacency_list[source_node_name]:
        old_distance[neighbour_name] = latency

    # 3.3. Initialize path to reach each neighbor
    path = {}
    for name in nodes:
        path[name] = []

    # 3.4. Relax all edges |V| - 1 times
    for _ in range(len(nodes) - 1):
        for name in nodes:
            for neighbour_name, latency in adjacency_list[name]:
                if distance[name] != float("inf") and distance[name] + latency < distance[neighbour_name]:
                    distance[neighbour_name] = distance[name] + latency
                    path[neighbour_name] = path[name] + [neighbour_name]

    # 3.4. Check for negative-weight cycles
    for name in nodes:
        for neighbour_name, latency in adjacency_list[name]:
            if distance[name] != float("inf") and distance[name] + latency < distance[neighbour_name]:
                print("❌ Negative Weight Cycle Exists")
                return

    # Round all distances to 2 decimal places
    for name in nodes:
        distance[name] = round(distance[name], 2)

    print("✅ Bellman Ford Algorithm Applied")

    # 4. Append the shortest path in bellman.md
    print("Shortest Path from Source Node to all Nodes:")
    with open("bellman.md", "a") as file:
        file.write("## Shortest Path from Source Node to all Nodes\n")
        file.write(
            "| Node Name | New Distance (ms) | Old Distance (ms) | Path |\n")
        file.write("| --- | --- | --- | --- |\n")
        for name in nodes:
            file.write(
                f"| {name} | {distance[name]} | {old_distance.get(name, 0)} | {' -> '.join(path[name])} |\n")
    print("✅ Shortest Path saved in bellman.md")


# Starting Point of the Program
def main():

    do_latency = False  # ? True/False to plot Latency Graphs
    do_load = False  # ? True/False to plot Load Graphs
    do_bellman_ford = True  # ? True/False to apply Bellman Ford Algorithm

    # Getting Region Details
    nodes, midpoint, region_name = Regions.getData()

    # Plotting Graph for Latency and Clusters
    if do_latency:
        node_id_list, latency_ratio_list = doRegion(
            nodes, midpoint, region_name)

    # For Load and Load Ratio
    if do_load:
        load_ratio_list = doLoad(nodes, midpoint, region_name)

    # Plotting Multi Bar Chart for Latency & Load
    if do_latency and do_load:
        plotLatencyAndLoad(node_id_list, latency_ratio_list,
                           load_ratio_list, region_name)

    # Applying Bellman Ford Algorithm
    if do_bellman_ford:
        bellmanFord(nodes, midpoint, region_name)


if __name__ == "__main__":
    main()
