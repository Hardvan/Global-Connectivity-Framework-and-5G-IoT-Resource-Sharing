""" 1) Find Latency (Delay) for each Node. Latency = 2 * distance / speed.
    2) Plot Graph in ascending order.
    3) Clustering: Based on four Quadrants. Assume Midpoint as Origin."""

""" Things to Add:
    - Other Regions Nodes
    """




import random
import matplotlib.pyplot as plt
import math
import numpy as np
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
            continue

    if choice == 1:
        nodes, midpoint, region_name = BTAsiaPacific_Region()

    elif choice == 2:
        nodes, midpoint, region_name = Quest_Region()

    elif choice == 3:
        nodes, midpoint, region_name = TATA_Region()

    elif choice == 4:
        nodes, midpoint, region_name = ERNET_Region()

    elif choice == 5:
        nodes, midpoint, region_name = PERN_Region()

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

    long_km = long * 111.32 * math.cos(math.radians(lat))
    lat_km = lat * 110.574

    mid_long_km = mid_long * 111.32 * math.cos(math.radians(mid_lat))
    mid_lat_km = mid_lat * 110.574

    distance = math.sqrt((long_km - mid_long_km)**2 +
                         (lat_km - mid_lat_km)**2)     # in km

    speed = 3e5         # in km/s

    time = (2*distance/speed)*1000  # in ms

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

    return


def doRegion(nodes, midpoint, region_name):
    """ Getting Latency for Each Node """

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

        for j in range(i+1, len(latency_list)):

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
    """ Getting Lower and Upper limit for Load """

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

    return


def BTAsiaPacific_Region():

    nodes = {}

    # Jakarta
    nodes["Jakarta"] = {}
    nodes["Jakarta"]["Country"] = "Indonesia"
    nodes["Jakarta"]["Longitude"] = 106.84513
    nodes["Jakarta"]["Latitude"] = -6.21462

    # Perth
    nodes["Perth"] = {}
    nodes["Perth"]["Country"] = "Australia"
    nodes["Perth"]["Longitude"] = 115.83333
    nodes["Perth"]["Latitude"] = -31.93333

    # Singapore
    nodes["Singapore"] = {}
    nodes["Singapore"]["Country"] = "Singapore"
    nodes["Singapore"]["Longitude"] = 103.85007
    nodes["Singapore"]["Latitude"] = 1.28967

    # Kuala Lumpur
    nodes["Kuala Lumpur"] = {}
    nodes["Kuala Lumpur"]["Country"] = "Malaysia"
    nodes["Kuala Lumpur"]["Longitude"] = 101.68653
    nodes["Kuala Lumpur"]["Latitude"] = 3.1412

    # Sydney
    nodes["Sydney"] = {}
    nodes["Sydney"]["Country"] = "Australia"
    nodes["Sydney"]["Longitude"] = 151.20732
    nodes["Sydney"]["Latitude"] = -33.86785

    # Auckland
    nodes["Auckland"] = {}
    nodes["Auckland"]["Country"] = "New Zealand"
    nodes["Auckland"]["Longitude"] = 174.76667
    nodes["Auckland"]["Latitude"] = -36.86667

    # New Delhi
    nodes["New Delhi"] = {}
    nodes["New Delhi"]["Country"] = "India"
    nodes["New Delhi"]["Longitude"] = 77.22445
    nodes["New Delhi"]["Latitude"] = 28.63576

    # Mumbai
    nodes["Mumbai"] = {}
    nodes["Mumbai"]["Country"] = "India"
    nodes["Mumbai"]["Longitude"] = 72.84794
    nodes["Mumbai"]["Latitude"] = 19.01441

    # Seoul
    nodes["Seoul"] = {}
    nodes["Seoul"]["Country"] = "South Korea"
    nodes["Seoul"]["Longitude"] = 126.97783
    nodes["Seoul"]["Latitude"] = 37.56826

    # Tokyo
    nodes["Tokyo"] = {}
    nodes["Tokyo"]["Country"] = "Japan"
    nodes["Tokyo"]["Longitude"] = 139.5813
    nodes["Tokyo"]["Latitude"] = 35.61488

    # Taipei
    nodes["Taipei"] = {}
    nodes["Taipei"]["Country"] = "Taiwan"
    nodes["Taipei"]["Longitude"] = 121.53185
    nodes["Taipei"]["Latitude"] = 25.04776

    # Hong Kong
    nodes["Hong Kong"] = {}
    nodes["Hong Kong"]["Country"] = "Hong Kong"
    nodes["Hong Kong"]["Longitude"] = 114.15769
    nodes["Hong Kong"]["Latitude"] = 22.28552

    # Manila
    nodes["Manila"] = {}
    nodes["Manila"]["Country"] = "Philippines"
    nodes["Manila"]["Longitude"] = 120.9822
    nodes["Manila"]["Latitude"] = 14.6042

    # Bangkok
    nodes["Bangkok"] = {}
    nodes["Bangkok"]["Country"] = "Thailand"
    nodes["Bangkok"]["Longitude"] = 100.51667
    nodes["Bangkok"]["Latitude"] = 13.75

    # Chenai
    nodes["Chenai"] = {}
    nodes["Chenai"]["Country"] = "India"
    nodes["Chenai"]["Longitude"] = 80.27847
    nodes["Chenai"]["Latitude"] = 13.08784

    # Mumbai
    nodes["Mumbai"] = {}
    nodes["Mumbai"]["Country"] = "India"
    nodes["Mumbai"]["Longitude"] = 72.84794
    nodes["Mumbai"]["Latitude"] = 19.01441

    # Assigning Node ID
    i = 1
    for name in nodes:
        nodes[name]["Node ID"] = i
        i += 1

    # Mid-Point
    midpoint = {}
    midpoint["Label"] = "Banda Sea"
    midpoint["Longitude"] = 124.568393
    midpoint["Latitude"] = -2.539676

    # Region Name
    region_name = "BT Asia Pacific"

    return nodes, midpoint, region_name


