""" Function to extract details about a node from csv file, while ignoring empty nodes. """

nodes = {}

file = open("F:\Python Programming\IEEE Task\Tata_Region_Nodes.txt","r")
lines = file.readlines()

for i in range(0,len(lines),8):
    
    if "node" in lines[i]:
        name = lines[i+2].split()[1].replace("\"","")
        nodes[name] = {}
        
        country = lines[i+3].split()[1].replace("\"","")
        nodes[name]["Country"] = country
        
        long = float(lines[i+4].split()[1])
        nodes[name]["Longitude"] = long
        
        lat = float(lines[i+6].split()[1])
        nodes[name]["Latitude"] = lat
        
        
print(nodes)

