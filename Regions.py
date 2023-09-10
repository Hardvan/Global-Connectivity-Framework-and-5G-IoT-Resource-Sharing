def BTAsiaPacific_Region():
    """Returns the nodes, midpoint and region name for BT Asia Pacific Region.

    Returns:
        nodes (dict): Dictionary of nodes with their details.
        midpoint (dict): Dictionary of midpoint with its details.
        region_name (str): Name of the region.
    """

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
    """Returns the nodes, midpoint and region name for Quest Region.

    Returns:
        nodes (dict): Dictionary of nodes with their details.
        midpoint (dict): Dictionary of midpoint with its details.
        region_name (str): Name of the region.
    """

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
    """Returns the nodes, midpoint and region name for TATA Region.

    Returns:
        nodes (dict): Dictionary of nodes with their details.
        midpoint (dict): Dictionary of midpoint with its details.
        region_name (str): Name of the region.
    """

    nodes = {}

    file = open("F:\Python Programming\IEEE Task\TATA_Region_Nodes.txt", "r")
    lines = file.readlines()

    # Extracting Nodes from the file
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
    """Returns the nodes, midpoint and region name for ERNET Region.

    Returns:
        nodes (dict): Dictionary of nodes with their details.
        midpoint (dict): Dictionary of midpoint with its details.
        region_name (str): Name of the region.
    """

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
    """Returns the nodes, midpoint and region name for PERN Region.

    Returns:
        nodes (dict): Dictionary of nodes with their details.
        midpoint (dict): Dictionary of midpoint with its details.
        region_name (str): Name of the region.
    """

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


def getData():

    choice = None
    nodes = None
    midpoint = None
    region_name = None

    print("Which Region?\n")
    print("Region 1: BT Asia-Pacific")
    print("Region 2: Quest")
    print("Region 3: TATA")
    print("Region 4: ERNET")
    print("Region 5: PERN")

    while True:
        choice = int(input("Enter your choice (1-5): "))
        if choice in range(1, 5+1):
            break
        else:
            print("Invalid Choice. Enter again")

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