def Quest_Region():

    nodes = {}

    file = open("F:\Python Programming\IEEE Task\QUEST_Region_Nodes.txt", "r")
    lines = file.readlines()

    for i in range(0, len(lines), 8):

        if "node" in lines[i]:
            name = lines[i+2].split()[1].replace("\"", "")
            nodes[name] = {}

            country = lines[i+3].split()[1].replace("\"", "")
            nodes[name]["Country"] = country

            long = float(lines[i+4].split()[1])
            nodes[name]["Longitude"] = long

            lat = float(lines[i+6].split()[1])
            nodes[name]["Latitude"] = lat

    # Assigning Node ID
    i = 1
    for name in nodes:
        nodes[name]["Node ID"] = i
        i += 1

    # Mid-Point
    midpoint = {}
    midpoint["Label"] = "Nagpur"
    midpoint["Longitude"] = -172.854899
    midpoint["Latitude"] = 34.782258

    # Region Name
    region_name = "QUEST"

    return nodes, midpoint, region_name


def TATA_Region():

    nodes = {}

    file = open("F:\Python Programming\IEEE Task\TATA_Region_Nodes.txt", "r")
    lines = file.readlines()

    for i in range(0, len(lines), 8):

        if "node" in lines[i]:
            name = lines[i+2].split()[1].replace("\"", "")
            nodes[name] = {}

            country = lines[i+3].split()[1].replace("\"", "")
            nodes[name]["Country"] = country

            long = float(lines[i+4].split()[1])
            nodes[name]["Longitude"] = long

            lat = float(lines[i+6].split()[1])
            nodes[name]["Latitude"] = lat

    # Assigning Node ID
    i = 1
    for name in nodes:
        nodes[name]["Node ID"] = i
        i += 1

    # Mid-Point
    midpoint = {}
    midpoint["Label"] = "Nagpur"
    midpoint["Longitude"] = 79.0809
    midpoint["Latitude"] = 21.1467

    # Region Name
    region_name = "TATA"

    return nodes, midpoint, region_name


def ERNET_Region():

    nodes = {}

    # Pune
    nodes["Pune"] = {}
    nodes["Pune"]["Country"] = "India"
    nodes["Pune"]["Longitude"] = 73.85535
    nodes["Pune"]["Latitude"] = 18.51957

    # Indore
    nodes["Indore"] = {}
    nodes["Indore"]["Country"] = "India"
    nodes["Indore"]["Longitude"] = 75.8333
    nodes["Indore"]["Latitude"] = 22.71792

    # Trivandrum
    nodes["Trivandrum"] = {}
    nodes["Trivandrum"]["Country"] = "India"
    nodes["Trivandrum"]["Longitude"] = 76.91667
    nodes["Trivandrum"]["Latitude"] = 8.48333

    # Mumbai
    nodes["Mumbai"] = {}
    nodes["Mumbai"]["Country"] = "India"
    nodes["Mumbai"]["Longitude"] = 72.84794
    nodes["Mumbai"]["Latitude"] = 19.01441

    # Ahmedabad
    nodes["Ahmedabad"] = {}
    nodes["Ahmedabad"]["Country"] = "India"
    nodes["Ahmedabad"]["Longitude"] = 72.61667
    nodes["Ahmedabad"]["Latitude"] = 23.03333

    # Jaipur
    nodes["Jaipur"] = {}
    nodes["Jaipur"]["Country"] = "India"
    nodes["Jaipur"]["Longitude"] = 75.81667
    nodes["Jaipur"]["Latitude"] = 26.91667

    # Chennai
    nodes["Chennai"] = {}
    nodes["Chennai"]["Country"] = "India"
    nodes["Chennai"]["Longitude"] = 80.27847
    nodes["Chennai"]["Latitude"] = 13.08784

    # Bengaluru
    nodes["Bengaluru"] = {}
    nodes["Bengaluru"]["Country"] = "India"
    nodes["Bengaluru"]["Longitude"] = 77.60329
    nodes["Bengaluru"]["Latitude"] = 12.97623

    # Delhi
    nodes["Delhi"] = {}
    nodes["Delhi"]["Country"] = "India"
    nodes["Delhi"]["Longitude"] = 77.22445
    nodes["Delhi"]["Latitude"] = 28.63576

    # Guwahati
    nodes["Guwahati"] = {}
    nodes["Guwahati"]["Country"] = "India"
    nodes["Guwahati"]["Longitude"] = 91.75095
    nodes["Guwahati"]["Latitude"] = 26.18617

    # Gorakhpur
    nodes["Gorakhpur"] = {}
    nodes["Gorakhpur"]["Country"] = "India"
    nodes["Gorakhpur"]["Longitude"] = 75.68333
    nodes["Gorakhpur"]["Latitude"] = 29.45

    # Kanpur
    nodes["Kanpur"] = {}
    nodes["Kanpur"]["Country"] = "India"
    nodes["Kanpur"]["Longitude"] = 80.35
    nodes["Kanpur"]["Latitude"] = 26.46667

    # Allahabad
    nodes["Kanpur"] = {}
    nodes["Kanpur"]["Country"] = "India"
    nodes["Kanpur"]["Longitude"] = 81.85
    nodes["Kanpur"]["Latitude"] = 25.45

    # Kalkota
    nodes["Kalkota"] = {}
    nodes["Kalkota"]["Country"] = "India"
    nodes["Kalkota"]["Longitude"] = 88.36972
    nodes["Kalkota"]["Latitude"] = 22.56972

    # Bhubaneswar
    nodes["Bhubaneswar"] = {}
    nodes["Bhubaneswar"]["Country"] = "India"
    nodes["Bhubaneswar"]["Longitude"] = 85.83333
    nodes["Bhubaneswar"]["Latitude"] = 20.23333

    # Hyderabad
    nodes["Hyderabad"] = {}
    nodes["Hyderabad"]["Country"] = "India"
    nodes["Hyderabad"]["Longitude"] = 78.47444
    nodes["Hyderabad"]["Latitude"] = 17.37528

    # Assigning Node ID
    i = 1
    for name in nodes:
        nodes[name]["Node ID"] = i
        i += 1

    # Mid-Point
    midpoint = {}
    midpoint["Label"] = "Nagpur"
    midpoint["Longitude"] = 79.0809
    midpoint["Latitude"] = 21.1467

    # Region Name
    region_name = "ERNET"

    return nodes, midpoint, region_name


def PERN_Region():

    nodes = {}

    # Peshawar
    nodes["Peshawar"] = {}
    nodes["Peshawar"]["Country"] = "Pakistan"
    nodes["Peshawar"]["Longitude"] = 71.58018
    nodes["Peshawar"]["Latitude"] = 34.00837

    # Karachi
    nodes["Karachi"] = {}
    nodes["Karachi"]["Country"] = "Pakistan"
    nodes["Karachi"]["Longitude"] = 67.0822
    nodes["Karachi"]["Latitude"] = 24.9056

    # Faisalabad
    nodes["Faisalabad"] = {}
    nodes["Faisalabad"]["Country"] = "Pakistan"
    nodes["Faisalabad"]["Longitude"] = 73.08333
    nodes["Faisalabad"]["Latitude"] = 31.41667

    # Quetta
    nodes["Quetta"] = {}
    nodes["Quetta"]["Country"] = "Pakistan"
    nodes["Quetta"]["Longitude"] = 67.0125
    nodes["Quetta"]["Latitude"] = 30.18722

    # Lahore
    nodes["Lahore"] = {}
    nodes["Lahore"]["Country"] = "Pakistan"
    nodes["Lahore"]["Longitude"] = 74.34361
    nodes["Lahore"]["Latitude"] = 31.54972

    # Abbottabad
    nodes["Abbottabad"] = {}
    nodes["Abbottabad"]["Country"] = "Pakistan"
    nodes["Abbottabad"]["Longitude"] = 73.21449
    nodes["Abbottabad"]["Latitude"] = 34.14685

    # Islamabad
    nodes["Islamabad"] = {}
    nodes["Islamabad"]["Country"] = "Pakistan"
    nodes["Islamabad"]["Longitude"] = 73.04329
    nodes["Islamabad"]["Latitude"] = 33.72148

    # Assigning Node ID
    i = 1
    for name in nodes:
        nodes[name]["Node ID"] = i
        i += 1

    # Mid-Point
    midpoint = {}
    midpoint["Label"] = "Banda Sea"
    midpoint["Longitude"] = 73.260825
    midpoint["Latitude"] = 29.195361

    # Region Name
    region_name = "QUEST"

    return nodes, midpoint, region_name


# TOP - LEVEL STATEMENTS
# Getting Region Details
nodes, midpoint, region_name = getData()


# Plotting Graph for Latency and Clusters
node_id_list, latency_ratio_list = doRegion(nodes, midpoint, region_name)


# For Load and Load Ratio
load_ratio_list = doLoad(nodes, midpoint, region_name)


# Plotting Multi Bar Chart for Latency & Load
plotLatencyAndLoad(node_id_list, latency_ratio_list, load_ratio_list)
